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

#ifndef lint
static char rcsid[] = "$Id: build_graph.c,v 1.2 1998/05/27 16:25:30 ipp Exp ipp $";
#endif /* lint */

/* frank: habe alle log10 auskommentiert, da mit gprof immer 
 * Fehler kommen */

/*
 * functions for building graph:
 *   BOOLEAN build_graph( int * )
 *   void build_graph_layer( void )
 *
 * makes use of the following functions:
 *   vertex_list insert_into_table( hashtable, char * ) ,
 *   vertex_list get_next( hashtable, BOOLEAN ) ,
 *   vertex_list lookup_from_table( hashtable, char * )
 * taken from hash.c ,
 *   BOOLEAN are_there_non_exclusive( token_list, int ) ,
 *   BOOLEAN get_them_non_exclusive( token_list, int, goal_array *, int * )
 *   edge_list insert_edge( edge_list, vertex_list ) ,
 *   edge_list insert_edge_at_end( edge_list, vertex_list ) ,
 *   cond_edge_list insert_cond_edge( cond_edge_list,
 *                                    vertex_list, token_list ) ,
 *   cond_edge_list insert_cond_edge_at_end( cond_edge_list,
 *                                           vertex_list, token_list ),
 *   void set_uid( vertex_list, int ) ,
 *   char *make_noop_string( char * )
 * taken from util_build.c ,
 *   void find_mutex_ops_and_insert_del_edges( int ) ,
 *   pair find_mutex_facts( int ) ,
 *   void make_exclusive( vertex_list, vertex_list ) ,
 *   BOOLEAN are_mutex( vertex_list, vertex_list )
 * taken from exclusions.c
 */

#include"ipp.h" /* defines, data structures, fn prototypes, global variables */
#include<math.h> /* for logarithm-use in heuristics */

/* main function for extending graph at least *min_time steps
 * until goals are reached non exclusively first time
 * is called exactly one time by main, at the very beginning
 * of extend graph/search for plan - phase
 *
 * return value is true gdw goals can be reached non mutex in <= MAX_PLAN steps
 */  
BOOLEAN build_graph( int *min_time )

{

  int time = 0;/* index for current time step */
  vertex_list ft;/* for setting up initial fact level */
  token_list i_token;/* index */
  BOOLEAN reached_goals = FALSE, first = TRUE;/* return value, flag */
  int i = 0;/* for initial uid s */

  /* insert initial facts into time step 0 */
  for ( i_token = initial_facts; i_token; i_token = i_token->next ) {
    ft = insert_into_table( fact_table[rifo_active_part][0], i_token->item );
    set_uid( ft, i++ );
  }

  /* plan until goals are reached or graph has leveled off */
  for( ; time < MAX_PLAN; time++ ) {
    reached_goals = are_there_non_exclusive( goal_facts, time );
    if ( reached_goals ) {
      if ( display_info && time > 0 && first ) {
        printf("\nipp: goals first reachable in %d time steps\n\n", time);
      }
      break;
    }
    if ( same_as_prev_flag ) break;
    build_graph_layer( ( time==0 ) );
  }

  *min_time = time;
  return reached_goals;

}


/* this is the main function for building the graph;
 * builds one layer of the graph by applying the 
 * operators to the facts at time step <time>;
 * has to be called on consecutive time steps, just
 * to be sure about that, time is a static variable
 */
void build_graph_layer( BOOLEAN new_graph )

{

  static int time = 0;/* holds current time */
  static pair fact_summary, old_fact_summary;/* used for checking level-off */

  token_list i_token;/* index */
  vertex_list ft1, ft2, op, ft;/* auxiliary pointers to fact-vertexes */
  operator_list i_operator;/* index */
  int i;/* for setting up uids */

  pot_eff_list potentials = NULL, pot_end = potentials, temp;

  if ( new_graph ) {
    time = 0;
  }

  /* initialise summary */
  if ( time == 0 ) {
    fact_summary.first = 0;
    for ( i_token = initial_facts; i_token; i_token = i_token->next )
      fact_summary.first++;/* first holds number of facts */
    fact_summary.second = 0;/* second holds number of exclusion relations */
  }

  if ( same_as_prev_flag ) {
    /* graph has leveled off; just copy over */
    make_copy( time );
  } else {
    /* first copy facts over to next time step ( ->noop s ) */
    get_next( fact_table[rifo_active_part][time], INIT );/* initialise */
    while ( ( ft1 = get_next( fact_table[rifo_active_part][time], EXEC ) ) != NULL ) {
      ft2 = insert_into_table( fact_table[rifo_active_part][time+1], ft1->name );
      ft2->prev_time = ft1;
      ft1->next_time = ft2;
    }

    /* apply the operators */
    for ( i_operator = operators; i_operator; i_operator = i_operator->next ){
      temp = apply_operator( i_operator, time );
      if ( !temp ) continue;
      if ( potentials ) {
	pot_end->next = temp;
	for ( ; temp; temp = temp->next ) pot_end = pot_end->next;
      } else {
	potentials = temp;
	temp = temp->next;
	pot_end = potentials;
	for ( ; temp; temp = temp->next ) pot_end = pot_end->next;
      }
    }

    /* insert noop s; doing it here, they will be first
     * in the hashtable lists( planner tries them first )
     */
    make_noop_layer( time );

    /* setup uids ( technical for finding exclusions ) */
    get_next( op_table[rifo_active_part][time], INIT );/* init */
    for ( i = 0; ( op = get_next( op_table[rifo_active_part][time], EXEC ) ) != NULL; i++ ) {
      if ( i>= max_nodes ) {
        printf( "\nipp: too many operators. increase max_nodes\n\n" );
	OUTPUT_FILE;
        exit( 1 );
      }
      set_uid( op, i );
    }
    get_next( fact_table[rifo_active_part][time+1], INIT );/* init */
    for ( i = 0; ( ft = get_next( fact_table[rifo_active_part][time+1], EXEC ) ) != NULL; i++) {
      if ( i>= max_nodes ) {
        printf( "\nipp: too many facts. increase max_nodes\n\n" );
	OUTPUT_FILE;
        exit( 1 );
      }
      set_uid( ft, i );
    }

    /* insert mutual exclusions between operators
     * and connect the delete edges;
     * do delete edges here cause all the add edges have
     * to be done first;( see details in apply_operator and 
     * find_mutex_ops_and_insert_del_edges )
     */
    find_mutex_ops_and_insert_del_edges( time );

    /* insert those effects which have conditions made true by possibly
     * parellel chosen actions; insert the conditions as dummy nodes
     * ( facts that are not added at all ) in fact_table[time];
     * those are needed for natural resolving conflicts between chosen
     * ops
     */
    insert_potential_effects( time, potentials );

    /* insert mutual exclusions between facts
     * and check if graph has leveled off
     */
    old_fact_summary = fact_summary;
    fact_summary = find_mutex_facts( time + 1 );
    if ( fact_summary.first == old_fact_summary.first &&
         fact_summary.second == old_fact_summary.second  ) {
      same_as_prev_flag = TRUE;
      if ( display_info ) 
        printf( "\nipp: graph has leveled off at time step %d\n\n", time+1 );
      first_full_time = time;
    }
  }
  
  /* print out info, if required */
  if ( display_info ) {
    printf( "time: %3d, %3d facts and %5d exclusive pairs\n",
             time+1, fact_summary.first, fact_summary.second );
  }

  /* increment time */
  time++;

}


/* this function is called after graph has leveled off;
 * to copy op_table[time-1] to op_table[time]
 * and fact_table[time] to fact_table[time+1]
 */
void make_copy( int time )

{

  /* help pointers to vertexes: op : operator vertex, ft: fact vertex */
  vertex_list op1, op2, ft, ft1, ft2, op;

  edge_list i_e, condition_list, temp;/* index */
  cond_edge_list i_ce;/* index */

  int i;
  vertex_list o;

  /* first do the ops and connect to their preconditions,
   * copy over uids
   */
  get_next( op_table[rifo_active_part][time-1], INIT );/* initialise */
  while ( ( op1 = get_next( op_table[rifo_active_part][time-1], EXEC ) ) != NULL ) {
    op2 = insert_into_table( op_table[rifo_active_part][time], op1->name );
    op2->prev_time = op1;
    op1->next_time = op2;
    op2->uid_mask = op1->uid_mask;
    op2->uid_block = op1->uid_block;
    op2->is_noop = op1->is_noop;

    for ( i_e = op1->precond_edges; i_e; i_e = i_e ->next ) {
      ft = i_e->endpt->next_time;/* that is our new precondition */
      op2->precond_edges = insert_edge_at_end( op2->precond_edges, ft );
      ft->precond_edges = insert_edge_at_end( ft->precond_edges, op2 );
    }
  }
  /* now all ops at step time-1 have pointer op->next_time
   * to same op at step time. <*> needed later in this function
   */

  /* now do the facts and connect the add-effect edges,
   * also copy over uids
   */
  get_next( fact_table[rifo_active_part][time], INIT );/* initialise */
  while ( ( ft1 = get_next( fact_table[rifo_active_part][time], EXEC ) ) != NULL ) {
    ft2 = insert_into_table( fact_table[rifo_active_part][time+1], ft1->name );
    ft2->prev_time = ft1;
    ft1->next_time = ft2;
    ft2->uid_mask = ft1->uid_mask;
    ft2->uid_block = ft1->uid_block;
    if ( ft1->my_noop ) ft2->my_noop = ft1->my_noop->next_time;

    for ( i_ce = ft1->add_edges; i_ce; i_ce = i_ce->next ) {
      op = i_ce->endpt->next_time;/* that is the new add-operator */
      condition_list = NULL;
      for ( i_e = i_ce->conditions; i_e; i_e = i_e->next ) {
        temp = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
	CHECK_MEMORY(temp);
	GRAPH(edge_list_elt);
        temp->endpt = i_e->endpt->next_time;
        temp->next = condition_list;
        condition_list = temp;
      }
      ft2->add_edges = insert_cond_edge_at_end( ft2->add_edges,
                                              op, condition_list );
      op->add_edges = insert_cond_edge_at_end( op->add_edges,
                                              ft2, condition_list );
    }
  }
  /* now also all facts at step time have pointer fact->next_time
   * to same fact at step time+1. <+> needed right now
   */

  /* copy the exlusions and del_edges from facts time to facts time+1 */
  get_next( fact_table[rifo_active_part][time+1], INIT );/* initialise */
  while ( ( ft = get_next( fact_table[rifo_active_part][time+1], EXEC ) ) != NULL ) {
    for ( i = 0; i<HSIZE; i++ ) {
      for ( o = fact_table[rifo_active_part][time][i]; o; o = o->next ) {
	if ( o == ft->prev_time || (int) o < (int) ft->prev_time ) continue;
	if ( ARE_MUTEX( o, ft->prev_time ) )
	  make_exclusive( ft, o->next_time );
      }
    }
    for( i_ce = ft->prev_time->del_edges; i_ce; i_ce = i_ce->next ) {
      condition_list = NULL;
      for ( i_e = i_ce->conditions; i_e; i_e = i_e->next ) {
        temp = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
	CHECK_MEMORY(temp);
	GRAPH(edge_list_elt);
        temp->endpt = i_e->endpt->next_time;
        temp->next = condition_list;
        condition_list = temp;
      }
      ft->del_edges = insert_cond_edge( ft->del_edges,
                                        i_ce->endpt->next_time,
                                        condition_list );
    }/* need <*> for second argument of insert_edge - call */
  }

  /* now do the same thing for the operators( one time step earlier ) */
  get_next( op_table[rifo_active_part][time], INIT );/* initialise */
  while ( ( op = get_next( op_table[rifo_active_part][time], EXEC ) ) != NULL ) {
    for ( i = 0; i<HSIZE; i++ ) {
      for ( o = op_table[rifo_active_part][time-1][i]; o; o = o->next ) {
	if ( o == op->prev_time || (int) o < (int) op->prev_time ) continue;
	if ( ARE_MUTEX( o, op->prev_time ) )
	  make_exclusive( op, o->next_time );
      }
    }
    for( i_ce = op->prev_time->del_edges; i_ce; i_ce = i_ce->next ) {
      condition_list = NULL;
      for ( i_e = i_ce->conditions; i_e; i_e = i_e->next ) {
        temp = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
	CHECK_MEMORY(temp);
	GRAPH(edge_list_elt);
        temp->endpt = i_e->endpt->next_time;
        temp->next = condition_list;
        condition_list = temp;
      }
      op->del_edges = insert_cond_edge( op->del_edges,
                                        i_ce->endpt->next_time,
                                        condition_list );
    }/* need <+> for second argument of insert_edge - call */
  }

}


/* this function simply inserts the noop s, assuming that the facts
 * are already there
 */
void make_noop_layer( int time )

{

  vertex_list ft1, ft2, noop;/* help pointers */
  double heuristic;
  cond_edge_list i_ce;

  /* for all facts at step time, insert noop with effect fact at step time+1 */
  get_next( fact_table[rifo_active_part][time], INIT );/* initialise */
  while ( ( ft1 = get_next( fact_table[rifo_active_part][time], EXEC ) ) != NULL ) {
    ft2 = ft1->next_time;
    noop = insert_noop_into_table( op_table[rifo_active_part][time],
				   make_noop_string( ft1->name ) );

    /* alte Version mit memory leak */
    /*     noop = insert_into_table( op_table[rifo_active_part][time], */
    /* 			      make_noop_string( ft1->name ) ); */

    noop->is_noop = TRUE;
    /* connect the precond edge */
    noop->precond_edges = insert_edge( noop->precond_edges, ft1 );
    ft1->precond_edges = insert_edge( ft1->precond_edges, noop );
    switch ( do_heuristic ) {
      
    case 0: 
      break;   
      
    case 1:
      heuristic = 0.0;
      for ( i_ce = ft1->add_edges; i_ce; i_ce=i_ce->next ) {
	heuristic += i_ce->endpt->heuristic;
	heuristic += 1.0;
      }
    if ( time > 0 )
      noop->heuristic = heuristic;
    else
      noop->heuristic = 1.0;
    break;
    
  case 2:
    heuristic = 10.0;
    for ( i_ce = ft1->add_edges; i_ce; i_ce=i_ce->next ) {
          heuristic *= i_ce->endpt->heuristic;
    }
    if ( time > 0 ) 
       noop->heuristic = log10(heuristic); 
     else 
       noop->heuristic = 10.0; 
    break;
    
  } 
    /* connect the add edge. of course, condition list is NULL */
    noop->add_edges = insert_cond_edge( noop->add_edges, ft2, NULL );
    if ( !do_heuristic )
      ft2->add_edges = insert_cond_edge( ft2->add_edges, noop, NULL );
    else
      ft2->add_edges = insert_sort_cond_edge( ft2->add_edges, noop, NULL );
    /* insert my noop info */
    ft2->my_noop = noop;
  }

}


/* tries to apply given operator to fact_table[time];
 * connects precond and add edges in case operator can be applied
 * and builds del_list.
 *
 * returns list of effects that might be in the graph
 *
 * uses BOOLEAN are_mutex( vertex_list, vertex_list )
 * taken from exclusions.c, get_them_non_exclusive
 * and some insert_edge - like functions, which are defined
 * in util_build.c
 */
pot_eff_list apply_operator( operator_list operator, int time )

{

  static goal_array ft_pre, ft_con;/* array for precond facts */

  token_list i_token;/* index */
  int num_pre, num_con, i, j;/* num - numbers of conds, i,j indizes */

  vertex_list operator_vertex;/* this is the generated operator vertex */

  inst_effect_list i_effect;/* index */
  vertex_list ft;/* used for inserting new fact vertexes at step time+1 */

  delete_list new_delete;/* used for building del_list */

  BOOLEAN still_ok;/* used in checking effect conditions */
  edge_list condition_list, temp;/* to build up edge_list in cond_edge */

  double heuristic;

  cond_edge_list i_ce;

  pot_eff_list potentials = NULL, temp_pot;

  /* check if the preconds are there
   * and load them into ft array
   */
  if ( !get_them_non_exclusive( operator->preconditions, time,
                                &ft_pre, &num_pre ) )
    return NULL;

  /* apply operator,
   * first get new vertex 
   */
  operator_vertex = insert_into_table( op_table[rifo_active_part][time], operator->name );

  /* connect the preconds */
  switch ( do_heuristic ) {

  case 0: 
    for ( i=0; i<num_pre; i++ ) {
      operator_vertex->precond_edges =
	insert_edge( operator_vertex->precond_edges, ft_pre[i] );
      ft_pre[i]->precond_edges =
	insert_edge( ft_pre[i]->precond_edges, operator_vertex );
    }
    break;   
    
  case 1:
    heuristic = 0.0;
    for ( i=0; i<num_pre; i++ ) {
      operator_vertex->precond_edges =
	insert_edge( operator_vertex->precond_edges, ft_pre[i] );
      ft_pre[i]->precond_edges =
	insert_edge( ft_pre[i]->precond_edges, operator_vertex );
      for ( i_ce = ft_pre[i]->add_edges; i_ce; i_ce=i_ce->next ) {
	heuristic += i_ce->endpt->heuristic;
	heuristic += 1.0;
      }
    }
    if ( time > 0 )
      operator_vertex->heuristic = num_pre == 0 ? 1.0 : heuristic / num_pre; 
    else
      operator_vertex->heuristic = 1.0;
    break;
    
  case 2:
    heuristic = 10.0;
    for ( i=0; i<num_pre; i++ ) {
      operator_vertex->precond_edges =
	insert_edge( operator_vertex->precond_edges, ft_pre[i] );
      ft_pre[i]->precond_edges =
	insert_edge( ft_pre[i]->precond_edges, operator_vertex );
      for ( i_ce = ft_pre[i]->add_edges; i_ce; i_ce=i_ce->next ) {
	heuristic *= i_ce->endpt->heuristic;
      }
    }
    if ( time > 0 )
      operator_vertex->heuristic = num_pre == 0 ? 10.0 : log10(heuristic * num_pre);
    else
      operator_vertex->heuristic = num_pre == 0 ? 10.0 : log10(10 * num_pre);
    break;
    
  default:
    printf("\nipp: check your computer; this output is not possible\n\n");
    OUTPUT_FILE;
    exit( 1 );
  }
  /* AUsgabe Zahlenwerte der Heuristiken */
  /*   printf("%s %f\n",operator->name,operator_vertex->heuristic); */

  /* insert add edges and build del_list */
  for( i_effect = operator->effects; i_effect; i_effect = i_effect->next ) {
    /* for each effect do:
     * set up condition list and connect edges
     */
    if ( i_effect->conditions ) {
      /* is conditional: look conditions up,
       * if they are possibly true: build list
       */
      if ( !get_them( i_effect->conditions, time,
		      &ft_con, &num_con ) ) {
	temp_pot = ( pot_eff_list ) calloc( 1, sizeof( pot_eff_list_elt ) );
	CHECK_MEMORY(temp_pot);
	GRAPH(pot_eff_list_elt);
	temp_pot->op = operator_vertex;
	temp_pot->conditions = i_effect->conditions;
	temp_pot->adds = i_effect->add_effects;
	temp_pot->dels = i_effect->del_effects;
	temp_pot->next = potentials;
	potentials = temp_pot;
	continue;
      }
      /* see if they are exclusive */
      for ( i=0; i<num_con; i++ ) {
	for ( j=i+1; j<num_con; j++ )
	  if ( ARE_MUTEX( ft_con[i], ft_con[j] ) ) break;
	if ( j<num_con ) break;
      }
      if ( i<num_con ) continue;
      /* see if they are exclusive of preconds */
      for ( i=0; i<num_con; i++ ) {
	for ( j=0; j<num_pre; j++ )
	  if ( ARE_MUTEX( ft_con[i], ft_pre[j] ) ) break;
	if ( j<num_pre ) break;
      }
      if ( i<num_con ) continue;

      /* now build list */
      condition_list = NULL;
      for ( i = 0; i < num_con; i++ ) {
	temp = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
	CHECK_MEMORY(temp);
	GRAPH(edge_list_elt);
	temp->endpt = ft_con[i];
	temp->next = condition_list;
	condition_list = temp;
      }
    } else {
      /* list will be empty */
      condition_list = NULL;
    }
    /* effect conditions can possibly be made true */
    for( i_token = i_effect->add_effects; i_token; i_token =i_token->next){
      /* for each add effect do */
      ft = lookup_from_table( fact_table[rifo_active_part][time+1], i_token->item );
      if ( !ft ) {
	ft = insert_into_table( fact_table[rifo_active_part][time+1], i_token->item );
      }
      /* now ft is add effect vertex at step time+1:
       * connect the conditional edges with the
       * conditions of current effect
       */
      operator_vertex->add_edges = 
	insert_cond_edge( operator_vertex->add_edges,
			  ft, condition_list ); 
      if ( do_heuristic )
	ft->add_edges = 
	  insert_sort_cond_edge( ft->add_edges, 
				 operator_vertex, condition_list );
      else
        ft->add_edges = 
	  insert_cond_edge( ft->add_edges, 
			    operator_vertex, condition_list );
    }
    for( i_token = i_effect->del_effects; i_token; i_token =i_token->next){
      /* for each del effect do:
       * store deleted fact and it's conditions in
       * operators del_list; when all add - facts are inserted,
       * i.e. after all calls of apply_operator, build del_edges for those
       * deletes from del_list, which are in fact_table[rifo_active_part][time+1]
       * this is done in find_mutex_ops_and_insert_del_edges
       * ( in file exclusions.c )
       */
      new_delete = ( delete_list ) calloc( 1, sizeof( delete_list_elt ) );
      CHECK_MEMORY(new_delete);
      GRAPH(delete_list_elt);
      new_delete->effect = i_token->item;
      new_delete->conditions = condition_list;
      new_delete->next = operator_vertex->del_list;
      operator_vertex->del_list = new_delete;
    }
  }
 
  return potentials;

}


void insert_potential_effects( int time, pot_eff_list potentials )

{

  pot_eff_list p;

  static goal_array next_facts;
  int num;

  for ( p = potentials; p; p = p->next )
    if ( pot_applicable( p, time, &next_facts, &num ) )
      put_pot_eff_in( p, time, next_facts, num );

}


BOOLEAN pot_applicable( pot_eff_list p, int time,
			goal_array *next_facts, int *num ) 

{

  token_list t;
  int i;
  cond_edge_list c_e;

  *num = 0;

  for ( t = p->conditions; t; t = t->next ) {
    if ( 0 )
      printf("now trying to find cond: %s\n", t->item);
    (*next_facts)[*num] = lookup_from_table( fact_table[rifo_active_part][time+1], t->item );
    if ( !(*next_facts)[*num] ) {
      if ( 0 )
	printf("didnt find pot cond %s\n", t->item );
      return FALSE;/* not found one fact */
    }
    (*num)++;
  }

  for ( i=0; i<(*num); i++ ) {
    for ( c_e = (*next_facts)[i]->add_edges; c_e; c_e = c_e->next )
      if ( c_e->endpt != p->op && !ARE_MUTEX( c_e->endpt, p->op ) ) {
	if ( 0 )
	  printf("found op %s that adds cond %s of op %s\n", c_e->endpt->name,
		 (*next_facts)[i]->name, p->op->name );
	break;
      }
    if ( !c_e ) return FALSE;
  }

  return TRUE;

}


void put_pot_eff_in( pot_eff_list p, int time,
		     goal_array next_facts, int num )

{

  int i;
  edge_list conditions = NULL, temp;
  token_list i_token;
  vertex_list ft;

  for ( i=0; i<num; i++ ) {
    temp = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
    CHECK_MEMORY(temp);
    GRAPH(edge_list_elt);
    if ( next_facts[i]->prev_time ) {
      temp->endpt = next_facts[i]->prev_time;
    } else {
      temp->endpt = insert_into_table( fact_table[rifo_active_part][time], next_facts[i]->name );
      temp->endpt->is_dummy = TRUE;
      temp->endpt->next_time = next_facts[i];
      next_facts[i]->prev_time = temp->endpt;
    }
    temp->next = conditions;
    conditions = temp;
  }

  for( i_token = p->adds; i_token; i_token =i_token->next) {
    /* for each add effect do */
    ft = lookup_from_table( fact_table[rifo_active_part][time+1], i_token->item );
    if ( !ft ) continue;
    /* now ft is add effect vertex at step time+1:
     * connect the conditional edges with the
     * conditions of current effect
     */
    p->op->add_edges = 
      insert_cond_edge( p->op->add_edges,
			ft, conditions ); 
    if ( do_heuristic )
      ft->add_edges = 
	insert_sort_cond_edge( ft->add_edges, 
			       p->op, conditions );
      else
        ft->add_edges = 
	  insert_cond_edge( ft->add_edges, 
			    p->op, conditions );
  }
  for( i_token = p->dels; i_token; i_token =i_token->next) {
    /* for each del effect do */
    ft = lookup_from_table( fact_table[rifo_active_part][time+1], i_token->item );
    if ( !ft ) continue;
    /* now ft is add effect vertex at step time+1:
     * connect the conditional edges with the
     * conditions of current effect
     */
    p->op->del_edges = 
      insert_cond_edge( p->op->del_edges,
			ft, conditions ); 
    if ( do_heuristic )
      ft->del_edges = 
	insert_sort_cond_edge( ft->add_edges, 
			       p->op, conditions );
    else
      ft->del_edges = 
	insert_cond_edge( ft->add_edges, 
			  p->op, conditions );
  }

}
