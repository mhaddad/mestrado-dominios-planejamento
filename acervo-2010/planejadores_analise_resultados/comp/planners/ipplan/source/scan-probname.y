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

//void probnameerr( int errno, char *par );
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
problem_definition 
;


/**********************************************************************/
problem_definition : 
'(' DEFINE_TOK         
{ fcterr( PROBNAME_EXPECTED, NULL ); }
problem_name
{  
  strcpy(problemName, $4);
  printf("\nproblem '%s' defined\n", $4 ); 
}
;


/**********************************************************************/
problem_name :
'(' PROBLEM_TOK
NAME               
{ 
  $$ = new_token( strlen($3)+1 );
  strcpy( $$, $3);
}
;



%%

#include "lex.probname.c"

/**********************************************************************
 * Functions
 **********************************************************************/


void probnameerr( int errno, char *par )
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


void get_fct_file_name( char *filename )
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

