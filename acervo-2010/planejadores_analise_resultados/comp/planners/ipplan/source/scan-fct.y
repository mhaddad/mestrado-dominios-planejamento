%{
#ifdef YYDEBUG
  extern int yydebug=1;
#endif


#include <stdio.h>
#include <string.h> 
#include "ipp.h"

#ifndef SCAN_ERR
#define SCAN_ERR
#define DEFINE_EXPECTED            0
#define PROBLEM_EXPECTED           1
#define PROBNAME_EXPECTED          2
#define LBRACKET_EXPECTED          3
#define RBRACKET_EXPECTED          4
#define DOMDEFS_EXPECTED           5
#define REQUIREM_EXPECTED          6
#define TYPEDLIST_EXPECTED         7
#define DOMEXT_EXPECTED            8
#define DOMEXTNAME_EXPECTED        9
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
#define SITUATION_EXPECTED        20
#define SITNAME_EXPECTED          21
#define BDOMAIN_EXPECTED          22
#define BADDOMAIN                 23
#define INIFACTS                  24
#define GOALDEF                   25
#define ADLGOAL                   26
  
#endif


static char *errmsg[] = {
  "'define' expected",
  "'problem' expected",
  "problem name expected",
  "'(' expected",
  "')' expected",
  "additional domain definitions expected",
  "requirements (e.g. ':strips') expected",
  "typed list of <%s> expected",
  "domain extension expected",
  "domain to be extented expected",
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
  "'situation' expected",
  "situation name expected",
  "':domain' expected",
  "this problem needs another domain file",
  "initial facts definition expected",
  "goal definition expected",
  "first order logic expression expected",
  NULL
};

//void fcterr( int errno, char *par );
effect_list make_q_goal_list( fact_list pars, fact_list conds, 
			      fact_list goals, int quant );


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


%type <token> problem_name
%type <fact_list> adl_goal_description
%type <fact_list> adl_goal_description_star
%type <fact_list> literal_name_plus
%type <token_list> literal_name
%type <token_list> literal_term
%type <token_list> atomic_formula_term
%type <token_list> term_star
%type <token> term
%type <token_list> name_star
%type <token_list> atomic_formula_name
%type <token> predicate
%type <fact_list> typed_list_name
%type <fact_list> typed_list_variable
%type <token_list> name_plus

%token DEFINE_TOK
%token PROBLEM_TOK
%token SITUATION_TOK
%token BSITUATION_TOK
%token OBJECTS_TOK
%token BDOMAIN_TOK
%token INIT_TOK
%token GOAL_TOK
%token AND_TOK
%token NOT_TOK
%token <string> NAME
%token <string> VARIABLE
%token <string> TYPE
%token EQUAL_TOK
%token FORALL_TOK
%token IMPLY_TOK
%token OR_TOK
%token EXISTS_TOK
%token EITHER_TOK

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
/* empty */
|
problem_definition file
;


/**********************************************************************/
problem_definition : 
'(' DEFINE_TOK         
{ fcterr( PROBNAME_EXPECTED, NULL ); }
problem_name
problem_defs
')'                 
{  
  strcpy(problemName, $4);
  printf("\nproblem '%s' defined\n", $4 ); 
}
;


/**********************************************************************/
problem_name :
'(' PROBLEM_TOK
NAME       
')'        
{ 
  $$ = new_token( strlen($3)+1 );
  strcpy( $$, $3);
}
;


/**********************************************************************/
base_domain_name :
'(' BDOMAIN_TOK 
NAME       
')'
{ 
  if ( strcmp( $3, gdomain_name ) != SAME )
    {
      fcterr( BADDOMAIN, NULL );
      yyerror();
    }
}

/**********************************************************************/
problem_defs:
/* empty */
|
objects_def problem_defs
|
init_def problem_defs
|
goal_def problem_defs
|
base_domain_name problem_defs
;


/**********************************************************************/
objects_def:
'(' OBJECTS_TOK
typed_list_name
')'
{ 
  fact_list f;
  type_tree root;
  type_tree_list ttl;

  if ( orig_constant_list )
    {
      for(f=orig_constant_list; f->next; f=f->next )
	;
      f->next = $3;
    }
  else
    orig_constant_list = $3;
  /* maybe new types are introduced here and must be added to the
     type tree */
  for ( f=orig_constant_list; f; f=f->next )
    {
      root = main_type_tree(); /* do not search the EITHER trees */
      if ( !find_branch( f->item->next->item, root ) )
	{ /* type of this constant is not known yet */
	  ttl = new_type_tree_list( f->item->next->item );
	  ttl->next = root->sub_types;
	  root->sub_types = ttl;
	}
    }
}
;


/**********************************************************************/
init_def:
'(' INIT_TOK
{ fcterr( INIFACTS, NULL ); }
literal_name_plus
')'
{
  fact_list f;
  fact_list last = NULL;

  orig_initial_facts = $4;
  /* assuming a closed world we can ommit negated predicates in
     the initial state -- things not given do not hold anyway */
  for( f = orig_initial_facts; f; f = f->next )
    {
      if ( f->item->item[0] == '!' )
	{
	  if ( last == NULL )
	    {
	      orig_initial_facts = f->next;
	      /* f and its items should be freed now */
	    }
	  else
	    {
	      last->next = f->next;
	      /* f and its items should be freed now */
	    }
	}
      else
	{
	  last = f;
	}
    }
}
;

/**********************************************************************/
goal_def:
'(' GOAL_TOK
{ fcterr( GOALDEF, NULL ); }
adl_goal_description
')'
{
  op_list gop = new_op_list( GOAL_OP_STR );
  
  gop->preconds = $4;
  gop->effects = new_effect_list();
  gop->effects->add_effects = new_fact_list();
  gop->effects->add_effects->item = new_token_list();
  gop->effects->add_effects->item->item = new_token(1+strlen(GOAL_REACHED));
  strcpy( gop->effects->add_effects->item->item, GOAL_REACHED );
  gop->next = loaded_ops;
  loaded_ops = gop;
  /* This is really beautiful and it was very easy compared to the efforts
     made some time ago to have just a fraction of this expressivity */
  goal_facts = new_token_list();
  goal_facts->item = new_token(1+strlen(GOAL_REACHED));
  strcpy( goal_facts->item, GOAL_REACHED );
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

/**********************************************************************/

literal_name_plus:
literal_name
{
  $$ = new_fact_list();
  $$->item = $1;
}
|
literal_name
literal_name_plus
{
   $$ = new_fact_list();
   $$->item = $1;
   $$->next = $2;
}
 
/**********************************************************************/

literal_name:
'(' NOT_TOK
atomic_formula_name
')'
{ 
  $$ = new_token_list();
  $$->item = new_token( strlen($3->item)+2 );
  strcpy( $$->item, "!" );
  strcat( $$->item, $3->item );
  $$->next = $3->next;
}
|
atomic_formula_name
{
  $$ = $1;
}
;

/**********************************************************************/

atomic_formula_name:
'('
predicate 
name_star
')'
{ 
  $$ = new_token_list();
  $$->item = new_token( strlen($2)+1 );
  strcpy( $$->item, $2 );
  $$->next = $3;
}
;

/**********************************************************************/

name_star:
/* empty */
{ $$ = NULL; }
|
NAME
name_star
{
  $$ = new_token_list();
  $$->item = new_token( strlen($1)+1 );
  strcpy( $$->item, $1 );
  $$->next = $2;
}
;


%%

#include "lex.fct.c"

/**********************************************************************
 * Functions
 **********************************************************************/

/* 
call	bison -pfct -bscan-fct scan-fct.y
*/
void fcterr( int errno, char *par )
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


void load_fct_file( char *filename )
{
  FILE *fp;/* pointer to input files */

  /* open fact file */
  if( ( fp = fopen( filename, "r" ) ) == NULL ) {
    printf( "\nipp: can't find fact file: %s\n\n", filename );
    OUTPUT_FILE;
    exit( 1 );
  }
  act_filename = filename;
  lineno = 1; 
  yyin = fp;
  yyparse();
  fclose( fp );/* and close file again */
}

effect_list make_q_goal_list( fact_list pars, fact_list conds, 
			      fact_list goals, int quant )
{
  effect_list result;
  
  result = ( effect_list ) calloc( 1, sizeof( effect_list_elt ) );
  result->quantified_variables = ( fact_list ) calloc( 1, sizeof( fact_list_elt ) );
  result->quantified_variables->item = 
    ( token_list ) calloc( 1, sizeof( token_list_elt ) );
  result->quantified_variables->item->item = ( token ) calloc( 1, sizeof( char ) );
  result->quantified_variables->item->item[0] = QUANTIFIERS[quant];
  result->quantified_variables->next = pars;
  result->conditions = conds;
  result->add_effects = goals;
  result->del_effects = NULL;
  result->next = NULL;
  return result;
}


void print_factlist( fact_list list )
{

  fact_list i_list;
  token_list i_token;

  for ( i_list = list; i_list; i_list = i_list->next ) 
    {
      for ( i_token = i_list->item; i_token; i_token = i_token->next )
	printf( "%s ", i_token->item );
      printf( ".  " );
    }
}

/* prints out facts */
void print_fct( fact_list con_list, token_list ini_list, token_list gol_list )

{

  printf( "\nconstants: " );
  print_factlist( con_list ); 

  printf( "\n\ninitial: " );
  print_tokenlist( ini_list );

  printf( "\n\ngoal: " );
  print_tokenlist( gol_list );

  printf( "\n" );

}

  
void print_tokenlist(token_list list)
{
  token_list i_token;

  for ( i_token = list; i_token; i_token = i_token->next )
    {
      printf( "\n%s ", i_token->item );
      if (!strcmp(i_token->item, ""))
	printf("Match\n");
    }
}

