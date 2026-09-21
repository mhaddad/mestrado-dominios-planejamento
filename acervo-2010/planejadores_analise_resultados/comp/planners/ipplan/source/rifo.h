/* (C) Copyright 1997 Albert Ludwigs University Freiburg
 *     Institute of Computer Science
 *
 * All rights reserved. Use of this software is permitted for 
 * non-commercial research purposes, and it may be copied only 
 * for that use.  All copies must include this copyright message.
 * This software is made available AS IS, and neither the authors
 * nor the  Albert Ludwigs University Freiburg make any warranty
 * about the software or its performance. 
 */
/* 


 **************************************************************
 * RIFO - Remove Irrelevants in Plan Generation                *
 **************************************************************
 */

#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>
#include<strings.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/resource.h>

#include "ipp.h"

/*** limits ***/

#define rifo_HSIZE 200
#define MAXSTRLEN 256
#define MAXSETSIZE 1024
#define SETARSIZE 8*4   /* SETARSIZE = MAXSETSIZE div sizeof(long):  */


/*** defines ***/

/* #define UNDEFELEMENT (MAXSETSIZE-1) */
#define NOELEMENT (-1) 
#define SAME 0
#define ONE_LINE 1

/*** macros ***/

#define MAX(x,y) ((x) > (y) ? (x) : (y))
#define MIN(x,y) ((x) > (y) ? (y) : (x))
#define equal_tokens(x,y) (!strcmp((x),(y))) 


/*** structures used ***/

/* If a bit b in members[i] is set, element no. 32*i+b is in the set */
typedef struct SETTYPE 
{
  int memcount;
  unsigned long members[SETARSIZE];
} settype, *settype_t;

/* used to store sets of sets */
typedef struct SETLIST 
{
  settype_t item;
  struct SETLIST *next;
} set_elt, *set_list;

/* hashtable to store info (e.g. possibility sets) on operators and facts */
typedef struct rifo_HASHENTRY
{
  char *key;
  int lastdepth;
  int hashval;
  int memcode;
  set_list used_facts;  
  token factnode;
  operator_list opnode;
  struct rifo_HASHENTRY *next;
} rifo_hashentry, *rifo_hashentry_t;
  
typedef rifo_hashentry_t rifo_hashtable_t[rifo_HSIZE];


/**** extern variables: *****/ 
extern int rifo_display_info; /* 0: RIFO turned off, 
				>0: how much information about RIFO is printed out */
extern int mindepth, maxdepth; /* for iterative depth-first search */
extern int setlistthres; /* max no. of elements in one set */
extern int unionstrategy; /* how to get one set out of a set of sets */
extern int oplevel, factlevel; /* describe the different heuristics */
extern rifo_hashtable_t rel_fct_table, rel_op_table;  /* relevant facts and operators */
extern token_list constant_tl; /* to store all typed objects */
extern long memused;
extern long memmaxused;
extern long nodes_visited;
extern rifo_hashtable_t objects_table; /* quickly find type of a given object */
/* first and second part of relevant initial facts */
extern settype *primary_fact_set;
extern settype *secondary_fact_set; 
/* store loaded operators when running RIFO */
extern operator_list save_operators; 
extern token_list save_initial_facts; 


 
/* prototypes */

/***** prototypes: rifoutils.c *****/
void FREE(int size, void *ptr); 
void * MALLOC(int size);
void * CALLOC(int size1, int size2);
void fatal_error(char *str);
int equal_facts(token_list f1, token_list f2);
int really_is_var(char *str);
token_list token_list_from_token( token str );
token_list merge_token_lists( token_list tok1, token_list tok2 );
int token_list_length(token_list tl);
int fact_list_length(fact_list fl);
int op_list_length( operator_list fl);
void free_token_list(token_list tl);
int string_in_list(char *str, token_list tl);
void print_one_set(settype *set, char *prefix, int donewline);
void print_set_list(set_list sl, char *prefix);
void print_token_list( token_list list, int oneline );
void save_original_ipp_information();
void reset_original_ipp_information();

/***** prototypes: rifohash.c */
rifo_hashentry_t rifo_lookup_from_table(rifo_hashtable_t htable, token key);
rifo_hashentry_t rifo_insert_token(rifo_hashtable_t htable, token t );
rifo_hashentry_t rifo_insert_into_table(rifo_hashtable_t htable, token key);
rifo_hashentry_t rifo_get_next(rifo_hashtable_t h, int flag);

/***** prototypes: sets.c */
settype * make_set(int member);
settype * set_copy(settype *result, settype *set);
settype * set_union(settype *result, settype *set1, settype *set2, 
		    int docount);
settype * set_union_list(set_list sl, int maxsets);
settype * set_intersection(settype *result, settype *set1, settype *set2, 
			   int docount);
settype * set_insert_el(settype *result, int member);
int set_member(int member, settype *set);
int set_empty_list( set_list sl );
int set_subseteq(settype *set1, settype *set2);
int set_list_length(set_list sl);
set_list make_set_list(int member);
set_list set_copy_list(set_list list);
set_list set_multiply_lists(set_list s1, set_list s2);
void set_merge_into_list(set_list *sl, int *length, settype *newset, 
			 int newmem);
set_list set_merge_lists(set_list s1, set_list s2);
void set_free_list(set_list list);

/***** prototypes: fbackchain.c */
BOOLEAN find_relevant_initial_facts( BOOLEAN really_run );

