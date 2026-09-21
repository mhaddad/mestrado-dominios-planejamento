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
static char rcsid[] = "$Id: util_search.c,v 1.1 1998/05/25 08:16:55 ipp Exp ipp $";
#endif /* lint */

/*
 * some helpers for searching
 */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

void expand( int max_time )

{

  /* this stores goals at each time step */
  if ( goals_at != NULL ) free( goals_at );
  goals_at = ( goal_array * ) calloc( max_time + 1, sizeof( goal_array ) );
  CHECK_MEMORY(goals_at);
  if ( num_goals_at != NULL ) free( num_goals_at );
  num_goals_at = ( int * ) calloc( max_time + 1, sizeof( int ) );
  CHECK_MEMORY(num_goals_at);

  /* this stores the ops */
  if ( ops_at != NULL ) free( ops_at );
  ops_at = ( goal_array * ) calloc( max_time, sizeof( goal_array ) );
  CHECK_MEMORY(ops_at);
  /* also need to know how many there are */
  if ( num_ops_at != NULL ) free( num_ops_at );
  num_ops_at = ( int * ) calloc( max_time, sizeof( int ) );
  CHECK_MEMORY(num_ops_at);

  /* this stores the critics */
  if ( critics_at != NULL ) free( critics_at );
  critics_at = ( goal_array * ) calloc( max_time + 1, sizeof( goal_array ) );
  CHECK_MEMORY(critics_at);
  /* and their number */
  if ( num_critics_at != NULL ) free( num_critics_at );
  num_critics_at = ( int * ) calloc( max_time + 1, sizeof( int ) ); 
  CHECK_MEMORY(num_critics_at);

  if ( SS_at != NULL ) free( SS_at );
  SS_at = ( SS_at_type * ) calloc( max_time + 1, sizeof( SS_at_type ) );
  CHECK_MEMORY(SS_at);
  if ( num_SS_at != NULL ) free( num_SS_at );
  num_SS_at = ( int * ) calloc( max_time + 1, sizeof( int ) ); 
  CHECK_MEMORY(num_SS_at);

}


/* says if the successor of a fact ft is unconditionally deleted
 * by a chosen op at time - 1 other than op_
 *
 * ( this is used in choosing ops: see if an effect condition is
 *   being deleted by an already chosen parallel op )
 */
BOOLEAN is_deleted( vertex_list ft, int time, vertex_list op_ )

{

  cond_edge_list i_ce;
  int i;

  /* for all chosen ops at time - 1 do */
  for ( i=0; i<num_ops_at[time-1]; i++ ) {
    if( ops_at[time-1][i] == op_ ) continue;
    /* if op != op_ 
     * for all del edges of op do
     */
    for ( i_ce = ops_at[time-1][i]->del_edges; i_ce; i_ce = i_ce->next )
      /* if it unconditionally deletes the ft at next time,
       * return TRUE
       */
      if ( !i_ce->conditions && 
           i_ce->endpt->prev_time == ft ) return TRUE;
  }

  return FALSE;

}


/* says if a future goal has been cut off:
 * check all goals at time from 0 to max index n
 * if one of the ops making it true is still possible
 * ( given the choice of our so far used ops )
 * if there is no such op for one goal, we return false.
 */
BOOLEAN goals_still_possible( int n, int time, vertex_list op )

{

  int i, j;
  static int e[NUMINTS];
  cond_edge_list i_ce;

  for ( i=0; i<num_ints; i++ ) {
    e[i] &= 0;
    for ( j=0; j<num_ops_at[time-1]; j++ ) {
      e[i] |= ops_at[time-1][j]->exclusive_vect[i];
    }
    e[i] |= op->exclusive_vect[i];
  }

  /* for all future goals do */
  for ( i=0; i<n; i++ ){
    /* for all add edges do */
    for ( i_ce = goals_at[time][i]->add_edges; i_ce; i_ce = i_ce->next )
      if ( ( ( e[i_ce->endpt->uid_block] ) & ( i_ce->endpt->uid_mask ) ) == 0 )
	break;/* found a good one */
    if ( !i_ce ) return FALSE;
  }

  return TRUE;

} 


/* this is the minimality check:
 * see if there is an operator that we don't actually need.
 *
 * first increment the is true values of all facts that are
 * made true by a conditional effect of a used operator where
 * the effect conditions are completely contained in the new goals
 * ( the unconditional is true values are already set during 
 *   operator set setup in search )
 * then see for each op if there is a goal which he is the only
 * one to make true.
 * if we find an op that doesn't do so, return FALSE.
 */
BOOLEAN action_set_is_minimal( int time )

{

  int i;
  edge_list i_e;
  cond_edge_list i_ce;
  BOOLEAN result = TRUE;

  /* for all used ops do */
  for ( i=0; i<num_ops_at[time-1]; i++ ) 
    /* for all add effects do */
    for ( i_ce = ops_at[time-1][i]->add_edges; i_ce; i_ce = i_ce->next )
      /* if effect is conditional */
      if ( i_ce->conditions ) {
        /* for all conditions do */
        for ( i_e = i_ce->conditions; i_e; i_e = i_e->next )
          if ( !i_e->endpt->is_goal ) break;/* found a bad one */
        if ( !i_e ) i_ce->endpt->is_true++;
      }

  /* for all used ops do */
  for ( i=0; i<num_ops_at[time-1]; i++ ) {
    /* for all add effects do */
    for ( i_ce = ops_at[time-1][i]->add_edges; i_ce; i_ce = i_ce->next ) {
      if ( !i_ce->endpt->is_goal ) continue;/* not a goal */
      if ( i_ce->endpt->is_true == 1 ) break;/* good op */
    }
    if( !i_ce ) {/* didn't need that one */
      result = FALSE;
      break;
    }
  }

  /* undo the is true changings that we made cause we need them
   * in the search recursion pattern
   */
  for ( i=0; i<num_ops_at[time-1]; i++ ) 
    for ( i_ce = ops_at[time-1][i]->add_edges; i_ce; i_ce = i_ce->next )
      if ( i_ce->conditions ) {
        for ( i_e = i_ce->conditions; i_e; i_e = i_e->next )
          if ( !i_e->endpt->is_goal ) break;
        if ( !i_e ) i_ce->endpt->is_true--;
      }

  /* and return the result */
  return result;

}


/* this is the routine that prints the actual output
 * of the whole thing to stdout
 */
void print_plan( int time ) 

{

  vertex_list op;/* helper */

  int i, j;/* index for time */
  BOOLEAN first;/* for better printing: is it the first one this level? */

  printf( "\nipp: found plan as follows\n\n" );

  /* for all non empty operator levels */
  for ( i=0; i<time; i++ ) {
    printf("time step %3d: ", i);
    first = TRUE;
    /* for all operators in plan */
    for ( j=0; j<num_ops_at[i]; j++ ) {
      op = ops_at[i][j];
      if ( op->is_noop ) continue;/* don't print noops */
      if ( first ) {
	printf("%s\n", op->name );
	first = FALSE;
      } else {
	printf( "               %s\n", op->name );
      }
    }
  }

  printf( "\n" );

}


BOOLEAN each_list_contains_dummy( void )

{

  int i, j;

  for ( i = 0; i < num_SS_at[0]; i++ ) {
    for ( j=0; SS_at[0][i].goals[j] != NULL; j++ )
      if ( SS_at[0][i].goals[j]->is_dummy ) break;
    if ( SS_at[0][i].goals[j] == NULL ) return FALSE;
  }

  return TRUE;

}


BOOLEAN cant_do_op( vertex_list op, int time )

{

  int i;

  if ( op->is_used ) return FALSE;

  for ( i=0; i<num_ops_at[time]; i++ ) {
    if ( ARE_MUTEX( ops_at[time][i], op ) ) return TRUE;
  }

  return FALSE;

}


BOOLEAN cant_do_ft( vertex_list ft, int time )

{

  int i;

  if ( ft->is_goal ) return FALSE;

  for ( i=0; ( goals_at[time][i] != NULL ); i++ ) {
    if ( ARE_MUTEX( goals_at[time][i], ft ) ) return TRUE;
  }

  return FALSE;

}
