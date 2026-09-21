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


#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

/* the setting up function; called by main
 * simply sets up search and does the initial call
 * as well as memoizing the result if search was a failure
 */
BOOLEAN search_plan( int max_time )

{

  int i;
  BOOLEAN result;
  vertex_list ft;
  token_list it;

  expand( max_time );

  /* say that the facts in initial level are true already */
  get_next( fact_table[rifo_active_part][0], INIT );
  while ( ( ft = get_next( fact_table[rifo_active_part][0], EXEC ) ) != NULL )
    ft->is_true = 1;

  /* setup the goal array at max time: lookup global 
   * goal strings from fact_table[max time]
   */
  num_goals_at[max_time] = 0;
  for ( it = goal_facts; it; it = it->next ) {
    ft = lookup_from_table( fact_table[rifo_active_part][max_time], it->item );
    goals_at[max_time][num_goals_at[max_time]++] = ft;
    ft->is_goal = 1;
    if ( num_goals_at[max_time] > MAX_GOALS ) {
      printf( "\n\nipp: increase MAX_GOALS( preset value: %d )", MAX_GOALS );
      OUTPUT_FILE;
      exit( 1 );
    }
  }
  /* and the critic array at max time, which is empty */
  num_critics_at[max_time] = 0;

  num_ops_at[max_time-1] = 0;
  num_goals_at[max_time-1] = 0;

  /* try to find a plan */
  result = search( num_goals_at[max_time] - 1, max_time );

  /* undo goal info */
  for ( i=0; i < num_goals_at[max_time]; i++ ) goals_at[max_time][i]->is_goal = 0;
 
  /* if it was a failure, memoize that */
  if ( !result )  memoize( max_time,
                           goals_at[max_time], num_goals_at[max_time],
                           critics_at[max_time], 0 );

  /* and tell main what we found */
  return result;

}


BOOLEAN search( int curr_index, int time )

{

  cond_edge_list i_ce;/* index for current chosen add edge */
  vertex_list op, ft;/* helpers */

  /* don't have to make goals at initial level true,
   * cause they are. we found a plan.
   */
  if ( time == 0 ) return TRUE;

  /* all ops for making goals true are chosen.
   * 
   * do some more computation and go on to next level.
   */
  if ( curr_index < 0 ) {

    /* the minimality check; see if there's an op that we can leave out
     * of the plan, i.e., that doesn't add a goal alone;
     *
     */
    if ( !action_set_is_minimal( time ) ) return FALSE;

    num_SS_at[time-1] = 0;
    return  prevent_critics_and_search( num_critics_at[time]-1, time );

  }

  /* skip over any goals that have been made true just by luck
   * by any op we've chosen already: is_true value > 0
   */
  while ( ( ft = goals_at[time][curr_index] )->is_true ) {
    curr_index--;
    if ( curr_index < 0 ) {
      return search( -1, time );
    }
  }

  /* try all possibilities of making that fact true */
  for ( i_ce = ft->add_edges; i_ce; i_ce = i_ce->next ) { 

    /* try to put op into plan */
    op = i_ce->endpt;
    if ( !try_op( op, i_ce->conditions, curr_index, time) )
      continue;

    /* try making the remaining goals true */
    if ( search( curr_index - 1, time ) )
      return TRUE;
    
    /* didn't manage: put op out of plan and try next one */
    untry_op( op, i_ce->conditions, time );

  }

  /* tried all add edges for fact without success: return FALSE */
  return FALSE;

}


BOOLEAN prevent_critics_and_search( int curr_index, int time )

{

  int i;
  vertex_list ft, noop, op;
  cond_edge_list i_ce;
  BOOLEAN found_critics;
  BOOLEAN param;

  for ( i = curr_index; i>-1; i-- ) {
    ft = critics_at[time][i];
    if ( cant_do_ft( ft, time ) ) continue;
    noop = ft->my_noop;
    if ( !noop ) continue;
    if ( !cant_do_op( noop, time-1 ) ) {
      if ( !(ft->prev_time->is_goal) ) {

	if ( num_SS_at[time-1] == MAX_SS ) {
	  printf("\ntoo many condition lists in SS. increase MAX_SS\n\n");
	  OUTPUT_FILE;
	  exit( 1 );
	}

	SS_at[time-1][num_SS_at[time-1]].goals[0] = ft->prev_time;
	SS_at[time-1][num_SS_at[time-1]].goals[1] = NULL;
	SS_at[time-1][num_SS_at[time-1]].op = noop;
	num_SS_at[time-1]++;

	if ( prevent_critics_and_search( i-1, time ) )
	  return TRUE;

	SS_at[time-1][--num_SS_at[time-1]].goals[0] = NULL;
	SS_at[time-1][num_SS_at[time-1]].op = NULL;

      }
      
      for ( i_ce = ft->del_edges; i_ce; i_ce = i_ce->next ) {
	op = i_ce->endpt;
	if ( !op->is_used ) continue;
	
	if ( !try_op( op, i_ce->conditions, curr_index, time ) )
	  continue;
	
	if ( prevent_critics_and_search( i-1, time ) )
	  return TRUE;
	
	untry_op( op, i_ce->conditions, time );
      }
      
      for ( i_ce = ft->del_edges; i_ce; i_ce = i_ce->next ) {
	op = i_ce->endpt;
	if ( op->is_used ) continue;
	
	if ( !try_op( op, i_ce->conditions, curr_index, time ) )
	  continue;
	
	if ( prevent_critics_and_search( i-1, time ) )
	  return TRUE;
	
	untry_op( op, i_ce->conditions, time );
      }
      
      /* all attempts to prevent this critic have failed
       */
      return FALSE;
    }
  }
  
  /* empty goal sets on non initial levels dont make sense
   */
  if ( time > 1 && num_goals_at[time-1] == 0 ) {
    printf("\nipp: empty goal set on non initial level encountered\n\n");
    OUTPUT_FILE;
    exit( 1 );
  }
  
  compute_SS( time ); 
  
  if ( time == 1 && !each_list_contains_dummy() ) return FALSE;
  
  for ( found_critics = choose_critics( time, INIT );
	found_critics;
	found_critics = choose_critics( time, EXEC) ) {
    
    if ( num_SS_at[time-1] > 0 )
      param = COMPLETE;
    else
      param = SEARCH;

    if ( complete_critics_and_search( param, time ) )
      return TRUE;
    
  }
  
  /* tried all possibilities without success: return FALSE */
  return FALSE;

}


BOOLEAN complete_critics_and_search( BOOLEAN mode, int time )

{

  int i, j;
  edge_list i_e;
  cond_edge_list i_ce;
  vertex_list op,ft;
  
  if ( mode == SEARCH ) {
 
    if ( num_goals_at[time-1] > 0 &&
	 memoized( goals_at[time-1], num_goals_at[time-1],
		   critics_at[time-1], num_critics_at[time-1] ) ) {
      return FALSE;
    }

    if ( time > 1 ) {
      num_ops_at[time-2] = 0;
      num_goals_at[time-2] = 0;
    }
	
    if ( search( num_goals_at[time-1] - 1, time - 1 ) ) return TRUE;

    memoize( time-1,
	     goals_at[time-1], num_goals_at[time-1],
	     critics_at[time-1], num_critics_at[time-1] );
    return FALSE;

  } else {

    /* for all used ops do */
    for ( i=0; i<num_ops_at[time-1]; i++ ) {
      op = ops_at[time-1][i];
      /* for all add edges do */
      for ( i_ce = op->add_edges; i_ce; i_ce = i_ce->next ) {
	ft = i_ce->endpt->prev_time;
	if ( !ft || !ft->is_critic ) continue;
        /* the fact is a new critic */
	if ( !i_ce->conditions ) {
          /* we add it unconditionally */
	  for ( j=0; j<ft->is_critic; j++ )
            if ( (ft->is_critic_for)[j] != op ) break;
          if ( j<ft->is_critic ) {
            /* it was someone else's critic
             */
	    return FALSE;
	  }
	} else {
          /* it is a conditional effect */

          /* if we already prevent this effect, there's nothing to do */
	  for ( i_e = i_ce->conditions; i_e; i_e = i_e->next )
	    if ( i_e->endpt->is_critic ) break;
	  if ( i_e ) continue;

          /* check if it's someone else's critic */
	  for ( j=0; j<ft->is_critic; j++ )
            if ( (ft->is_critic_for)[j] != op ) break;
          if ( j<ft->is_critic ) {

            /* put conditions into new critics one after the other */
	    for ( i_e = i_ce->conditions; i_e; i_e = i_e->next ) {
	      if ( i_e->endpt->is_goal ) continue;
	      critics_at[time-1][num_critics_at[time-1]++] = i_e->endpt;
	      i_e->endpt->is_critic++;
	      (i_e->endpt->is_critic_for)[i_e->endpt->is_critic-1] = op;

              /* try to find a plan with these new critics, i.e.,
               * first finish completion pattern.
               */
	      if ( complete_critics_and_search( COMPLETE, time ) )
                return TRUE;
              
              /* failed: put the critic out and try next one */
	      (i_e->endpt->is_critic_for)[i_e->endpt->is_critic--] = NULL;
	      critics_at[time-1][--num_critics_at[time-1]] = NULL;
	    }

            /* tried all possibilities without success: return FALSE */
	    return FALSE;
	  }
	}
      }
    }/* matches for all used ops do */

    /* we didn't have to add a new critic: we are finished with completing */
    return complete_critics_and_search( SEARCH, time );

  }

}


/* this one checks if a new op can be put into the plan, i.e.
 * if it's not exclusive of any other chosen op etc.
 */
BOOLEAN try_op( vertex_list op, edge_list conditions,
        	int curr_index, int time )

{

  edge_list i_e, j_e;/* indizes */
  cond_edge_list i_ce;/* index */
  int was_used;/* to tell if a fact was already there */
  vertex_list ft_;/* helper */

  /* see if op is marked as being exclusive */
  if ( cant_do_op( op, time-1 ) ) return FALSE; 

  /* if we don't use this op yet */
  if ( !op->is_used ) {
    /* see if it unconditionally adds a critic */
    for ( i_ce = op->add_edges; i_ce; i_ce = i_ce->next )
      if ( !i_ce->conditions && i_ce->endpt->is_critic ) break;
    if ( i_ce ) return FALSE;

    for ( i_ce = op->del_edges; i_ce; i_ce = i_ce->next ) {
      if ( i_ce->conditions ) continue;
      ft_ = i_ce->endpt;
      if( ft_->is_goal ) break;
      if( ft_->prev_time && ft_->prev_time->is_goal ) break;
    }
    if ( i_ce ) return FALSE;

    if ( !goals_still_possible( curr_index, time, op ) ) {
      return FALSE;
    }
  }

  for ( i_e = op->precond_edges; i_e; i_e = i_e->next ) {
    if ( cant_do_ft(i_e->endpt, time - 1 ) ) {
      return FALSE;
    }
  }

  for ( i_e = conditions; i_e; i_e = i_e->next ) {
    if ( cant_do_ft(i_e->endpt, time - 1 ) ||
	 is_deleted( i_e->endpt, time, op ) ||
	 i_e->endpt->is_dummy ) {
      return FALSE;
    }
  }

  /* now it's clear that we can put the op into the plan */

  /* mark the op and put it into the global array */
  was_used = op->is_used++;
  if ( !was_used && num_ops_at[time-1] == MAX_GOALS ) {
    printf( "\n\nipp: increase MAX_GOALS( preset value: %d )",MAX_GOALS );
    OUTPUT_FILE;
    exit( 1 );
  }
  if( !was_used ) {
    ops_at[time-1][num_ops_at[time-1]++] = op;
    num_of_actions_tried++;
  }

  /* also put the preconditions into goal array at time - 1 */
  for ( i_e = op->precond_edges; i_e; i_e = i_e->next ) {
    was_used = i_e->endpt->is_goal++;
    if ( ( !was_used && num_goals_at[time-1] == MAX_GOALS ) ||
	 i_e->endpt->is_goal > MAX_GOALS ) {
      printf( "\n\nipp: increase MAX_GOALS( preset value: %d )", MAX_GOALS );
      OUTPUT_FILE;
      exit( 1 );
    }
    (i_e->endpt->is_goal_for)[i_e->endpt->is_goal-1] = op;
    if ( !was_used ) goals_at[time-1][num_goals_at[time-1]++] = i_e->endpt;
  }

  /* ... and the effect conditions 
   *
   * NOTE: only put goals into the array that aren't already there
   */
  for ( i_e = conditions; i_e; i_e = i_e->next ) {
    was_used = i_e->endpt->is_goal++;
    if ( ( !was_used && num_goals_at[time-1] == MAX_GOALS ) ||
	 i_e->endpt->is_goal > MAX_GOALS ) {
      printf( "\n\nipp: increase MAX_GOALS( preset value: %d )", MAX_GOALS ); 
      OUTPUT_FILE;
      exit( 1 );
    }
    (i_e->endpt->is_goal_for)[i_e->endpt->is_goal-1] = op;
    if ( !was_used ) goals_at[time-1][num_goals_at[time-1]++] = i_e->endpt;
  }

  /* now mark the facts that will be true for sure as being so
   * ( used for speedup ( skip over goals ) and in minimality check )
   */
  for ( i_ce = op->add_edges; i_ce; i_ce = i_ce->next )
    if ( !i_ce->conditions ) i_ce->endpt->is_true++;
  
  /* and say we managed */
  return TRUE;
  
}


/* this one simply puts an op out of the plan, i.e.
 * undoes the information in the graph and the global arrays
 */
void untry_op( vertex_list op, edge_list conditions, int time )

{

  edge_list i_e;
  cond_edge_list i_ce;
  int was_used;

  /* undo is true info */
  for ( i_ce = op->add_edges; i_ce; i_ce = i_ce->next )
    if ( !i_ce->conditions ) i_ce->endpt->is_true--;

  /* put the effect conditions out of the new-goal array */
  for ( i_e = conditions; i_e; i_e = i_e->next ) {
    was_used = --i_e->endpt->is_goal;
    (i_e->endpt->is_goal_for)[i_e->endpt->is_goal] = NULL;
    if ( !was_used ) goals_at[time-1][--num_goals_at[time-1]] = NULL;
  }

  /* same for the preconds */
  for ( i_e = op->precond_edges; i_e; i_e = i_e->next ) {
    was_used = --i_e->endpt->is_goal;
    (i_e->endpt->is_goal_for)[i_e->endpt->is_goal] = NULL;
    if ( !was_used ) goals_at[time-1][--num_goals_at[time-1]] = NULL;
  }

  /* and, finally, remove the op from the plan */
  was_used = --op->is_used;
  if( !was_used ) ops_at[time-1][--num_ops_at[time-1]] = NULL;

}


/* routine for building up SS, the 'Set of Set'
 *
 * look for bad conditional effects of the used ops 
 * and put their condition lists( without the new goals )
 * into the return list of edge list
 *
 * NOTE: SS can be non-empty, we just add new lists to those
 *       which are already there.
 */
void compute_SS( int time )

{

  cond_edge_list i_ce;/* index */
  edge_list l;
  int i, j;/* inidizes */
  vertex_list op, ft;/* helpers */

  /* for all ops at time step time-1 do */
  for ( i=0; i<num_ops_at[time-1]; i++ ) {
    op = ops_at[time-1][i];
    /* for all conditional del effects */
    for ( i_ce = op->del_edges; i_ce; i_ce = i_ce->next ) {
      if ( i_ce->conditions ) {
        ft = i_ce->endpt;
        /* if goal is deleted */
        if ( ft->is_goal ||
           ( ft->prev_time && ft->prev_time->is_goal ) ) {

          /* if it is a new goal: see if it's the goal of someone else */     
          if ( !ft->is_goal ) {
            ft = ft->prev_time;
            for ( j=0; j<ft->is_goal; j++ )
              if ( (ft->is_goal_for)[j] != op ) break;
            if ( j == ft->is_goal ) continue;
	  }

	  if ( num_SS_at[time-1] == MAX_SS ) {
	    printf("\ntoo many condition lists in SS. increase MAX_SS\n\n");
	    OUTPUT_FILE;
	    exit( 1 );
	  }
	  j = 0;
	  for ( l = i_ce->conditions; l; l = l->next ) {
	    if ( l->endpt->is_goal ) continue;
	    SS_at[time-1][num_SS_at[time-1]].goals[j++] = l->endpt;
	    if ( j == MAX_GOALS ) {
	      printf("\nipp: increase MAX_GOALS\n\n");
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  }
	  SS_at[time-1][num_SS_at[time-1]].goals[j] = NULL;
	  SS_at[time-1][num_SS_at[time-1]++].op = ops_at[time-1][i];
        }
      }
    }
    /* for all conditional add effects */
    for ( i_ce = ops_at[time-1][i]->add_edges; i_ce; i_ce = i_ce->next ) {
      if ( i_ce->conditions ) {
        if ( i_ce->endpt->is_critic ) {

	  if ( num_SS_at[time-1] == MAX_SS ) {
	    printf("\ntoo many condition lists in SS. increase MAX_SS\n\n");
	    OUTPUT_FILE;
	    exit( 1 );
	  }
	  j = 0;
	  for ( l = i_ce->conditions; l; l = l->next ) {
	    if ( l->endpt->is_goal ) continue;
	    SS_at[time-1][num_SS_at[time-1]].goals[j++] = l->endpt;
	    if ( j == MAX_GOALS ) {
	      printf("\nipp: increase MAX_GOALS\n\n");
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  }
	  SS_at[time-1][num_SS_at[time-1]].goals[j] = NULL;
	  SS_at[time-1][num_SS_at[time-1]++].op = ops_at[time-1][i];
        }
      }
    }
  }

}


/* this one chooses a 'hitting set' out of SS, i.e. one fact from
 * each edge list; is called in search as a for - next loop:
 * first call with 3rd argument = INIT to initialise the choice,
 * then continue calling with 3rd argument = EXEC until
 * the return value is FALSE.
 */
BOOLEAN choose_critics( int time, BOOLEAN initialise )

{

  static int index[MAX_PLAN][MAX_SS];

  int i;
  vertex_list ft;

  /* is it the first call on this SS ? */
  if ( initialise ) {

    for ( i=0; i<num_SS_at[time-1]; i++ )
      if ( SS_at[time-1][i].goals[0] == NULL ) return FALSE;

    for ( i=0; i<num_SS_at[time-1]; i++ ) 
      index[time-1][i] = 0;

  } else {

    for ( i=0; i<num_SS_at[time-1]; i++ ) {
      ft = SS_at[time-1][i].goals[index[time-1][i]];
      (ft->is_critic_for)[--ft->is_critic] = NULL;
    }

    for ( i=0; i<num_SS_at[time-1]; i++ ) {
      index[time-1][i]++;
      if ( SS_at[time-1][i].goals[index[time-1][i]] == NULL ) {
	index[time-1][i] = 0;
      } else {
	break;
      }
    }
    if ( i == num_SS_at[time-1] ) return FALSE;

  }

  num_critics_at[time-1] = 0;
  for ( i=0; i < num_SS_at[time-1]; i++ ) {
    ft = SS_at[time-1][i].goals[index[time-1][i]];
    (ft->is_critic_for)[ft->is_critic++] = SS_at[time-1][i].op;
    if ( ft->is_critic == 1 ) {
      if ( num_critics_at[time-1] == MAX_GOALS ) {
	printf( "\n\nipp: increase MAX_GOALS( preset value: %d )",MAX_GOALS );
	OUTPUT_FILE;
	exit( 1 );
      }
      critics_at[time-1][num_critics_at[time-1]++] = ft;
    }
  }

  return TRUE;

}
