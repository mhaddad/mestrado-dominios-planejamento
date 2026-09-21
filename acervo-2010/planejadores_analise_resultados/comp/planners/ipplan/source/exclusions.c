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
static char rcsid[] = "$Id: exclusions.c,v 1.2 1998/05/27 16:45:47 ipp Exp ipp $";
#endif /* lint */

/*
 * functions for calculating mutual exclusions:
 *   void find_mutex_ops_and_insert_del_edges( int ) ,
 *   pair find_mutex_facts( int ) ,
 *   void make_exclusive( vertex_list, vertex_list )
 * called in build_graph.c ,
 *   BOOLEAN are_mutex( vertex_list , vertex_list )
 * called in build_graph.c, util_build.c and search_plan.c
 *
 * calls insert_edge and insert_cond_edge from util_build.c
 */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */


/* marks given vertexes as being exclusive
 */
void make_exclusive( vertex_list v, vertex_list w )

{

  if ( ARE_MUTEX( v, w ) ) return;

  v->exclusive_vect[w->uid_block] |= w->uid_mask;
  w->exclusive_vect[v->uid_block] |= v->uid_mask;

}


/* finds all exclusive pairs of operators at time step <time>
 * and marks them as being exclusive;
 *
 * also inserts delete edges
 */
void find_mutex_ops_and_insert_del_edges( int time )

{

  /* help pointers; op: operator vertex, ft: fact vertex */
  vertex_list op, op_, ft2, ft1;

  edge_list i_e, j_e, k_e;/* indizes */
  cond_edge_list i_ce;/* index */
  delete_list i_del;/* index */
  
  int i;
  vertex_list o;

  /* for all operators at time step do */
  get_next( op_table[rifo_active_part][time], INIT );/* initialise */
  while ( ( op = get_next( op_table[rifo_active_part][time], EXEC ) ) != NULL ) {
    /* first mark all operators op_ that have a precondition which
     * is exclusive of one of op s preconditions:
     *   competing needs
     * NOTE: each pair of ops is hit twice, so call
     *       make_exclusive only one of these times for speedup
     */
    for ( i=0; i<HSIZE; i++ ) {
      for ( o = op_table[rifo_active_part][time][i]; o; o = o->next ) { 

	if ( ( int ) o < ( int ) op ) continue;
	for ( i_e = op->precond_edges; i_e; i_e = i_e->next ) {
	  for ( j_e = o->precond_edges; j_e; j_e = j_e->next ) 
	    if ( ARE_MUTEX( i_e->endpt, j_e->endpt ) ) break;
	  if ( j_e ) break;
	}
	if ( i_e )
	  make_exclusive( op, o );
      }
    }

    /* now handle deletes */
    for ( i_del = op->del_list; i_del; i_del = i_del->next ) {
      /* see if there actually is something to delete, i.e.
       * if the deleted fact is present at time+1
       */
      ft2 = lookup_from_table( fact_table[rifo_active_part][time+1], i_del->effect );

      /* no ? nothing to do
       * NOTE: fact can't be precondition of an operator at same
       *       time step, cause in that case, it would simply
       *       have to be in fact level time+1 by noop.
       */
      if ( !ft2 ) continue;

      /* otherwise: first connect delete edge */
      op->del_edges = insert_cond_edge( op->del_edges, ft2, i_del->conditions);
      ft2->del_edges = insert_cond_edge( ft2->del_edges, op,i_del->conditions);

      /* if it is an unconditional delete */
      if ( !i_del->conditions ) {
        /* mark all operators that have the deleted fact ( ft2 )
         * as a precondition
         * of course, that's only possible if ft2 was already there at
         * previous time step !
         */
        ft1 = ft2->prev_time;
        if ( ft1 ) {
          /* now mark the operators; leave out op itself */
          for ( i_e = ft1->precond_edges; i_e; i_e = i_e->next )
            if ( op != i_e->endpt ) make_exclusive( op, i_e->endpt );
        }

        /* finally, mark all the operators which have the deleted fact
         * as an unconditional add effect. again, don't mark op itself
         */
        for ( i_ce = ft2->add_edges; i_ce; i_ce = i_ce->next ) {
          if ( (!i_ce->conditions) && (op != i_ce->endpt) )
            make_exclusive( op, i_ce->endpt );
        }
      }
    }

    /* special handling of noop s: you need never include noop and any
     * operator that unconditionally adds it's ( the noop's ) effect
     * in the same plan
     */
    if ( op->is_noop ) {
      for ( i_ce = op->add_edges->endpt->add_edges; i_ce; i_ce = i_ce->next )
        if ( (!i_ce->conditions) && (op != i_ce->endpt) )
          make_exclusive( op, i_ce->endpt );
    }
  }

}


/* given two fact vertexes, look for any pair of effects that add them
 * with the following properties:
 *   - the ops are not exclusive ( or one op )
 *   - the effect conditions are not exclusive
 *   - the effect conditions are not exclusive of the other ops preconds
 * if at least one such pair is found, then the facts are not exclusive.
 *
 * new: a pair of ops, i.e, add effects is also not valid if there are
 * contradicting effects that will be made true under the effect conditions
 * i.e c => ADD a DEL b contradicts d => ADD a b ( if we want a to be true )
 * currently not active !
 *
 * NOTE: if both are added by the same operator op, there
 *       will eventually be examined the pair ( op, op ), which,
 *       of course, is not exclusive
 */
BOOLEAN facts_are_exclusive( vertex_list ft1, vertex_list ft2 )

{

  cond_edge_list i_ce, j_ce, h_ce, k_ce;/* indizes */
  edge_list i_e, j_e;/* indizes */
  vertex_list op1, op2;/* better readability */
  

  for ( i_ce = ft1->add_edges; i_ce; i_ce = i_ce->next ) {
    for ( j_ce = ft2->add_edges; j_ce; j_ce = j_ce->next ) {
      op1 = i_ce->endpt;
      op2 = j_ce->endpt;
      if ( !ARE_MUTEX( op1, op2 ) ) {
        /* found a pair of non mutex ops with those effects */
	for ( i_e = i_ce->conditions; i_e; i_e = i_e->next ) {
          /* see if the conditions are non mutex */
          for ( j_e = j_ce->conditions; j_e; j_e = j_e->next ) {
            if ( ARE_MUTEX( i_e->endpt, j_e->endpt ) ) break;
	  }
          if ( j_e ) break;
          /* now see if those conds are non mutex of the other preconds */
          for ( j_e = op2->precond_edges; j_e; j_e = j_e->next ) {
            if ( ARE_MUTEX( i_e->endpt, j_e->endpt ) ) break;
	  }
          if ( j_e ) break;
        }
        if ( i_e ) continue;/* one of the tests hit; look for different pair */

        /* now check the other way round */
        for ( i_e = op1->precond_edges; i_e; i_e = i_e->next ) {
          for ( j_e = j_ce->conditions; j_e; j_e = j_e->next ) {
            if ( ARE_MUTEX( i_e->endpt, j_e->endpt ) ) break;
	  }
          if ( j_e ) break;
        }
        if ( i_e ) continue;/* look for different pair */

	/* found a good pair of effects
	 *
	 * to use fact contradicting test, remove this return statement
	 * from code
	 */
	 return FALSE;

        /* now look for contradicting effects */
        for ( h_ce = op1->add_edges; h_ce; h_ce = h_ce->next ) {
	  /* for all add effects of op1 */
          if ( contains( i_ce->conditions, h_ce->conditions ) ) {
	    /* if they are made true */
	    for ( k_ce = op2->del_edges; k_ce; k_ce = k_ce->next ) {
	      /* lookup all delete effects of op2 */
              if ( contains( j_ce->conditions, k_ce->conditions ) ) {
		/* if they are made true */
                if ( h_ce->endpt == k_ce->endpt ) break;/* and identical */
	      }
	    }
	    if ( k_ce ) break;/* then break both loops */
	  }
	}
	if ( h_ce ) continue;/* and reject pair */

	/* now do the same thing the other way round: add effects of op2
	 * and delete effects of op1
	 */
	for ( h_ce = op2->add_edges; h_ce; h_ce = h_ce->next ) {
          if ( contains( j_ce->conditions, h_ce->conditions ) ) {
	    for ( k_ce = op1->del_edges; k_ce; k_ce = k_ce->next ) {
              if ( contains( i_ce->conditions, k_ce->conditions ) ) {
                if ( h_ce->endpt == k_ce->endpt ) break;
	      }
	    }
	    if ( k_ce ) break;
	  }
	}
	if ( h_ce ) continue;

        /* found a good pair of effects */
        return FALSE;
      }
    }
  }

  return TRUE;

}


/* helpfunction for facts_are_exclusive; returns TRUE iff all edges
 * in l2 are contained in l1
 */
BOOLEAN contains( edge_list l1, edge_list l2 ) 

{

  edge_list i_e, j_e;

  for ( i_e = l2; i_e; i_e = i_e->next ) {
    for ( j_e = l1; j_e; j_e = j_e->next ) {
      if ( i_e->endpt == j_e->endpt ) break;/* found a matching edge */
    }
    if ( !j_e ) break;/* didnt find one */
  }

  return i_e == NULL ? TRUE : FALSE;/* did we do all edges in l2 ? */

}


/* finds all exclusive pairs of facts at time step <time>
 * and marks them as being so.
 */
pair find_mutex_facts( int time )

{

  /* statics for getting array to load complete fact_table */
  static BOOLEAN initialise = TRUE;
  static vertex_list *ft;

  pair result;/* return value */
  int i, j, fcount = 0, ecount = 0;/* i, j indizes, counts for ret value */
  edge_list i_e;/* index */
  vertex_list ft_, f;/* help pointer to fact vertex */

  /* get memory for fact array */
  if ( initialise ) {
    ft = ( vertex_list * ) calloc( max_nodes, sizeof( vertex_list ) );
    CHECK_MEMORY(ft);
    initialise = FALSE;
  }

  /* load fact table into array */
  get_next( fact_table[rifo_active_part][time], INIT );
  for ( i=0; ( ft[i] = get_next( fact_table[rifo_active_part][time], EXEC ) ) != NULL; i++ );
  fcount = i;

  /* check all facts */
  for ( i=0; ft[i] != NULL; i++ ) {
    if ( !ft[i]->prev_time ) {
      /* new fact; check against all others */
      for ( j=0; ft[j] != NULL; j++ ) {
        if ( !ft[j]->prev_time && j <= i ) continue;/* already had this pair */
        if ( facts_are_exclusive( ft[i], ft[j] ) ) {
          ecount++;/* ecount counts the exclusion relations */
          make_exclusive( ft[i], ft[j] );
        }
      }
    } else {
      /* old fact; only check against old exclusives */
      for (j = 0; j<HSIZE; j++ ) {
	for ( f = fact_table[rifo_active_part][time-1][j]; f; f = f->next ) {
	  if ( f == ft[i]->prev_time ||
	       (int) f < (int) ft[i]->prev_time ) continue;
	  if ( !ARE_MUTEX( f, ft[i]->prev_time ) ) continue;
	  if ( facts_are_exclusive( f->next_time, ft[i] ) ) {
	    ecount++;
	    make_exclusive( f->next_time, ft[i] );
	  }
	}
      }
    }
  }

  /* if #facts and #exclusions is the same as it was previous time
   * ( see build_graph_layer ), the graph has leveled off.
   */
  result.first = fcount;
  result.second = ecount;

  return result;

}
