%{
#ifdef YYDEBUG
  extern int yydebug=1;
#endif


#include <stdio.h>
#include <string.h> 
#include "ipp.h"

#ifndef SCAN_ERR
#define SCAN_ERR
#define DOMDEF_EXPECTED            0
#define DOMAIN_EXPECTED            1
#define DOMNAME_EXPECTED           2
#define LBRACKET_EXPECTED          3
#define RBRACKET_EXPECTED          4
#define DOMDEFS_EXPECTED           5
#define REQUIREM_EXPECTED          6
#define TYPEDLIST_EXPECTED         7
#define LITERAL_EXPECTED           8
#define PRECONDDEF_UNCORRECT       9
#define TYPEDEF_EXPECTED          10
#define CONSTLIST_EXPECTED        11
#define PREDDEF_EXPECTED          12 
#define NAME_EXPECTED             13
#define VARIABLE_EXPECTED         14
#define ACTIONFUNCTOR_EXPECTED    15
#define ATOM_FORMULA_EXPECTED     16
#define EFFECT_DEF_EXPECTED       17
#define NEG_FORMULA_EXPECTED      18
#define NOT_SUPPORTED             19
#define ACTION                    20
  
#endif

  char *adl_string[] = { "nothing", "literal", "and", "or","imply", 
		  "not", "exists", 
		  "forall", "(", ")", 
		  "variable", "endnot",
		  NULL };     

static char *errmsg[] = {
  "domain definition expected",
  "'domain' expected",
  "domain name expected",
  "'(' expected",
  "')' expected",
  "additional domain definitions expected",
  "requirements (e.g. ':STRIPS') expected",
  "typed list of <%s> expected",
  "literal expected",
  "uncorrect precondition definition",
  "type definition expected",
  "list of constants expected",
  "predicate definition expected",
  "<name> expected",
  "<variable> expected",
  "action functor expected",
  "atomic formula expected",
  "effect definition expected",
  "negated atomic formula expected",
  "requirement %s not supported by this IPP version",  
  "action definition is not correct",
  NULL
};

#define NAME_STR "name\0"
#define VARIABLE_STR "variable\0"
#define STANDARD_TYPE "OBJECT\0"

 
//void opserr( int errno, char *par );
void opserr( int errno, char *par )
{
  act_err = errno;
  if ( act_err_par )
    free( act_err_par );
  if ( par )
    {
      act_err_par = new_token( strlen(par)+1 );
      strcpy( act_err_par, par);
    }
  else
    act_err_par = NULL;
}

int act_err;
char *act_err_par = NULL;
op_list cur_op = NULL;
fact_list cur_fl;

%}

%start file

/* This may seem strange, but enables us to use the types known from
   ipp.h */
%union {
  char string[256];
  token token;
  fact_list fact_list;
  op_list op_list;
  token_list token_list;
  effect_list effect_list;
}


%type <effect_list> adl_effect
%type <effect_list> adl_effect_star
%type <fact_list> adl_goal_description
%type <fact_list> adl_goal_description_star
%type <token_list> literal_term
%type <token_list> term_star
%type <fact_list> typed_list_name
%type <fact_list> typed_list_variable
%type <fact_list> axiom_vars_def
%type <token> term
%type <token_list> atomic_formula_term
%type <token_list> name_plus
%type <token> predicate


%token DEFINE_TOK
%token DOMAIN_TOK
%token REQUIREMENTS_TOK
%token TYPES_TOK
%token EITHER_TOK
%token CONSTANTS_TOK
%token ACTION_TOK
%token AXIOM_TOK
%token VARS_TOK
%token PRECONDITION_TOK
%token PARAMETERS_TOK
%token EFFECT_TOK
%token AND_TOK
%token NOT_TOK
%token WHEN_TOK
%token FORALL_TOK
%token IMPLY_TOK
%token OR_TOK
%token EXISTS_TOK
%token EQUAL_TOK
%token <string> NAME
%token <string> VARIABLE
%token <string> TYPE


%%

/* numbers in comments are only useful for the programmer
   and reader of the yacc source code. Each terminal or
   non-terminal symbol and (which is not nice) each
   program section in {brackets} has a number and may
   be reached by the $ operator - the numbers only
   help prevent counting all the time and producing
   ugly fat spots on the monitor */

/**********************************************************************/
file:
{ opserr( DOMDEF_EXPECTED, NULL ); }
domain_definition 
;
/* can be extended to support 'addenda' and similar stuff */

/**********************************************************************/
domain_definition : 
'(' DEFINE_TOK  
domain_name       
{ 
  /* initialize typetree */
  global_type_tree_list = new_type_tree_list( STANDARD_TYPE );
}
optional_domain_defs 
{
  printf("\ndomain '%s' defined\n", gdomain_name );
}
;

/**********************************************************************/
domain_name :
'(' DOMAIN_TOK  NAME  ')' 
{ 
  gdomain_name = new_token( strlen($3)+1 );
  strcpy( gdomain_name, $3);
}
;

/**********************************************************************/
optional_domain_defs:
')'  /* end of domain */
|
require_def optional_domain_defs
|
constants_def optional_domain_defs
|
types_def optional_domain_defs
|
axiom_def optional_domain_defs
|
action_def optional_domain_defs
;


/**********************************************************************/
require_def:
'(' REQUIREMENTS_TOK 
{ opserr( REQUIREM_EXPECTED, NULL ); }
NAME
{ 
  if ( !supported( $4 ) )
    {
      opserr( NOT_SUPPORTED, $4 );
      yyerror();
    }
}
require_key_star
')'
;

require_key_star:
/* empty */
|
NAME
{ 
  if ( !supported( $1 ) )
    {
      opserr( NOT_SUPPORTED, $1 );
      yyerror();
    }
}
require_key_star
;

/**********************************************************************/
types_def:
'(' TYPES_TOK
{ opserr( TYPEDEF_EXPECTED, NULL ); }
typed_list_name 
')'
{ 
  add_to_type_tree( $4, main_type_tree() ); 
}
; 

/**********************************************************************/
constants_def:
'(' CONSTANTS_TOK
{ opserr( CONSTLIST_EXPECTED, NULL ); }
typed_list_name
')'
{ 
  orig_constant_list = $4;
}
;


/**********************************************************************
 * actions and their optional definitions
 **********************************************************************/

action_def:
'(' ACTION_TOK 
{ opserr( ACTION, NULL ); }
NAME
{ 
  cur_op = new_op_list( $4 );
}
param_def
action_def_body
')'
{
  cur_op->next = loaded_ops;
  loaded_ops = cur_op; 
}
;

/**********************************************************************/

param_def:
/* empty */
{ cur_op->params = NULL; }
|
PARAMETERS_TOK '(' typed_list_variable ')'
{
  fact_list f;
  cur_op->params = $3;
  for( f=cur_op->params; f; f = f->next )
    cur_op->number_of_real_params++; /* to be able to distinguish
					params from :VARS */
}

/**********************************************************************/

action_def_body:
/* empty */
|
VARS_TOK '(' typed_list_variable ')' action_def_body
{
  fact_list f;
  token t;
  /* add vars as parameters */
  if ( cur_op->params )
    {
      for( f = cur_op->params; f->next; f = f->next )
	;
      f->next = $3;
      f = f->next;
    }
  else
    f = $3;
}
|
PRECONDITION_TOK
adl_goal_description
{ cur_op->preconds = $2; }
action_def_body
|
EFFECT_TOK
adl_effect
{ cur_op->effects = $2; }
action_def_body
;


/**********************************************************************
 * axioms (most of an axioms definition is handled by rules defined
 * for actions)
 **********************************************************************/

axiom_def:
'(' AXIOM_TOK 
{ 
  cur_op = new_axiom_op_list(); /* returns new operator the name of which
				   is AXIOM plus a number */
}
axiom_vars_def
{
  cur_op->params = $4;
}
action_def_body
')'
{
  /* Allowing complete "effects" is more than UCPOP and PDDL do,
     but this can easily be checked: the effect must be a single
     literal, otherwise axiom effects may become a little complicated */
  cur_op->next = loaded_axioms;
  loaded_axioms = cur_op;
  /* save axioms separately for now, after preprocessing they may
     be added to the other operators */
}
;

/**********************************************************************/

axiom_vars_def:
/* empty */
{ 
  $$ = NULL; 
}
|
VARS_TOK
'('
typed_list_variable
')'
{
  $$ = $3;
}
;

/**********************************************************************
 * goal description providing full ADL
/**********************************************************************/

adl_goal_description: /* this provides only an easy-to-handle
			 structure for pl1-expressions which will
			 be preprocessed later. returns fact_list */
literal_term
{ 
  $$ = new_fact_list();
  $$->item = $1;
}
|
'(' AND_TOK
adl_goal_description_star
')'
{ 
  fact_list f;
  
  $$ = make_adl_fact( AND_CONST );
  $$->next = $3; 
  for ( f=$$; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
}
|
'(' OR_TOK
adl_goal_description_star
')'
{ 
  fact_list f;
  
  $$ = make_adl_fact( OR_CONST );
  $$->next = $3; 
  for ( f=$$; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
}
|
'(' NOT_TOK
adl_goal_description
')'
{ 
  fact_list f;
  
  $$ = make_adl_fact( NOT_CONST );
  $$->next = $3; 
  for ( f=$$; f->next; f=f->next )
    ;
  f->next = make_adl_fact( ENDNOT_CONST );
}
|
'(' IMPLY_TOK
adl_goal_description
adl_goal_description
')'
{ 
  fact_list f;
  
  $$ = make_adl_fact( OR_CONST );
  $$->next = make_adl_fact( NOT_CONST );
  $$->next->next = $3; 
  for ( f=$$; f->next; f=f->next )
    ;
  f->next = make_adl_fact( ENDNOT_CONST);
  f->next->next = $4;
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
}
|
'(' EXISTS_TOK
'('
typed_list_variable
')'
adl_goal_description
')'
{ 
  fact_list f;
  
  $$ = f = make_adl_fact( EXISTS_CONST );
  f->next = make_adl_fact( LBRACK_CONST );
  f->next->next = $4; 
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
  f = f->next;
  f->next = $6;
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
}
|
'(' FORALL_TOK
'('
typed_list_variable
')'
adl_goal_description
')'
{ 
  fact_list f;
  
  $$ = f = make_adl_fact( FORALL_CONST );
  f->next = make_adl_fact( LBRACK_CONST );
  f->next->next = $4; 
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
  f = f->next;
  f->next = $6;
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
}
;


adl_goal_description_star:
{
  $$ = NULL;
}
|
adl_goal_description adl_goal_description_star
{
  fact_list f;

  $$ = $1;
  if ( !$$ )
    $$ = $2;
  else
    {
      for ( f = $$; f->next; f = f->next )
	;
      f->next = $2;
    }
}


/**********************************************************************
 * effects as allowed in pddl are saved in IPP data structures
 *********************************************************************/

adl_effect: /* describes everything after the keyword :effect */
literal_term
{
  $$ = new_effect_list();
  if ( ($1->item)[0] == '!' ) 
    {
      token_list tl;
      token t = new_token( strlen($1->item)+1-1 );
      strcpy( t, ($1->item)+1 );
      $$->del_effects = new_fact_list();
      $$->del_effects->item = new_token_list();
      $$->del_effects->item->item = t;
      $$->del_effects->item->next = $1->next;
    }
  else
    {
      $$->add_effects = new_fact_list();
      $$->add_effects->item = $1;
    }
}
|
'(' AND_TOK
adl_effect_star /* return effect_list */
')'
{
  /* check if effects are just literals i.e. atomic or negated
     atomic formula. If so, merge the effects */
  fflush( stdout );
  $$ = merge_literal_effects( $3 );
}  
|
'(' FORALL_TOK
'('
typed_list_variable
')'
adl_effect
')'
{
  /* $3 are parameters in all effects described in $5, so just bring
     the variables into the effects */
  effect_list cur_eff;
  fact_list par, end;

  $$ = $6;
  for ( cur_eff=$$; cur_eff; cur_eff=cur_eff->next )
    { /* for each effect already specified... */
      par=cur_eff->quantified_variables;
      if ( par )
	{
	  /* ...find all parameters specified yet... */
	  for ( ; par->next; par=par->next )
	    ;
	  /* ...and append new parameters. */
	  par->next = copy_complete_fact_list( $4, &end );
	}
      else
	{
	  /* ... or, if no other parameters, just copy the new ones */
	  cur_eff->quantified_variables = copy_complete_fact_list( $4, &end );
	}
    }
}
|
'(' WHEN_TOK
adl_goal_description
adl_effect
')'
{
  /* $3 is a condition for all elements of $4, so just bring the
     condition into the effects */
  effect_list cur_eff;
  fact_list cond, end;

  for ( $$=cur_eff=$4; cur_eff; cur_eff=cur_eff->next )
    { /* for each effect already specified... */
      if ( cur_eff->conditions )
	{
	  cond = cur_eff->conditions;
	  cur_eff->conditions = make_adl_fact( AND_CONST );
	  cur_eff->conditions->next = cond;
	  /* ...find all conditions specified yet... */
	  for ( ; cond->next; cond=cond->next )
	    ;
	  /* ...and append new conditions. */
	  cond->next = copy_complete_fact_list( $3, &end );
	  for ( ; cond->next; cond=cond->next )
	    ;
	  cond->next = make_adl_fact( RBRACK_CONST );
	}
      else
	{
	  /* ... or, if no other conditions, just copy the new ones */
	  cur_eff->conditions = copy_complete_fact_list( $3, &end );
	}
    }
}
;

adl_effect_star:
{ 
  $$ = NULL; 
}
|
adl_effect
adl_effect_star
{
  $$ = $1;
  $$->next = $2;
}
;



/**********************************************************************
 * some expressions used in many different rules
 **********************************************************************/

literal_term:
'(' NOT_TOK
atomic_formula_term
')'
{ 
  $$ = new_token_list();
  $$->item = new_token( strlen($3->item)+2 );
  strcpy( $$->item, "!" );
  strcat( $$->item, $3->item );
  $$->next = $3->next;
}
|
atomic_formula_term
{
  $$ = $1;
}
;

/**********************************************************************/

atomic_formula_term:
'('
predicate 
term_star
')'
{ 
  $$ = new_token_list();
  $$->item = new_token( strlen($2)+1 );
  strcpy( $$->item, $2 );
  $$->next = $3;
}
;

/**********************************************************************/

term_star:
/* empty */
{ $$ = NULL; }
|
term
term_star
{
  $$ = new_token_list();
  $$->item = new_token( strlen($1)+1 );
  strcpy( $$->item, $1 );
  $$->next = $2;
}
;

/**********************************************************************/

term:
NAME
{ 
  $$ = new_token( strlen($1)+1 );
  strcpy( $$, $1 );
}
|
VARIABLE
{ 
  $$ = new_token( strlen($1)+1 );
  strcpy( $$, $1 );
}
;

/**********************************************************************/

name_plus:
NAME
{
  $$ = new_token_list();
  $$->item = new_token( strlen($1)+1 );
  strcpy( $$->item, $1 );
}
|
NAME name_plus
{
  $$ = new_token_list();
  $$->item = new_token( strlen($1)+1 );
  strcpy( $$->item, $1 );
  $$->next = $2;
}


/**********************************************************************/

typed_list_name:     /* returns fact_list */
/* empty */
{ $$ = NULL; }
|
NAME EITHER_TOK name_plus ')' typed_list_name
{ /* this is a very, very special case... it may mean that
     a. a parameter has one of the types in name_plus
     b. a type is subtype of one of the following types in name_plus 
     => for both possibilities we use the same solution:
     build a new type name: either_name1_name2_..._namen and check
     if a type with this name already exists. If so then NAME has this type,
     if not then build a new type, include it in the type tree and
     return NAME with the new type 
     The new artificial type is not a subtype of OBJECT because its own
     elements must already be instances of a subtype of OBJECT */
  token s;
  token_list t;
  type_tree tt, root;
  type_tree_list rootl, *st;
  
  s = new_token( MAX_LENGTH );
  strcpy( s, EITHER_STR );
  for ( t = $3; t; t = t->next )
    {
      strcat( s, CONNECTOR );
      strcat( s, t->item );
    }
  tt = NULL;
  for ( rootl = global_type_tree_list; rootl; rootl = rootl->next )
    if ( tt = find_branch( s, root ) )
      break;
  if ( !tt )
    { /* the type doesn't exist yet, so build it */
      rootl = new_type_tree_list( s );
      rootl->next = global_type_tree_list;
      st = &(rootl->item->sub_types);
      for ( t = $3; t; t = t->next )
	{
	  if ( tt = find_branch( t->item, main_type_tree() ) )
	    {
	      *st = new_type_tree_list( NULL );
	      (*st)->item = tt;
	      st = &((*st)->next);
	    }
	}  
    }

  /* now do the simple stuff: return a name with a (quite complicated)
     type */
  $$ = new_fact_list();
  $$->item = new_token_list();
  $$->item->item = new_token( strlen($1)+1 );
  strcpy( $$->item->item, $1 );
  $$->item->next = new_token_list();
  $$->item->next->item = s;
  $$->next = $5;
}
|
NAME TYPE typed_list_name   /* end of list for one type */
{
  $$ = new_fact_list();
  $$->item = new_token_list();
  $$->item->item = new_token( strlen($1)+1 );
  strcpy( $$->item->item, $1 );
  $$->item->next = new_token_list();
  $$->item->next->item = new_token( strlen($2)+1 );
  strcpy( $$->item->next->item, $2 );
  $$->next = $3;
}
|
NAME typed_list_name        /* a list element (gets type from next one) */
{
  $$ = new_fact_list();
  $$->item = new_token_list();
  $$->item->item = new_token( strlen($1)+1 );
  strcpy( $$->item->item, $1 );
  $$->item->next = new_token_list();
  if ( $2 )   /* another element (already typed) is following */
    {
      char* s = $2->item->next->item;
      int   l = strlen( s ) + 1;
      $$->item->next->item = new_token( l );
      strcpy( $$->item->next->item, s ); /* same type as the next one */
      $$->next = $2;
    }
  else /* no further element - it must be an untyped list */
    {
      $$->item->next->item = new_token( strlen(STANDARD_TYPE)+1 );
      strcpy( $$->item->next->item, STANDARD_TYPE );
      $$->next = $2;
    }
}
;

/***********************************************/

typed_list_variable:     /* returns fact_list */
/* empty */
{ $$ = NULL; }
|
VARIABLE EITHER_TOK name_plus ')' typed_list_variable
{ /* this is a very, very special case... it may mean that
     a parameter has one of the types in name_plus
     => build a new type name: either_name1_name2_..._namen and check
     if a type with this name already exists. If so then NAME has this type,
     if not then build a new type, include it in the type tree and
     return NAME with the new type 
     The new artificial type is not a subtype of OBJECT because its own
     elements must already be instances of a subtype of OBJECT */
  token s;
  token_list t;
  type_tree tt, root;
  type_tree_list rootl, *st;
  
  s = new_token( MAX_LENGTH );
  strcpy( s, EITHER_STR );
  for ( t = $3; t; t = t->next )
    {
      strcat( s, CONNECTOR );
      strcat( s, t->item );
    }
  tt = NULL;
  for ( rootl = global_type_tree_list; rootl; rootl = rootl->next )
    if ( tt = find_branch( s, rootl->item ) )
      break;
  if ( !tt )
    { /* the type doesn't exist yet, so build it */
      rootl = new_type_tree_list( s );
      rootl->next = global_type_tree_list;
      st = &(rootl->item->sub_types);
      for ( t = $3; t; t = t->next )
	{
	  if ( tt = find_branch( t->item, main_type_tree() ) )
	    {
	      *st = new_type_tree_list( NULL );
	      (*st)->item = tt;
	      st = &((*st)->next);
	    }
	}  
      global_type_tree_list = rootl;
    }

  /* now do the simple stuff: return a name with a (quite complicated)
     type */
  $$ = new_fact_list();
  $$->item = new_token_list();
  $$->item->item = new_token( strlen($1)+1 );
  strcpy( $$->item->item, $1 );
  $$->item->next = new_token_list();
  $$->item->next->item = s;
  $$->next = $5;
}
|
VARIABLE TYPE typed_list_variable   /* end of list for one type */
{
  $$ = new_fact_list();
  $$->item = new_token_list();
  $$->item->item = new_token( strlen($1)+1 );
  strcpy( $$->item->item, $1 );
  $$->item->next = new_token_list();
  $$->item->next->item = new_token( strlen($2)+1 );
  strcpy( $$->item->next->item, $2 );
  $$->next = $3;
}
|
VARIABLE typed_list_variable    /* a list element (gets type from next one) */
{
  $$ = new_fact_list();
  $$->item = new_token_list();
  $$->item->item = new_token( strlen($1)+1 );
  strcpy( $$->item->item, $1 );
  $$->item->next = new_token_list();
  if ( $2 )   /* another element (already typed) is following */
    {
      char* s = $2->item->next->item;
      int   l = strlen( s );
      $$->item->next->item = new_token( l+1 );
      strcpy( $$->item->next->item, s ); /* same type as the next one */
      $$->next = $2;
    }
  else /* no further element - it must be an untyped list */
    {
      $$->item->next->item = new_token( strlen(STANDARD_TYPE)+1 );
      strcpy( $$->item->next->item, STANDARD_TYPE );
      $$->next = $2;
    }
}
;

/**********************************************************************/

predicate:
NAME
{ 
  $$ = new_token( strlen($1)+1 );
  strcpy( $$, $1 );
}
|
EQUAL_TOK
{ 
  $$ = new_token( strlen(EQ_STR)+1 );
  strcpy( $$, EQ_STR );
}
;




%%

#include "lex.ops.c"

/**********************************************************************
 * Functions
 **********************************************************************/

/* 
call	bison -pops -bscan-ops scan-ops.y

void opserr( int errno, char *par )
{
  act_err = errno;
  if ( act_err_par )
    free( act_err_par );
  if ( par )
    {
      act_err_par = new_token( strlen(par)+1 );
      strcpy( act_err_par, par);
    }
  else
    act_err_par = NULL;
}*/
  
int yyerror( char *msg )
{
  fflush( stdout );
  printf("\n%s: syntax error in line %d, '%s':\n", act_filename, lineno, yytext );
  if ( act_err_par )
    {
      printf( errmsg[act_err], act_err_par );
      printf( "\n" );
    }
  else
    printf("%s\n", errmsg[act_err] );

  OUTPUT_FILE;
  exit( 1 );
}


void load_ops_file( char *filename )
{
  FILE *fp;/* pointer to input files */

  /* open operator file */
  if( ( fp = fopen( filename, "r" ) ) == NULL ) {
    printf( "\nipp: can't find operator file: %s\n\n", filename );
    OUTPUT_FILE;
    exit( 1 );
  }
  act_filename = filename;
  lineno = 1; 
  yyin = fp;
  yyparse();
  fclose( fp );/* and close file again */
}


void print_ops( op_list op )
{ 
  
  op_list    i_op;

  for ( i_op = op; i_op; i_op = i_op->next ) {
    
    printf( "\n%s \n", i_op->name );

    printf( "v: (%d real params) ", i_op->number_of_real_params );
    print_factlist( i_op->params );

    printf( "\np: ");
    print_factlist( i_op->preconds );

    print_effect( i_op->effects );

  }
}

void print_effect( effect_list effects )
{
  effect_list i_list;

  printf( "\ne:");
  for ( i_list = effects; i_list; i_list = i_list->next ) {
    printf( "\n" );
    if ( i_list->quantified_variables ) {
      printf( "ALL " );
      print_factlist( i_list->quantified_variables );
    }
    if ( i_list->conditions ) {
      print_factlist( i_list->conditions );
      printf( "\n=> " ); 
    }
    if ( i_list->add_effects ) {
      printf( "ADD " );
      print_factlist( i_list->add_effects );
      if ( i_list->del_effects ) {
	printf( "DEL " );
	print_factlist( i_list->del_effects );
	printf( ";\n" );
      } else {
	printf( ";\n" );
      }
    } else {
      printf( "DEL " );
      print_factlist( i_list->del_effects );
      printf( ";\n" );
    }
  }
}


/***************************************************************/
/* those ones should be in somewhere in the IPP kernel         */

int supported( char *str )
{
  char *sup[] = { ":STRIPS", ":NEGATION", ":EQUALITY",":TYPING", 
		  ":CONDITIONAL-EFFECTS", ":DISJUNCTIVE-PRECONDITIONS", 
		  ":EXISTENTIAL-PRECONDITIONS", ":UNIVERSAL-PRECONDITIONS", 
		  ":QUANTIFIED-PRECONDITIONS", ":ADL",
		  ":DOMAIN-AXIOMS", ":SUBGOAL-THROUGH-AXIOMS",
		  NULL };     
  int i;
  
  for(i=0; sup[i]; i++ )
    if ( strcmp( sup[i], str ) == SAME )
      return TRUE;
  return FALSE;
}

void ahf( char *par, fact_list *f )
{
  token_list t;
  token s;

  if (!*f)
    return;
  t = (*f)->item;
  for ( ; t; t = t->next )
    if ( t->item[0] == '?' )
      if ( strcmp( t->item+1, par ) == SAME )
	{ /* okay, it's the same but not yet adjusted to the
	     hidden flag */
	  s = new_token( strlen( t->item ) + 2 );
	  sprintf( s, "?%s%s", HIDDEN_STR, par );
	  free( t->item );
	  t->item = s;
	}
  ahf( par, &(*f)->next );
} 

void adjust_hidden_flag( op_list op )
{
  fact_list par;
  effect_list eff;

  for( par = op->params; par; par = par->next )
    {
      if ( par->item->item[1] == HIDDEN_STR[0] )
	{
	  ahf( par->item->item+2, &op->preconds );
	  for ( eff = op->effects; eff; eff = eff->next )
	    {
	      ahf( par->item->item+2, &eff->conditions );
	      ahf( par->item->item+2, &eff->add_effects );
	      ahf( par->item->item+2, &eff->del_effects );
	    }
	}
    }
}
