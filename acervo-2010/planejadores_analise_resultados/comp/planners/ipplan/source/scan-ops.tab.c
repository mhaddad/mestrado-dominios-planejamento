
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.4.1"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1

/* Using locations.  */
#define YYLSP_NEEDED 0

/* Substitute the variable and function names.  */
#define yyparse         opsparse
#define yylex           opslex
#define yyerror         opserror
#define yylval          opslval
#define yychar          opschar
#define yydebug         opsdebug
#define yynerrs         opsnerrs


/* Copy the first part of user declarations.  */

/* Line 189 of yacc.c  */
#line 1 "scan-ops.y"

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



/* Line 189 of yacc.c  */
#line 176 "scan-ops.tab.c"

/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     DEFINE_TOK = 258,
     DOMAIN_TOK = 259,
     REQUIREMENTS_TOK = 260,
     TYPES_TOK = 261,
     EITHER_TOK = 262,
     CONSTANTS_TOK = 263,
     ACTION_TOK = 264,
     AXIOM_TOK = 265,
     VARS_TOK = 266,
     PRECONDITION_TOK = 267,
     PARAMETERS_TOK = 268,
     EFFECT_TOK = 269,
     AND_TOK = 270,
     NOT_TOK = 271,
     WHEN_TOK = 272,
     FORALL_TOK = 273,
     IMPLY_TOK = 274,
     OR_TOK = 275,
     EXISTS_TOK = 276,
     EQUAL_TOK = 277,
     NAME = 278,
     VARIABLE = 279,
     TYPE = 280
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 214 of yacc.c  */
#line 99 "scan-ops.y"

  char string[256];
  token token;
  fact_list fact_list;
  op_list op_list;
  token_list token_list;
  effect_list effect_list;



/* Line 214 of yacc.c  */
#line 248 "scan-ops.tab.c"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif


/* Copy the second part of user declarations.  */


/* Line 264 of yacc.c  */
#line 260 "scan-ops.tab.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int yyi)
#else
static int
YYID (yyi)
    int yyi;
#endif
{
  return yyi;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)				\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack_alloc, Stack, yysize);			\
	Stack = &yyptr->Stack_alloc;					\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  3
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   128

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  28
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  39
/* YYNRULES -- Number of rules.  */
#define YYNRULES  72
/* YYNRULES -- Number of states.  */
#define YYNSTATES  156

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   280

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
      26,    27,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint8 yyprhs[] =
{
       0,     0,     3,     4,     7,     8,    14,    19,    21,    24,
      27,    30,    33,    36,    37,    38,    46,    47,    48,    52,
      53,    59,    60,    66,    67,    68,    77,    78,    83,    84,
      90,    91,    96,    97,   102,   103,   104,   112,   113,   118,
     120,   125,   130,   135,   141,   149,   157,   158,   161,   163,
     168,   176,   182,   183,   186,   191,   193,   198,   199,   202,
     204,   206,   208,   211,   212,   218,   222,   225,   226,   232,
     236,   239,   241
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int8 yyrhs[] =
{
      29,     0,    -1,    -1,    30,    31,    -1,    -1,    26,     3,
      33,    32,    34,    -1,    26,     4,    23,    27,    -1,    27,
      -1,    35,    34,    -1,    42,    34,    -1,    40,    34,    -1,
      51,    34,    -1,    44,    34,    -1,    -1,    -1,    26,     5,
      36,    23,    37,    38,    27,    -1,    -1,    -1,    23,    39,
      38,    -1,    -1,    26,     6,    41,    64,    27,    -1,    -1,
      26,     8,    43,    64,    27,    -1,    -1,    -1,    26,     9,
      45,    23,    46,    47,    48,    27,    -1,    -1,    13,    26,
      65,    27,    -1,    -1,    11,    26,    65,    27,    48,    -1,
      -1,    12,    55,    49,    48,    -1,    -1,    14,    57,    50,
      48,    -1,    -1,    -1,    26,    10,    52,    54,    53,    48,
      27,    -1,    -1,    11,    26,    65,    27,    -1,    59,    -1,
      26,    15,    56,    27,    -1,    26,    20,    56,    27,    -1,
      26,    16,    55,    27,    -1,    26,    19,    55,    55,    27,
      -1,    26,    21,    26,    65,    27,    55,    27,    -1,    26,
      18,    26,    65,    27,    55,    27,    -1,    -1,    55,    56,
      -1,    59,    -1,    26,    15,    58,    27,    -1,    26,    18,
      26,    65,    27,    57,    27,    -1,    26,    17,    55,    57,
      27,    -1,    -1,    57,    58,    -1,    26,    16,    60,    27,
      -1,    60,    -1,    26,    66,    61,    27,    -1,    -1,    62,
      61,    -1,    23,    -1,    24,    -1,    23,    -1,    23,    63,
      -1,    -1,    23,     7,    63,    27,    64,    -1,    23,    25,
      64,    -1,    23,    64,    -1,    -1,    24,     7,    63,    27,
      65,    -1,    24,    25,    65,    -1,    24,    65,    -1,    23,
      -1,    22,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   161,   161,   161,   170,   168,   182,   191,   193,   195,
     197,   199,   201,   208,   210,   207,   221,   225,   224,   238,
     237,   249,   248,   264,   266,   263,   282,   284,   295,   298,
     316,   314,   321,   319,   333,   338,   332,   358,   362,   378,
     384,   397,   410,   423,   442,   464,   489,   493,   514,   534,
     544,   576,   612,   616,   631,   642,   651,   667,   669,   682,
     688,   698,   705,   718,   720,   774,   786,   814,   816,   869,
     881,   908,   914
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "DEFINE_TOK", "DOMAIN_TOK",
  "REQUIREMENTS_TOK", "TYPES_TOK", "EITHER_TOK", "CONSTANTS_TOK",
  "ACTION_TOK", "AXIOM_TOK", "VARS_TOK", "PRECONDITION_TOK",
  "PARAMETERS_TOK", "EFFECT_TOK", "AND_TOK", "NOT_TOK", "WHEN_TOK",
  "FORALL_TOK", "IMPLY_TOK", "OR_TOK", "EXISTS_TOK", "EQUAL_TOK", "NAME",
  "VARIABLE", "TYPE", "'('", "')'", "$accept", "file", "$@1",
  "domain_definition", "$@2", "domain_name", "optional_domain_defs",
  "require_def", "$@3", "$@4", "require_key_star", "$@5", "types_def",
  "$@6", "constants_def", "$@7", "action_def", "$@8", "$@9", "param_def",
  "action_def_body", "$@10", "$@11", "axiom_def", "$@12", "$@13",
  "axiom_vars_def", "adl_goal_description", "adl_goal_description_star",
  "adl_effect", "adl_effect_star", "literal_term", "atomic_formula_term",
  "term_star", "term", "name_plus", "typed_list_name",
  "typed_list_variable", "predicate", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,    40,    41
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    28,    30,    29,    32,    31,    33,    34,    34,    34,
      34,    34,    34,    36,    37,    35,    38,    39,    38,    41,
      40,    43,    42,    45,    46,    44,    47,    47,    48,    48,
      49,    48,    50,    48,    52,    53,    51,    54,    54,    55,
      55,    55,    55,    55,    55,    55,    56,    56,    57,    57,
      57,    57,    58,    58,    59,    59,    60,    61,    61,    62,
      62,    63,    63,    64,    64,    64,    64,    65,    65,    65,
      65,    66,    66
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     0,     2,     0,     5,     4,     1,     2,     2,
       2,     2,     2,     0,     0,     7,     0,     0,     3,     0,
       5,     0,     5,     0,     0,     8,     0,     4,     0,     5,
       0,     4,     0,     4,     0,     0,     7,     0,     4,     1,
       4,     4,     4,     5,     7,     7,     0,     2,     1,     4,
       7,     5,     0,     2,     4,     1,     4,     0,     2,     1,
       1,     1,     2,     0,     5,     3,     2,     0,     5,     3,
       2,     1,     1
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       2,     0,     0,     1,     0,     3,     0,     0,     4,     0,
       0,     0,     0,     7,     5,     0,     0,     0,     0,     0,
       6,    13,    19,    21,    23,    34,     8,    10,     9,    12,
      11,     0,    63,    63,     0,    37,    14,    63,     0,     0,
      24,     0,    35,    16,     0,    63,    66,    20,    22,    26,
      67,    28,    17,     0,    61,     0,    65,     0,    28,    67,
       0,     0,     0,     0,     0,    16,    15,    62,    63,    67,
       0,     0,    67,    70,    38,    67,     0,    30,    39,    55,
       0,    32,    48,    36,    18,    64,     0,    25,     0,    69,
       0,    46,     0,     0,     0,    46,     0,    72,    71,    57,
      28,    52,     0,     0,     0,    28,    27,    67,    28,    46,
       0,     0,     0,    67,     0,     0,    67,    59,    60,     0,
      57,    31,    52,     0,     0,     0,     0,    67,    33,    68,
      29,    47,    40,    42,    54,     0,     0,    41,     0,    56,
      58,    53,    49,     0,     0,     0,    43,     0,    51,     0,
       0,     0,     0,    45,    44,    50
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int8 yydefgoto[] =
{
      -1,     1,     2,     5,    10,     8,    14,    15,    31,    43,
      53,    65,    16,    32,    17,    33,    18,    34,    49,    58,
      64,   100,   105,    19,    35,    51,    42,   109,   110,   122,
     123,    78,    79,   119,   120,    55,    38,    60,    99
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -94
static const yytype_int8 yypact[] =
{
     -94,     9,   -11,   -94,    18,   -94,    -8,    32,   -94,    16,
      23,    20,    35,   -94,   -94,    23,    23,    23,    23,    23,
     -94,   -94,   -94,   -94,   -94,   -94,   -94,   -94,   -94,   -94,
     -94,    28,    37,    37,    39,    56,   -94,     1,    41,    42,
     -94,    53,   -94,    57,    58,    37,   -94,   -94,   -94,    69,
      59,    11,   -94,    62,    58,    68,   -94,    70,    11,     3,
      73,    71,    75,    77,    78,    57,   -94,   -94,    37,    59,
      79,    58,    59,   -94,   -94,    59,    55,   -94,   -94,   -94,
      76,   -94,   -94,   -94,   -94,   -94,    80,   -94,    81,   -94,
      82,    75,    75,    84,    75,    75,    85,   -94,   -94,    31,
      11,    77,    86,    75,    87,    11,   -94,    59,    11,    75,
      88,    89,    90,    59,    75,    91,    59,   -94,   -94,    92,
      31,   -94,    77,    93,    43,    90,    77,    59,   -94,   -94,
     -94,   -94,   -94,   -94,   -94,    94,    95,   -94,    96,   -94,
     -94,   -94,   -94,    97,    98,    75,   -94,    75,   -94,    77,
      99,   100,   101,   -94,   -94,   -94
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int8 yypgoto[] =
{
     -94,   -94,   -94,   -94,   -94,   -94,    15,   -94,   -94,   -94,
      19,   -94,   -94,   -94,   -94,   -94,   -94,   -94,   -94,   -94,
     -52,   -94,   -94,   -94,   -94,   -94,   -94,   -57,   -93,   -62,
     -37,   -63,   -89,   -18,   -94,   -42,   -26,   -55,   -94
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -1
static const yytype_uint8 yytable[] =
{
      82,    81,   115,   112,    73,    77,    70,    39,    44,     3,
      71,    46,    67,   125,    86,     4,   131,    89,     7,    56,
      90,     6,    61,    62,    37,    63,    45,    59,    72,    88,
      26,    27,    28,    29,    30,   111,     9,   114,    82,    11,
      21,    22,    85,    23,    24,    25,   126,    20,   121,    12,
      13,    36,   129,   128,   117,   118,   130,   136,   135,    82,
      37,   138,    40,    82,   143,    97,    98,    41,    47,    48,
      91,    92,   144,    93,    94,    95,    96,    97,    98,    50,
      52,    54,    57,    59,    84,   141,    82,   152,   150,    66,
     151,   101,   102,   103,   104,    68,    69,    75,    97,    98,
      74,    76,   140,    80,     0,    83,    87,   106,   107,   108,
     113,   116,   124,   127,     0,   132,   133,   134,   137,   139,
     142,   145,   146,   147,   148,   149,   153,   154,   155
};

static const yytype_int16 yycheck[] =
{
      63,    63,    95,    92,    59,    62,    58,    33,     7,     0,
       7,    37,    54,   102,    69,    26,   109,    72,    26,    45,
      75,     3,    11,    12,    23,    14,    25,    24,    25,    71,
      15,    16,    17,    18,    19,    92,     4,    94,   101,    23,
       5,     6,    68,     8,     9,    10,   103,    27,   100,    26,
      27,    23,   107,   105,    23,    24,   108,   114,   113,   122,
      23,   116,    23,   126,   126,    22,    23,    11,    27,    27,
      15,    16,   127,    18,    19,    20,    21,    22,    23,    26,
      23,    23,    13,    24,    65,   122,   149,   149,   145,    27,
     147,    15,    16,    17,    18,    27,    26,    26,    22,    23,
      27,    26,   120,    26,    -1,    27,    27,    27,    27,    27,
      26,    26,    26,    26,    -1,    27,    27,    27,    27,    27,
      27,    27,    27,    27,    27,    27,    27,    27,    27
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    29,    30,     0,    26,    31,     3,    26,    33,     4,
      32,    23,    26,    27,    34,    35,    40,    42,    44,    51,
      27,     5,     6,     8,     9,    10,    34,    34,    34,    34,
      34,    36,    41,    43,    45,    52,    23,    23,    64,    64,
      23,    11,    54,    37,     7,    25,    64,    27,    27,    46,
      26,    53,    23,    38,    23,    63,    64,    13,    47,    24,
      65,    11,    12,    14,    48,    39,    27,    63,    27,    26,
      48,     7,    25,    65,    27,    26,    26,    55,    59,    60,
      26,    57,    59,    27,    38,    64,    65,    27,    63,    65,
      65,    15,    16,    18,    19,    20,    21,    22,    23,    66,
      49,    15,    16,    17,    18,    50,    27,    27,    27,    55,
      56,    55,    60,    26,    55,    56,    26,    23,    24,    61,
      62,    48,    57,    58,    26,    60,    55,    26,    48,    65,
      48,    56,    27,    27,    27,    65,    55,    27,    65,    27,
      61,    58,    27,    57,    65,    27,    27,    27,    27,    27,
      55,    55,    57,    27,    27,    27
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yyerrlab

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      yytoken = YYTRANSLATE (yychar);				\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
#else
static void
yy_stack_print (yybottom, yytop)
    yytype_int16 *yybottom;
    yytype_int16 *yytop;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif



#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yysyntax_error (char *yyresult, int yystate, int yychar)
{
  int yyn = yypact[yystate];

  if (! (YYPACT_NINF < yyn && yyn <= YYLAST))
    return 0;
  else
    {
      int yytype = YYTRANSLATE (yychar);
      YYSIZE_T yysize0 = yytnamerr (0, yytname[yytype]);
      YYSIZE_T yysize = yysize0;
      YYSIZE_T yysize1;
      int yysize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yyx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yyfmt;
      char const *yyf;
      static char const yyunexpected[] = "syntax error, unexpected %s";
      static char const yyexpecting[] = ", expecting %s";
      static char const yyor[] = " or %s";
      char yyformat[sizeof yyunexpected
		    + sizeof yyexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yyor - 1))];
      char const *yyprefix = yyexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;

      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yycount = 1;

      yyarg[0] = yytname[yytype];
      yyfmt = yystpcpy (yyformat, yyunexpected);

      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
	if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR)
	  {
	    if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yycount = 1;
		yysize = yysize0;
		yyformat[sizeof yyunexpected - 1] = '\0';
		break;
	      }
	    yyarg[yycount++] = yytname[yyx];
	    yysize1 = yysize + yytnamerr (0, yytname[yyx]);
	    yysize_overflow |= (yysize1 < yysize);
	    yysize = yysize1;
	    yyfmt = yystpcpy (yyfmt, yyprefix);
	    yyprefix = yyor;
	  }

      yyf = YY_(yyformat);
      yysize1 = yysize + yystrlen (yyf);
      yysize_overflow |= (yysize1 < yysize);
      yysize = yysize1;

      if (yysize_overflow)
	return YYSIZE_MAXIMUM;

      if (yyresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yyp = yyresult;
	  int yyi = 0;
	  while ((*yyp = *yyf) != '\0')
	    {
	      if (*yyp == '%' && yyf[1] == 's' && yyi < yycount)
		{
		  yyp += yytnamerr (yyp, yyarg[yyi++]);
		  yyf += 2;
		}
	      else
		{
		  yyp++;
		  yyf++;
		}
	    }
	}
      return yysize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}

/* Prevent warnings from -Wmissing-prototypes.  */
#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */


/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;



/*-------------------------.
| yyparse or yypush_parse.  |
`-------------------------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{


    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       `yyss': related to states.
       `yyvs': related to semantic values.

       Refer to the stacks thru separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yytoken = 0;
  yyss = yyssa;
  yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */
  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;

	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),
		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss_alloc, yyss);
	YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yyn == YYPACT_NINF)
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yyn == 0 || yyn == YYTABLE_NINF)
	goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:

/* Line 1455 of yacc.c  */
#line 161 "scan-ops.y"
    { opserr( DOMDEF_EXPECTED, NULL ); ;}
    break;

  case 4:

/* Line 1455 of yacc.c  */
#line 170 "scan-ops.y"
    { 
  /* initialize typetree */
  global_type_tree_list = new_type_tree_list( STANDARD_TYPE );
;}
    break;

  case 5:

/* Line 1455 of yacc.c  */
#line 175 "scan-ops.y"
    {
  printf("\ndomain '%s' defined\n", gdomain_name );
;}
    break;

  case 6:

/* Line 1455 of yacc.c  */
#line 183 "scan-ops.y"
    { 
  gdomain_name = new_token( strlen((yyvsp[(3) - (4)].string))+1 );
  strcpy( gdomain_name, (yyvsp[(3) - (4)].string));
;}
    break;

  case 13:

/* Line 1455 of yacc.c  */
#line 208 "scan-ops.y"
    { opserr( REQUIREM_EXPECTED, NULL ); ;}
    break;

  case 14:

/* Line 1455 of yacc.c  */
#line 210 "scan-ops.y"
    { 
  if ( !supported( (yyvsp[(4) - (4)].string) ) )
    {
      opserr( NOT_SUPPORTED, (yyvsp[(4) - (4)].string) );
      yyerror();
    }
;}
    break;

  case 17:

/* Line 1455 of yacc.c  */
#line 225 "scan-ops.y"
    { 
  if ( !supported( (yyvsp[(1) - (1)].string) ) )
    {
      opserr( NOT_SUPPORTED, (yyvsp[(1) - (1)].string) );
      yyerror();
    }
;}
    break;

  case 19:

/* Line 1455 of yacc.c  */
#line 238 "scan-ops.y"
    { opserr( TYPEDEF_EXPECTED, NULL ); ;}
    break;

  case 20:

/* Line 1455 of yacc.c  */
#line 241 "scan-ops.y"
    { 
  add_to_type_tree( (yyvsp[(4) - (5)].fact_list), main_type_tree() ); 
;}
    break;

  case 21:

/* Line 1455 of yacc.c  */
#line 249 "scan-ops.y"
    { opserr( CONSTLIST_EXPECTED, NULL ); ;}
    break;

  case 22:

/* Line 1455 of yacc.c  */
#line 252 "scan-ops.y"
    { 
  orig_constant_list = (yyvsp[(4) - (5)].fact_list);
;}
    break;

  case 23:

/* Line 1455 of yacc.c  */
#line 264 "scan-ops.y"
    { opserr( ACTION, NULL ); ;}
    break;

  case 24:

/* Line 1455 of yacc.c  */
#line 266 "scan-ops.y"
    { 
  cur_op = new_op_list( (yyvsp[(4) - (4)].string) );
;}
    break;

  case 25:

/* Line 1455 of yacc.c  */
#line 272 "scan-ops.y"
    {
  cur_op->next = loaded_ops;
  loaded_ops = cur_op; 
;}
    break;

  case 26:

/* Line 1455 of yacc.c  */
#line 282 "scan-ops.y"
    { cur_op->params = NULL; ;}
    break;

  case 27:

/* Line 1455 of yacc.c  */
#line 285 "scan-ops.y"
    {
  fact_list f;
  cur_op->params = (yyvsp[(3) - (4)].fact_list);
  for( f=cur_op->params; f; f = f->next )
    cur_op->number_of_real_params++; /* to be able to distinguish
					params from :VARS */
;}
    break;

  case 29:

/* Line 1455 of yacc.c  */
#line 299 "scan-ops.y"
    {
  fact_list f;
  token t;
  /* add vars as parameters */
  if ( cur_op->params )
    {
      for( f = cur_op->params; f->next; f = f->next )
	;
      f->next = (yyvsp[(3) - (5)].fact_list);
      f = f->next;
    }
  else
    f = (yyvsp[(3) - (5)].fact_list);
;}
    break;

  case 30:

/* Line 1455 of yacc.c  */
#line 316 "scan-ops.y"
    { cur_op->preconds = (yyvsp[(2) - (2)].fact_list); ;}
    break;

  case 32:

/* Line 1455 of yacc.c  */
#line 321 "scan-ops.y"
    { cur_op->effects = (yyvsp[(2) - (2)].effect_list); ;}
    break;

  case 34:

/* Line 1455 of yacc.c  */
#line 333 "scan-ops.y"
    { 
  cur_op = new_axiom_op_list(); /* returns new operator the name of which
				   is AXIOM plus a number */
;}
    break;

  case 35:

/* Line 1455 of yacc.c  */
#line 338 "scan-ops.y"
    {
  cur_op->params = (yyvsp[(4) - (4)].fact_list);
;}
    break;

  case 36:

/* Line 1455 of yacc.c  */
#line 343 "scan-ops.y"
    {
  /* Allowing complete "effects" is more than UCPOP and PDDL do,
     but this can easily be checked: the effect must be a single
     literal, otherwise axiom effects may become a little complicated */
  cur_op->next = loaded_axioms;
  loaded_axioms = cur_op;
  /* save axioms separately for now, after preprocessing they may
     be added to the other operators */
;}
    break;

  case 37:

/* Line 1455 of yacc.c  */
#line 358 "scan-ops.y"
    { 
  (yyval.fact_list) = NULL; 
;}
    break;

  case 38:

/* Line 1455 of yacc.c  */
#line 366 "scan-ops.y"
    {
  (yyval.fact_list) = (yyvsp[(3) - (4)].fact_list);
;}
    break;

  case 39:

/* Line 1455 of yacc.c  */
#line 379 "scan-ops.y"
    { 
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = (yyvsp[(1) - (1)].token_list);
;}
    break;

  case 40:

/* Line 1455 of yacc.c  */
#line 387 "scan-ops.y"
    { 
  fact_list f;
  
  (yyval.fact_list) = make_adl_fact( AND_CONST );
  (yyval.fact_list)->next = (yyvsp[(3) - (4)].fact_list); 
  for ( f=(yyval.fact_list); f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
;}
    break;

  case 41:

/* Line 1455 of yacc.c  */
#line 400 "scan-ops.y"
    { 
  fact_list f;
  
  (yyval.fact_list) = make_adl_fact( OR_CONST );
  (yyval.fact_list)->next = (yyvsp[(3) - (4)].fact_list); 
  for ( f=(yyval.fact_list); f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
;}
    break;

  case 42:

/* Line 1455 of yacc.c  */
#line 413 "scan-ops.y"
    { 
  fact_list f;
  
  (yyval.fact_list) = make_adl_fact( NOT_CONST );
  (yyval.fact_list)->next = (yyvsp[(3) - (4)].fact_list); 
  for ( f=(yyval.fact_list); f->next; f=f->next )
    ;
  f->next = make_adl_fact( ENDNOT_CONST );
;}
    break;

  case 43:

/* Line 1455 of yacc.c  */
#line 427 "scan-ops.y"
    { 
  fact_list f;
  
  (yyval.fact_list) = make_adl_fact( OR_CONST );
  (yyval.fact_list)->next = make_adl_fact( NOT_CONST );
  (yyval.fact_list)->next->next = (yyvsp[(3) - (5)].fact_list); 
  for ( f=(yyval.fact_list); f->next; f=f->next )
    ;
  f->next = make_adl_fact( ENDNOT_CONST);
  f->next->next = (yyvsp[(4) - (5)].fact_list);
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
;}
    break;

  case 44:

/* Line 1455 of yacc.c  */
#line 448 "scan-ops.y"
    { 
  fact_list f;
  
  (yyval.fact_list) = f = make_adl_fact( EXISTS_CONST );
  f->next = make_adl_fact( LBRACK_CONST );
  f->next->next = (yyvsp[(4) - (7)].fact_list); 
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
  f = f->next;
  f->next = (yyvsp[(6) - (7)].fact_list);
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
;}
    break;

  case 45:

/* Line 1455 of yacc.c  */
#line 470 "scan-ops.y"
    { 
  fact_list f;
  
  (yyval.fact_list) = f = make_adl_fact( FORALL_CONST );
  f->next = make_adl_fact( LBRACK_CONST );
  f->next->next = (yyvsp[(4) - (7)].fact_list); 
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
  f = f->next;
  f->next = (yyvsp[(6) - (7)].fact_list);
  for ( ; f->next; f=f->next )
    ;
  f->next = make_adl_fact( RBRACK_CONST );
;}
    break;

  case 46:

/* Line 1455 of yacc.c  */
#line 489 "scan-ops.y"
    {
  (yyval.fact_list) = NULL;
;}
    break;

  case 47:

/* Line 1455 of yacc.c  */
#line 494 "scan-ops.y"
    {
  fact_list f;

  (yyval.fact_list) = (yyvsp[(1) - (2)].fact_list);
  if ( !(yyval.fact_list) )
    (yyval.fact_list) = (yyvsp[(2) - (2)].fact_list);
  else
    {
      for ( f = (yyval.fact_list); f->next; f = f->next )
	;
      f->next = (yyvsp[(2) - (2)].fact_list);
    }
;}
    break;

  case 48:

/* Line 1455 of yacc.c  */
#line 515 "scan-ops.y"
    {
  (yyval.effect_list) = new_effect_list();
  if ( ((yyvsp[(1) - (1)].token_list)->item)[0] == '!' ) 
    {
      token_list tl;
      token t = new_token( strlen((yyvsp[(1) - (1)].token_list)->item)+1-1 );
      strcpy( t, ((yyvsp[(1) - (1)].token_list)->item)+1 );
      (yyval.effect_list)->del_effects = new_fact_list();
      (yyval.effect_list)->del_effects->item = new_token_list();
      (yyval.effect_list)->del_effects->item->item = t;
      (yyval.effect_list)->del_effects->item->next = (yyvsp[(1) - (1)].token_list)->next;
    }
  else
    {
      (yyval.effect_list)->add_effects = new_fact_list();
      (yyval.effect_list)->add_effects->item = (yyvsp[(1) - (1)].token_list);
    }
;}
    break;

  case 49:

/* Line 1455 of yacc.c  */
#line 537 "scan-ops.y"
    {
  /* check if effects are just literals i.e. atomic or negated
     atomic formula. If so, merge the effects */
  fflush( stdout );
  (yyval.effect_list) = merge_literal_effects( (yyvsp[(3) - (4)].effect_list) );
;}
    break;

  case 50:

/* Line 1455 of yacc.c  */
#line 550 "scan-ops.y"
    {
  /* $3 are parameters in all effects described in $5, so just bring
     the variables into the effects */
  effect_list cur_eff;
  fact_list par, end;

  (yyval.effect_list) = (yyvsp[(6) - (7)].effect_list);
  for ( cur_eff=(yyval.effect_list); cur_eff; cur_eff=cur_eff->next )
    { /* for each effect already specified... */
      par=cur_eff->quantified_variables;
      if ( par )
	{
	  /* ...find all parameters specified yet... */
	  for ( ; par->next; par=par->next )
	    ;
	  /* ...and append new parameters. */
	  par->next = copy_complete_fact_list( (yyvsp[(4) - (7)].fact_list), &end );
	}
      else
	{
	  /* ... or, if no other parameters, just copy the new ones */
	  cur_eff->quantified_variables = copy_complete_fact_list( (yyvsp[(4) - (7)].fact_list), &end );
	}
    }
;}
    break;

  case 51:

/* Line 1455 of yacc.c  */
#line 580 "scan-ops.y"
    {
  /* $3 is a condition for all elements of $4, so just bring the
     condition into the effects */
  effect_list cur_eff;
  fact_list cond, end;

  for ( (yyval.effect_list)=cur_eff=(yyvsp[(4) - (5)].effect_list); cur_eff; cur_eff=cur_eff->next )
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
	  cond->next = copy_complete_fact_list( (yyvsp[(3) - (5)].fact_list), &end );
	  for ( ; cond->next; cond=cond->next )
	    ;
	  cond->next = make_adl_fact( RBRACK_CONST );
	}
      else
	{
	  /* ... or, if no other conditions, just copy the new ones */
	  cur_eff->conditions = copy_complete_fact_list( (yyvsp[(3) - (5)].fact_list), &end );
	}
    }
;}
    break;

  case 52:

/* Line 1455 of yacc.c  */
#line 612 "scan-ops.y"
    { 
  (yyval.effect_list) = NULL; 
;}
    break;

  case 53:

/* Line 1455 of yacc.c  */
#line 618 "scan-ops.y"
    {
  (yyval.effect_list) = (yyvsp[(1) - (2)].effect_list);
  (yyval.effect_list)->next = (yyvsp[(2) - (2)].effect_list);
;}
    break;

  case 54:

/* Line 1455 of yacc.c  */
#line 634 "scan-ops.y"
    { 
  (yyval.token_list) = new_token_list();
  (yyval.token_list)->item = new_token( strlen((yyvsp[(3) - (4)].token_list)->item)+2 );
  strcpy( (yyval.token_list)->item, "!" );
  strcat( (yyval.token_list)->item, (yyvsp[(3) - (4)].token_list)->item );
  (yyval.token_list)->next = (yyvsp[(3) - (4)].token_list)->next;
;}
    break;

  case 55:

/* Line 1455 of yacc.c  */
#line 643 "scan-ops.y"
    {
  (yyval.token_list) = (yyvsp[(1) - (1)].token_list);
;}
    break;

  case 56:

/* Line 1455 of yacc.c  */
#line 655 "scan-ops.y"
    { 
  (yyval.token_list) = new_token_list();
  (yyval.token_list)->item = new_token( strlen((yyvsp[(2) - (4)].token))+1 );
  strcpy( (yyval.token_list)->item, (yyvsp[(2) - (4)].token) );
  (yyval.token_list)->next = (yyvsp[(3) - (4)].token_list);
;}
    break;

  case 57:

/* Line 1455 of yacc.c  */
#line 667 "scan-ops.y"
    { (yyval.token_list) = NULL; ;}
    break;

  case 58:

/* Line 1455 of yacc.c  */
#line 671 "scan-ops.y"
    {
  (yyval.token_list) = new_token_list();
  (yyval.token_list)->item = new_token( strlen((yyvsp[(1) - (2)].token))+1 );
  strcpy( (yyval.token_list)->item, (yyvsp[(1) - (2)].token) );
  (yyval.token_list)->next = (yyvsp[(2) - (2)].token_list);
;}
    break;

  case 59:

/* Line 1455 of yacc.c  */
#line 683 "scan-ops.y"
    { 
  (yyval.token) = new_token( strlen((yyvsp[(1) - (1)].string))+1 );
  strcpy( (yyval.token), (yyvsp[(1) - (1)].string) );
;}
    break;

  case 60:

/* Line 1455 of yacc.c  */
#line 689 "scan-ops.y"
    { 
  (yyval.token) = new_token( strlen((yyvsp[(1) - (1)].string))+1 );
  strcpy( (yyval.token), (yyvsp[(1) - (1)].string) );
;}
    break;

  case 61:

/* Line 1455 of yacc.c  */
#line 699 "scan-ops.y"
    {
  (yyval.token_list) = new_token_list();
  (yyval.token_list)->item = new_token( strlen((yyvsp[(1) - (1)].string))+1 );
  strcpy( (yyval.token_list)->item, (yyvsp[(1) - (1)].string) );
;}
    break;

  case 62:

/* Line 1455 of yacc.c  */
#line 706 "scan-ops.y"
    {
  (yyval.token_list) = new_token_list();
  (yyval.token_list)->item = new_token( strlen((yyvsp[(1) - (2)].string))+1 );
  strcpy( (yyval.token_list)->item, (yyvsp[(1) - (2)].string) );
  (yyval.token_list)->next = (yyvsp[(2) - (2)].token_list);
;}
    break;

  case 63:

/* Line 1455 of yacc.c  */
#line 718 "scan-ops.y"
    { (yyval.fact_list) = NULL; ;}
    break;

  case 64:

/* Line 1455 of yacc.c  */
#line 721 "scan-ops.y"
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
  for ( t = (yyvsp[(3) - (5)].token_list); t; t = t->next )
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
      for ( t = (yyvsp[(3) - (5)].token_list); t; t = t->next )
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
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = new_token_list();
  (yyval.fact_list)->item->item = new_token( strlen((yyvsp[(1) - (5)].string))+1 );
  strcpy( (yyval.fact_list)->item->item, (yyvsp[(1) - (5)].string) );
  (yyval.fact_list)->item->next = new_token_list();
  (yyval.fact_list)->item->next->item = s;
  (yyval.fact_list)->next = (yyvsp[(5) - (5)].fact_list);
;}
    break;

  case 65:

/* Line 1455 of yacc.c  */
#line 775 "scan-ops.y"
    {
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = new_token_list();
  (yyval.fact_list)->item->item = new_token( strlen((yyvsp[(1) - (3)].string))+1 );
  strcpy( (yyval.fact_list)->item->item, (yyvsp[(1) - (3)].string) );
  (yyval.fact_list)->item->next = new_token_list();
  (yyval.fact_list)->item->next->item = new_token( strlen((yyvsp[(2) - (3)].string))+1 );
  strcpy( (yyval.fact_list)->item->next->item, (yyvsp[(2) - (3)].string) );
  (yyval.fact_list)->next = (yyvsp[(3) - (3)].fact_list);
;}
    break;

  case 66:

/* Line 1455 of yacc.c  */
#line 787 "scan-ops.y"
    {
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = new_token_list();
  (yyval.fact_list)->item->item = new_token( strlen((yyvsp[(1) - (2)].string))+1 );
  strcpy( (yyval.fact_list)->item->item, (yyvsp[(1) - (2)].string) );
  (yyval.fact_list)->item->next = new_token_list();
  if ( (yyvsp[(2) - (2)].fact_list) )   /* another element (already typed) is following */
    {
      char* s = (yyvsp[(2) - (2)].fact_list)->item->next->item;
      int   l = strlen( s ) + 1;
      (yyval.fact_list)->item->next->item = new_token( l );
      strcpy( (yyval.fact_list)->item->next->item, s ); /* same type as the next one */
      (yyval.fact_list)->next = (yyvsp[(2) - (2)].fact_list);
    }
  else /* no further element - it must be an untyped list */
    {
      (yyval.fact_list)->item->next->item = new_token( strlen(STANDARD_TYPE)+1 );
      strcpy( (yyval.fact_list)->item->next->item, STANDARD_TYPE );
      (yyval.fact_list)->next = (yyvsp[(2) - (2)].fact_list);
    }
;}
    break;

  case 67:

/* Line 1455 of yacc.c  */
#line 814 "scan-ops.y"
    { (yyval.fact_list) = NULL; ;}
    break;

  case 68:

/* Line 1455 of yacc.c  */
#line 817 "scan-ops.y"
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
  for ( t = (yyvsp[(3) - (5)].token_list); t; t = t->next )
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
      for ( t = (yyvsp[(3) - (5)].token_list); t; t = t->next )
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
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = new_token_list();
  (yyval.fact_list)->item->item = new_token( strlen((yyvsp[(1) - (5)].string))+1 );
  strcpy( (yyval.fact_list)->item->item, (yyvsp[(1) - (5)].string) );
  (yyval.fact_list)->item->next = new_token_list();
  (yyval.fact_list)->item->next->item = s;
  (yyval.fact_list)->next = (yyvsp[(5) - (5)].fact_list);
;}
    break;

  case 69:

/* Line 1455 of yacc.c  */
#line 870 "scan-ops.y"
    {
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = new_token_list();
  (yyval.fact_list)->item->item = new_token( strlen((yyvsp[(1) - (3)].string))+1 );
  strcpy( (yyval.fact_list)->item->item, (yyvsp[(1) - (3)].string) );
  (yyval.fact_list)->item->next = new_token_list();
  (yyval.fact_list)->item->next->item = new_token( strlen((yyvsp[(2) - (3)].string))+1 );
  strcpy( (yyval.fact_list)->item->next->item, (yyvsp[(2) - (3)].string) );
  (yyval.fact_list)->next = (yyvsp[(3) - (3)].fact_list);
;}
    break;

  case 70:

/* Line 1455 of yacc.c  */
#line 882 "scan-ops.y"
    {
  (yyval.fact_list) = new_fact_list();
  (yyval.fact_list)->item = new_token_list();
  (yyval.fact_list)->item->item = new_token( strlen((yyvsp[(1) - (2)].string))+1 );
  strcpy( (yyval.fact_list)->item->item, (yyvsp[(1) - (2)].string) );
  (yyval.fact_list)->item->next = new_token_list();
  if ( (yyvsp[(2) - (2)].fact_list) )   /* another element (already typed) is following */
    {
      char* s = (yyvsp[(2) - (2)].fact_list)->item->next->item;
      int   l = strlen( s );
      (yyval.fact_list)->item->next->item = new_token( l+1 );
      strcpy( (yyval.fact_list)->item->next->item, s ); /* same type as the next one */
      (yyval.fact_list)->next = (yyvsp[(2) - (2)].fact_list);
    }
  else /* no further element - it must be an untyped list */
    {
      (yyval.fact_list)->item->next->item = new_token( strlen(STANDARD_TYPE)+1 );
      strcpy( (yyval.fact_list)->item->next->item, STANDARD_TYPE );
      (yyval.fact_list)->next = (yyvsp[(2) - (2)].fact_list);
    }
;}
    break;

  case 71:

/* Line 1455 of yacc.c  */
#line 909 "scan-ops.y"
    { 
  (yyval.token) = new_token( strlen((yyvsp[(1) - (1)].string))+1 );
  strcpy( (yyval.token), (yyvsp[(1) - (1)].string) );
;}
    break;

  case 72:

/* Line 1455 of yacc.c  */
#line 915 "scan-ops.y"
    { 
  (yyval.token) = new_token( strlen(EQ_STR)+1 );
  strcpy( (yyval.token), EQ_STR );
;}
    break;



/* Line 1455 of yacc.c  */
#line 2411 "scan-ops.tab.c"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
      {
	YYSIZE_T yysize = yysyntax_error (0, yystate, yychar);
	if (yymsg_alloc < yysize && yymsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yyalloc = 2 * yysize;
	    if (! (yysize <= yyalloc && yyalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yyalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yymsg != yymsgbuf)
	      YYSTACK_FREE (yymsg);
	    yymsg = (char *) YYSTACK_ALLOC (yyalloc);
	    if (yymsg)
	      yymsg_alloc = yyalloc;
	    else
	      {
		yymsg = yymsgbuf;
		yymsg_alloc = sizeof yymsgbuf;
	      }
	  }

	if (0 < yysize && yysize <= yymsg_alloc)
	  {
	    (void) yysyntax_error (yymsg, yystate, yychar);
	    yyerror (yymsg);
	  }
	else
	  {
	    yyerror (YY_("syntax error"));
	    if (yysize != 0)
	      goto yyexhaustedlab;
	  }
      }
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (yyn != YYPACT_NINF)
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined(yyoverflow) || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
     yydestruct ("Cleanup: discarding lookahead",
		 yytoken, &yylval);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}



/* Line 1675 of yacc.c  */
#line 924 "scan-ops.y"


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

