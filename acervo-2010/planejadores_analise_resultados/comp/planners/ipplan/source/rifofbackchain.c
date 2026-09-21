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


/* Backchain on a conjunction of literals and determine
   the ground facts from the initial state that are used.
   
   Usual circle:   fbackchain_goals()   -->    fbackchain_one_goal()
                           ^                         |
                           |                         v
		   cond_fbackchain_ops  <--    fbackchain_ops()

*/



#include "ipp.h"
#include "rifo.h"

int curdepth; /* global var, current depth of backchaining search */
token_list the_objs; /* list of used objects */

int backchain_on_ini = 1; /* backchain on initial facts */

settype* empty_set; /* a kind of constant which is initialised in
		     find_relevant_initial_facts() */

/* prototypes */
set_list fbackchain_goals( int depth, token_list goals, 
			   token_list constants_used );
set_list fbackchain_ops( int depth, token goal );
void clear_tables( void );
void init_tables( void );
token_list rec_select_facts( token_list facts, 
			     settype *in_set, settype *but_not_in_set );



/* used to print out current search depth  */
static void pprefix( int count )
{
  register int i;
  for ( i=0; i<count; i++ ) printf( " " );
  printf( "{%d}",count );
}



/* some functions initializing the data structures */ 


/* clear fact and op table */
void clear_tables( void )
{
  int i;
  rifo_hashentry_t h, temp;

  if ( rifo_display_info >= 5 ) 
    {
      printf( ">> Clearing tables ...\n" );
    }
  for ( i=0;i<HSIZE;i++ ) 
    {
      h = rel_fct_table[i];
      while ( h ) 
	{
	  temp = h->next;
	  FREE( strlen( h->key )+1,h->key );
	  set_free_list( h->used_facts );
	  FREE( sizeof( rifo_hashentry ),h );
	  h = temp;
	}
      rel_fct_table[i] = NULL;
      h = rel_op_table[i];
      while ( h ) 
	{
	  temp = h->next;
	  FREE( strlen( h->key )+1,h->key );
	  FREE( sizeof( rifo_hashentry ),h );
	  h = temp;
	}
      rel_op_table[i] = NULL;
    }
}



void init_op_table( rifo_hashtable_t objtable )
{
  register int i;
  for ( i=0; i<rifo_HSIZE; i++ ) 
    objtable[i] = NULL;
}



/* build up hashtable objects_table for fast access to objects and 
   their types */
token_list init_objs_from_types()
{
  fact_list act_obj_fl;
  token_list act_obj_tl;
  token_list copy_tl;
  rifo_hashentry_t h;
  int elcnt = 0;  

  copy_tl = token_list_from_fact_list( orig_constant_list );
  if ( rifo_display_info >= 5 ) 
    printf( "> Initializing object table from types...\n" );
  /* copying original objects */
  act_obj_tl = copy_tl;
  act_obj_fl = orig_constant_list;

  init_op_table( objects_table );
  while ( act_obj_fl ) 
    { /* insert type declaration into objects_table if not yet in it */
      h = rifo_insert_token( objects_table, act_obj_fl->item->item );
      if ( h->memcode == -1 ) 
	{ /* new objects */
	  h->memcode = elcnt++;
	  h->factnode = act_obj_tl->item;
	  if ( rifo_display_info >= 5 ) 
	    printf( ">> ... adding %s and %s to objects table as no. %d\n",
		    h->key, h->factnode, h->memcode );
	} 
      else
	if ( rifo_display_info >= 5 )
	  printf( ">>> ... %s already in fact table as no. %d\n",
		   h->key, h->memcode );
      act_obj_fl =act_obj_fl->next;
      act_obj_tl =act_obj_tl->next;
    }
  return copy_tl;
}



/* generates tokens like name_type from token name */
/* simply gets the value from the hashtable objects_table installed by
   init_objs_from_types() */
token full_name_and_type( token name )
{
  rifo_hashentry_t h;
  char estr[MAXSTRLEN];

  if ( !(h = rifo_lookup_from_table( objects_table, name )) ) {
    sprintf( estr, "Error: Object %s not found in object table", name );
    fatal_error( estr );
  }
  return h->factnode;
}


/* initialize fact table with initial state*/
void init_tables()
{
  token_list f;
  rifo_hashentry_t h;
  int elcnt,i;

  /* build hashtable objects_table from orig_constant_list 
     and initialize global var constant_tl  */
  constant_tl = init_objs_from_types();
  if ( rifo_display_info >= 5 ) 
    printf( "> Initializing tables with initial state...\n" );
  clear_tables( ); /* start with fresh tables */
  /* now put initial facts and type information into rel_fct_table */
  elcnt = 0;
  for ( i=0; i<2; i++ ) 
    {
      if ( i == 0 ) f = constant_tl;
      else f = initial_facts;
      while ( f ) 
	{ /* insert initial fact or type declaration into rel_fct_table if
	     not yet in it */
	  h = rifo_insert_token( rel_fct_table, f->item );
	  if ( h->memcode == -1 ) 
	    { /* new fact */
	      h->memcode = elcnt++;
	      if ( rifo_display_info >= 5 ) 
		printf( ">> ... adding %s to fact table as no. %d\n", 
			h->key,h->memcode );
	      h->factnode = f->item;
	      /* used_facts contains one set with one member: memcode */
	      h->used_facts = make_set_list( h->memcode );
	    } 
	  else
	    if ( rifo_display_info >= 5 )
	      printf( ">>> ... %s already in fact table as no. %d\n",
		      h->key,h->memcode );
	  if ( elcnt > MAXSETSIZE-1 )
	    fatal_error ( "Too many initial facts.\nChange MAXSETSIZE and SETARSIZE and recompile!\n" );
	  f = f->next;
	}
    }
}




/* the heart of this program: the backchaining functions */



/* go back in the factgeneration tree from one fact to the operators
   that could possibly create it */
set_list fbackchain_one_goal( int depth, token fact )
{
  rifo_hashentry_t h;
  set_list sl;
  int nolength;

  h = rifo_lookup_from_table( rel_fct_table, fact ); /* look for old entry */
  /* if there's an old entry found it's h, otherwise h is NULL */
  if ( h && ( h->memcode >= 0 ) &&
      ( ( !backchain_on_ini ) || ( depth <= 0 ) ) ) 
    { /* initial fact */
      if ( rifo_display_info >= 5 ) 
	{
	  pprefix( curdepth-depth );
	  printf( ">>> Initial fact '%s': ", fact );
	  print_set_list( h->used_facts, "" );
	}
      sl = set_copy_list( h->used_facts );
    } 
  else if ( h && ( ( h->lastdepth >= depth ) ) ) 
    { /* cached and result was found */
      if ( rifo_display_info >= 5 ) {
	pprefix( curdepth-depth );
	printf( ">>> Cached fact '%s' on level %d, actual level %d: ", 
		 fact, h->lastdepth, depth );
	print_set_list( h->used_facts, "" );
      }
      sl = set_copy_list( h->used_facts );
    } 
  else 
    { /* not known yet, cached at deeper level, or backchain on ini */
      if ( depth <= 0 ) return NULL;
      if ( rifo_display_info >= 5 ) 
	{
	  pprefix( curdepth-depth );
	  if ( h )
	    if ( h->memcode >= 0 )
	      printf( ">>> Try to find something for initial fact %s ...\n",
		       fact );
	    else
	      printf( ">>> Cached fact '%s' on level %d, try again ...\n",
		       fact, curdepth - h->lastdepth );
	  else
	    printf( ">>> Yet unknown literal: %s, try ...\n",fact );
	}
      /* that's the point: from the goal node find all possible operators
	 by backchaining and save the possibility set sl */
      sl = fbackchain_ops( depth-1, fact ); /* backchain to get result ... */
      if ( h && ( h->memcode >= 0 ) )
	set_merge_into_list( &sl, &nolength, make_set( h->memcode ),0 );
      if ( rifo_display_info >= 5 ) 
	{
	  pprefix( curdepth-depth );
	  printf( ">>> Result for literal '%s': ", fact );
	  print_set_list( sl, "" );
	}
      /* maybe there is an entry now */
      h = rifo_lookup_from_table( rel_fct_table, fact ); 
      if ( h == NULL ) 
	h = rifo_insert_into_table( rel_fct_table, fact );
      /* free if a list was created previously */
      set_free_list( h->used_facts ); 
      h->lastdepth = depth;
      h->used_facts = set_copy_list( sl );
    }
  return sl;
}



/* All objects used in an instantiated operator are relevant for
   this operator - of course! 
   They are included into a set which is the basis for the set
   of relevant initial facts */
set_list check_constants( int depth, token_list constants )
{
  set_list sl;
  static char estr[MAXSTRLEN];
  rifo_hashentry_t h;
  token t; /* e.g. name_type */

  sl = make_set_list( NOELEMENT );
  while ( constants ) {
    t = full_name_and_type( constants->item );
    if ( ( h = rifo_lookup_from_table( rel_fct_table, t ) ) &&
	( h->memcode >= 0 ) ) 
      { /* if a known object is used in an instantiated operator it's
	   included into the set */
	set_insert_el( sl->item, h->memcode );
      } 
    else 
      {
	sprintf( estr,"Error: Object %s with wrong type\n", t  );
	fatal_error( estr );
      }
    constants = constants->next;
  }
  return sl;
}



/* backchain on each of the given goals and try to reach all (AND node).
   depth is the current search depth, constants_used is NULL in the beginning
   and later contains the objects used by the ground operator whose preconds
   are our actual goals */
set_list fbackchain_goals( int depth, token_list goals, 
			   token_list constants_used )
{
  set_list sl, new_sl;
  token_list my_goals = goals;

  nodes_visited++;
  if ( rifo_display_info >= 5 ) 
    {
      pprefix( curdepth-depth );
      printf( "+++ Trying to find plans for " );
      print_token_list( goals, ONE_LINE );
      printf( "\n" );
    } 
  /* first find the set including all objects used on next higher level
     by the ground op we're backchaining on... */
  sl = check_constants( depth, constants_used);
  while ( sl && goals ) {
    /* backchain on first goal, then make new possibility set sl from
       old sl and the new set for the first goal. This is done
       as long as there are still goals to backchain and the
       possibility set is not empty, which would mean there is no
       possibility to reach the goals */
    new_sl = fbackchain_one_goal( depth, goals->item );
    sl = set_multiply_lists( sl, new_sl );
    goals = goals->next;
  }
  if ( rifo_display_info >= 5 ) 
    {
      pprefix( curdepth-depth );
      printf( "--- Result for goals " );
      print_token_list( my_goals, ONE_LINE );
      printf( "\n" );
      pprefix( curdepth-depth );
      print_set_list( sl, "--- " );
    }
  return sl;
}



/* backchains on preconditions and effect conditions because one of
   the add effects in eff is needed */
set_list cond_fbackchain_ops( int depth, operator_list op, 
			      inst_effect_list eff )
{
  token_list new_goals = NULL;
  set_list setl;
  rifo_hashentry_t h;

  /* backchain on preconditions AND effect conditions */
  new_goals = merge_token_lists( op->preconditions, eff->conditions );
  setl = fbackchain_goals( (depth-1), new_goals, op->objects );

  if ( oplevel == 2 ) 
    {
      h = rifo_lookup_from_table( rel_op_table, op->name ); 
      /* maybe there is an entry now */
      if ( !h ) h = rifo_insert_into_table( rel_op_table, op->name );
      set_free_list( h->used_facts ); /* free previously created list */
      h->used_facts = set_copy_list( setl );
      h->lastdepth = depth;
      h->opnode = op;
    }

  if ( rifo_display_info >= 5 ) 
    {
      pprefix( curdepth-depth );
      printf( "=== Results for " );
      printf( op->name );
      printf( "\n" );
      pprefix( curdepth-depth );
      print_set_list( setl, "=== " );
    }
  return setl;
}



/* in this function we backchain on one single goal and try to reach
   it with different operators (OR node) */
set_list fbackchain_ops( int depth, token goal )
{
  set_list setl = NULL, new_setl;
  operator_list op = operators;
  inst_effect_list eff;
  token_list add_eff;

  nodes_visited++;
  if ( rifo_display_info >= 5 ) 
    {
      pprefix( curdepth-depth );
      printf( "??? Trying to find operators for %s ...\n",
	       goal );
    }
  while ( op ) 
    {
      eff = op->effects;
      while ( eff ) 
	{
	  add_eff = eff->add_effects;
	  while ( add_eff ) 
	    {
	      if ( !add_eff->item ) 
		fatal_error( "Error: Add effect not specified!" );
	      /* checks if goal is an add effect of op */
	      if ( strcmp( add_eff->item, goal ) == SAME ) {
		if ( rifo_display_info >= 5 ) 
		  {
		    pprefix( curdepth-depth );
		    printf( ">>> Trying add effect '%s' of operator %s to backchain...\n",
			    add_eff->item, op->name );
		    /* ...e.g. rifo could use on_a_b of op. stack_a_b */
		  }
		/* Now we have to backchain on the effect conditions and on
		   the preconditions */
		new_setl = cond_fbackchain_ops( depth, op, eff );
		setl = set_merge_lists( setl, new_setl );
	      }
	      add_eff = add_eff->next;
	    }
	  eff = eff->next;
	}
      op = op->next;
    }
  
  if ( rifo_display_info >= 5 ) 
    {
      pprefix( curdepth-depth );
      printf( "!!! Results for ops to get %s ...\n",
	       goal );
      pprefix( curdepth-depth );
      print_set_list( setl, "!!! " );
    }
  return setl;
}




/* functions for selecting relevant objects, facts and operators */ 


/* go recursively through list of facts and select those in in_set 
   that aren't found in but_not_in_set.
   Old list of facts is not changed but a new token_list is returned */
token_list rec_select_facts( token_list facts, settype *in_set, 
			     settype *but_not_in_set )
{
  rifo_hashentry_t h;
  token_list t;

  if ( facts == NULL ) return NULL;
  h = rifo_insert_token( rel_fct_table, facts->item );
  if ( h->memcode == -1 )
    fatal_error( "Initial fact has no memcode!\n" );
  if ( set_member( h->memcode, in_set ) && 
       !set_member( h->memcode, but_not_in_set ) ) 
    {
      if ( rifo_display_info >= 2 ) 
	{
	  printf( ">> Fact " );
	  printf( "%s", facts->item );
	  printf( " selected.\n" );
	}
      t = (token_list) CALLOC(1, sizeof( token_list_elt ) );
      t->item = facts->item;
      t->next = rec_select_facts( facts->next, in_set, but_not_in_set );
      return t;
    } 
  else 
    {
      if ( rifo_display_info >= 4 ) 
	{
	  printf( ">> Fact " );
	  printf( "%s", facts->item );
	  printf( " ignored.\n" );
	}
      return rec_select_facts( facts->next, in_set, but_not_in_set );
    }
}

/* build a set of initial facts appearing in a given token list */
settype* get_set_from_tl( token_list tl, settype* s )
{
 
  rifo_hashentry_t h;
  
  while ( tl ) 
    {
      h = rifo_lookup_from_table( rel_fct_table, tl->item );
      /* if token condition is found in table, i.e. is initial fact,
	 add it to the set */
      if ( h && (h->memcode != -1) ) 
	{
	  s = set_insert_el( s, h->memcode );
	}
      tl = tl->next;
    }
  return s;
}


/* build a set of initial facts appearing in a given effect list */
settype* rec_get_facts_from_eff_conds( inst_effect_list eff )
{
  settype* s;
  token_list cond;
  rifo_hashentry_t h;
  
  if ( !eff ) 
    {
      return make_set( NOELEMENT );
    }
  s = rec_get_facts_from_eff_conds( eff->next );
  s = get_set_from_tl( eff->conditions, s );
  return s;
}
    


/* takes all operators which were used in the fact generation tree (they
   are saved in rel_op_table) but only if they use objects selected as
   relevant 
   This is the sharpest heuristic because only a few of all possible
   operators are selected */
operator_list find_useful_ground_ops( settype *inifactset, int* newcountp )
{
  rifo_hashentry_t h;
  operator_list dummy, act, newop;
  int is_ok, ops_in_table = 0;
  set_list fact_set;
  settype* needed_facts_set = NULL;

  rifo_get_next( rel_op_table, 0 ); /* INIT table to read out from beginning */
  *newcountp = 0;
  act = dummy = (operator_list) CALLOC(1, sizeof( operator_list_elt ) ); 
  while ( ( h = rifo_get_next( rel_op_table, 1 ) ) ) 
    {
      ops_in_table++;
      is_ok = 0;
      fact_set = h->used_facts;
      while (fact_set) 
	{
	  /* if one of the sets is a subset it might be possible */
	  if ( set_subseteq( fact_set->item, inifactset ) ) 
	    {
	      is_ok = 1;
	      break;
	    }
	  fact_set = fact_set->next;
	}
      if (is_ok) 
	{
	  (*newcountp)++;
	  newop = act->next = (operator_list) 
	    CALLOC(1, sizeof( operator_list_elt ) );
	  newop->name = h->opnode->name;   

	  newop->objects = h->opnode->objects;
	  newop->preconditions = h->opnode->preconditions;
	  newop->effects = h->opnode->effects;
	  newop->next = NULL;
	  /* now declare all initial facts appearing as effect conditions 
	     of this operator as relevant (saved in secondary_fact_set).
	     Later they will be put into secondary_initial_facts and merged 
	     with the primarily needed ones */
	  needed_facts_set = rec_get_facts_from_eff_conds( newop->effects );
	  secondary_fact_set = set_union( secondary_fact_set, 
					  secondary_fact_set, 
					  needed_facts_set, 1 );
	  act = newop;
	  if ( rifo_display_info >= 3 ) 
	    {
	      printf( ">> Selected ground operator: %s",h->key);
	      if ( rifo_display_info >= 5 )
		print_set_list( h->used_facts, " used facts" );
	      else
		printf( "\n");
	    }
	} 
      else 
	{
	  if ( rifo_display_info >= 4 )
	    {
	      printf( ">> Ignored ground operator: %s",h->key );
	      if ( rifo_display_info >= 5 )
		print_set_list( h->used_facts, " used facts" );
	      else
		printf( "\n");
	    }
	}
    }
  if ( rifo_display_info >= 5 ) 
    {
      printf( "--- %d operators in table\n", ops_in_table ); 
      act = operators;
      while ( act ) 
	{
	  if ( rifo_lookup_from_table( rel_op_table, act->name ) == NULL )
	    printf( "--- %s was not used during fact generation\n",
		    act->name );
	  act = act->next;
	}
    }
  if ( rifo_display_info >= 3 ) 
    printf( "\n" );
  return dummy->next;
}



/* help function for filter_possible_ground_ops
   returns list of operators that use relevant objects */
operator_list rec_find_possible_ground_ops( operator_list current_old, 
					    rifo_hashtable_t const_table, 
					    int* newcountp )
{
  token_list act_obj;
  operator_list act;
  settype* needed_facts_set = NULL;

  if ( !current_old ) return NULL;
  act_obj = current_old->objects;
  while ( act_obj ) 
    { 
      if ( !rifo_lookup_from_table( const_table, 
				    full_name_and_type(act_obj->item) ) ) 
	{
	  if ( rifo_display_info >= 4 ) 
	    printf( ">>>> operator %s ignored because %s is not relevant\n", 
		    current_old->name, act_obj->item );
	  return rec_find_possible_ground_ops( current_old->next, 
					       const_table, newcountp );
	}
      act_obj = act_obj->next;
    }
  if ( rifo_display_info >= 3 ) 
    printf( ">>>> operator %s uses relevant objects and was selected!\n", 
	    current_old->name );
  
  (*newcountp)++;
  act = (operator_list) CALLOC(1, sizeof( operator_list_elt ) );
  act->name = current_old->name; 
  act->objects = current_old->objects;
  act->preconditions = current_old->preconditions;
  act->effects = current_old->effects;
  /* now declare all initial facts appearing as effect conditions of this
     operator as relevant (saved in secondary_fact_set). Later they will 
     be put into secondary_initial_facts and merged with the primarily 
     needed ones */
  needed_facts_set = rec_get_facts_from_eff_conds( act->effects );
  secondary_fact_set = set_union( secondary_fact_set, secondary_fact_set, 
				  needed_facts_set, 1 );
  act->next = rec_find_possible_ground_ops( current_old->next, 
					    const_table, newcountp );
  return act;
}



/* builds table of relevants objects and 
   returns list of operators that use relevant objects */
operator_list filter_possible_ground_ops( settype *set, int* newcountp )
{
  rifo_hashtable_t const_table;
  rifo_hashentry_t h;
  token_list constants = constant_tl;

  if ( rifo_display_info >= 5 ) 
    printf( ">>>> looking for constants which appear in factset...\n" );
  init_op_table( const_table );
  while ( constants ) 
    {
      h = rifo_insert_token( rel_fct_table, constants->item );
      if ( h->memcode == -1 )
	fatal_error( "constant has no memcode!\n" );
      if ( set_member( h->memcode, set ) ) 
	{ /* constant is relevant */
	  rifo_insert_token( const_table, constants->item );
	  if ( rifo_display_info >= 5 ) 
	    printf( ">>>> ... adding %s to const_table as no. %d\n",
		    h->key, h->memcode );
	}
      constants = constants->next;
    }
  /* now we have a table in which all relevant objects appear... */
  return rec_find_possible_ground_ops( operators, const_table, newcountp );
  /* ... and may return all operators that use only those objects */
  if ( rifo_display_info >= 3 ) 
    printf( "\n" );
}



/* put all relevant facts (i.e. they appear in set) into table */
void select_relevant_tokens( token_list facts, settype *set, 
			     rifo_hashtable_t table )
{
  rifo_hashentry_t h;
  token_list t;

  while ( facts ) 
    {
      h = rifo_insert_token( rel_fct_table, facts->item );
      if ( h->memcode == -1 )
	fatal_error( "Initial fact or type has no memcode!\n" );
      if ( set_member( h->memcode, set ) ) 
	{ /* constant or type is relevant */
	  t = token_list_from_token( facts->item );
	  while ( t ) 
	    { /* add single tokens like in, obj1, bag */
	      if ( rifo_display_info >= 5 ) 
		printf( ">>>> insert token %s...\n", t->item );
	      rifo_insert_token( table, t->item );
	      t = t->next;
	    }
	}
      facts = facts->next;
    }
}
    


/* return those facts that consist only of tokens which are relevant
   = they appear in table. Old token_list facts will not be changed
   but a new token_list is built up */
token_list rec_filter_facts( token_list facts, rifo_hashtable_t table )
{
  token_list t;

  if ( facts == NULL ) return NULL;
  t =  token_list_from_token( facts->item );
  if ( t && t->next && !(strcmp(t->next->item,"object")==SAME) )
    { /* this one is not an object, but an initial, so
	 ignore the first token which is the predicate name */
      t = t->next;
    }
  while ( t ) 
    {
      if ( !rifo_lookup_from_table( table,t->item ) ) 
	{
	  if ( rifo_display_info >= 4 ) 
	    {
	      printf( ">> Fact %s ignored", facts->item );
	      if ( rifo_display_info >= 5 )
		printf( ", %s is no relevant object", t->item );
	      printf( "\n" );
	    }
	  return rec_filter_facts( facts->next,table );
	}
      t = t->next;
    }
  if ( rifo_display_info >= 2) 
    {
      printf( ">> Fact " );
      printf( "%s", facts->item );
      printf( " selected.\n" );
      fflush( stdout );
    }
  t = (token_list) CALLOC(1, sizeof( token_list_elt) );
  t->item = facts->item;
  t->next = rec_filter_facts( facts->next, table );
  return t;
}



/* main routine: find relevant facts by backchaining and minimizing the
   set of used initial facts */
BOOLEAN find_relevant_initial_facts( BOOLEAN really_run )
{
  static set_list results;
  set_list temp;
  static settype *factset = NULL;  /* union over the sets in the final pos. set */
  int numres = -1;
  int oldfnum, newfnum;
  int oldopnum, newopnum = 0;
  int depth;
  static rifo_hashtable_t objtable;
  token_list primary_initial_facts = initial_facts;
  token_list secondary_initial_facts = NULL;
  
  /* it is intended to run RIFO just one time and use the information won 
     there several times in different factlevel/oplevel combinations */
  if ( really_run )
    {
      init_tables();  /* mak'em clean and initialize with inital state */
      
      depth = mindepth;
      maxdepth = MAX( depth,maxdepth );
      if ( rifo_display_info >= 1 )
	printf( "rifo: backchaining process started... \n" );
      while ( depth <= maxdepth ) 
	{
	  if ( rifo_display_info >= 5 )
	    printf( "> ... using depth %d\n", depth );
	  /* Backchain on goals, no constants because goals are no operator 
	     preconds */
	  results = fbackchain_goals( (curdepth=depth*2), goal_facts, NULL );
	  numres = set_list_length( results );
	  if ( rifo_display_info >= 5 )
	    printf( "> ... %d resulting initial-fact set%s found\n",
		    numres, ( ( numres != 1 ) ? "s" : "" ) );
	  if ( rifo_display_info >= 5 ) 
	    {
	      temp = results;
	      while ( temp ) 
		{
		  printf( ">> Initial-fact set:" );
		  print_one_set( temp->item, "", 0 );
		  printf( "\n" );
		  temp = temp->next;
		}
	    }      
	  if ( numres > 0 ) 
	    { /* now build the union with one of the strategies described in
		 the paper over the sets in "results" */
	      factset = set_union_list( results, unionstrategy );
	      break;
	    }
	  depth++;
	}

      if ( factset == NULL ) 
	{
	  printf( "Cannot find a solution for depth %d.\n",maxdepth );
	  printf( "Returning original fact file.\n" );
	  return FALSE;
	}
    }
  else
    constant_tl = token_list_from_fact_list( orig_constant_list );

  oldfnum = token_list_length( constant_tl );
  oldfnum += token_list_length( initial_facts );
  oldopnum = op_list_length( operators );
  empty_set = make_set( NOELEMENT );
  primary_fact_set = make_set( NOELEMENT );
  secondary_fact_set = make_set( NOELEMENT );

  if ( factlevel == 1 ) 
    { /* take initial facts that use rel. objects */
      init_op_table( objtable );
      if ( rifo_display_info >= 5 ) 
	{ 
	  printf( "> Inserting tokens into objtable ...\n" ); 
	}
      /* use only initial facts dealing with relevant objects
	 (this means that the objects appear in the set of possibly
	 relevant facts "factset") and put them into objtable... */
      select_relevant_tokens( constant_tl, factset, objtable ); 
      select_relevant_tokens( initial_facts, factset, objtable ); 
      /* ...and now separate them again into initials and types */ 
      if ( rifo_display_info >= 5 ) 
	printf( "\n> Filtering relevant objects...\n" ); 
      constant_tl = rec_filter_facts( constant_tl, objtable );
      if ( rifo_display_info >= 5 ) 
	printf( "\n> Filtering initial facts that use relevant objects...\n" ); 
      primary_initial_facts = rec_filter_facts( initial_facts, objtable );
    } 
  else if ( factlevel == 2 ) 
    { /* strong filter: only facts mentioned in factset */
      if ( rifo_display_info >= 5 ) 
	printf( "\n> Filtering relevant objects...\n" ); 
      constant_tl = rec_select_facts( constant_tl, factset, empty_set );
      if ( rifo_display_info >= 5 ) 
	printf( "\n> Filtering initial facts from set of potentially relevant facts...\n" ); 
      primary_initial_facts = rec_select_facts( initial_facts, factset, 
						empty_set );
    }
  if ( factlevel > 0 && oplevel != 2) 
    {
      if ( rifo_display_info >= 5 ) 
	{
	  printf( "\n> Filtering ground ops using relevant objects...\n" );
	}	  
      newopnum = 0;
      operators = filter_possible_ground_ops( factset, &newopnum );
      if ( rifo_display_info >= 1 ) 
	{
	  printf( "rifo: %d out of %d ground operators using relevant objects selected.\n", 
		  newopnum, oldopnum );
	}
    }
  if ( oplevel == 2 ) 
    {   /* useful ground (instantiated) operators */
      if ( rifo_display_info >= 5 ) 
	{
	  printf( "\n> Filtering ground ops appearing in the fact generation tree...\n" ); 
	}
      newopnum = 0;
      operators = find_useful_ground_ops( factset, &newopnum );
      if ( rifo_display_info >= 1 ) 
	{
	  printf( "rifo: %d out of %d ground operators selected.\n", 
		  newopnum, oldopnum );
	}
    }
  /* after having selected the ground ops some initial facts 
     appearing as effect conditions have to be added */
  if ( rifo_display_info >= 5 ) 
    printf( "\n> Filtering initial facts needed as effect conditions...\n" ); 
  primary_fact_set = get_set_from_tl( primary_initial_facts, 
				      primary_fact_set );
  secondary_initial_facts = rec_select_facts( initial_facts, 
					      secondary_fact_set, 
					      primary_fact_set);
  initial_facts = merge_token_lists( primary_initial_facts, 
				     secondary_initial_facts );
  if ( rifo_display_info >= 1 ) 
    {
      printf( "rifo: selected %d initials first, %d initials second time, %d objects.\n", 
	      token_list_length( primary_initial_facts ), 
	      token_list_length( secondary_initial_facts),
	      token_list_length( constant_tl ) );      
      newfnum = token_list_length( constant_tl );
      newfnum += token_list_length( initial_facts );
      printf( "rifo: %d out of %d initial facts selected as relevant.\n",
	      newfnum, oldfnum );
    }
  
  if ( rifo_display_info >= 1 ) 
    {
      printf( "\n" );
    }

  return TRUE;
}

