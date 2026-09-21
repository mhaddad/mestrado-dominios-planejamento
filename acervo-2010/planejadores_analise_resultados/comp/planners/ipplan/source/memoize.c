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
static char rcsid[] = "$Id: memoize.c,v 1.1 1998/05/25 08:16:55 ipp Exp ipp $";
#endif /* lint */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */


/* do you understand that one ? 
 */
int min( int a, int b )

{

  return ( a < b ) ? a : b;

}


void memoize( int time, goal_array goals, int num_goals,
                        goal_array critics, int num_critics )

{ 

  int i;/* helpers */
  node_list node;/* stores our current node in the tree */
  vertex_list ft;
  static goal_array sort_goals;/* help array */
  static BOOLEAN first_call = TRUE;/* flag */
  int way = num_goals + num_critics;/* contains size of remaining path */

  /* get memory on first call */
  if ( first_call ) {
    for ( i=0; i<MAX_GOALS; i++ ) {
	sort_goals[i] = ( vertex_list ) calloc( 1, sizeof( vertex_list_elt ) );
	CHECK_MEMORY(sort_goals[i]);
    }
    first_call = FALSE;
  }

  if ( num_goals == 0 ) {
    return;
  } 

  /* have to copy over the facts relevant for memoizing into new array
   * cause we're going to order the goal array, and as it
   * consists of pointers this would change the goals_at info,
   * which would cause a good deal of confusion in the recursive
   * search algorithm
   */
  for ( i=0; i<num_goals; i++ ) {
    sort_goals[i]->hashval = goals[i]->hashval;
    sort_goals[i]->uid_block = goals[i]->uid_block;
    sort_goals[i]->uid_mask = goals[i]->uid_mask;
    sort_goals[i]->memonum = i;
  }

  /* now order the goals and critics
   */
  quicksort( sort_goals, 0, num_goals - 1 );
  quicksort( critics, 0, num_critics - 1 );

  ft = sort_goals[0];
  node = (goals[ft->memonum])->memo_start;

  if ( !node ) {
    /* we dind't find this goal; create a new entry here */
    node = ( node_list ) calloc( 1, sizeof( node_list_elt ) );
    MEMO(node_list_elt);
    CHECK_MEMORY(node);
    node->hashval = ft->hashval;
    node->uid_block = ft->uid_block;
    node->uid_mask = ft->uid_mask;
    node->goals = NULL;
    node->critics = NULL;
    node->min_way = --way;
    node->next = NULL;
    (goals[ft->memonum])->memo_start = node;
  } else {
    node->min_way = min( node->min_way, --way );
  }

  /* now we have the beginning of our remaining goal tree in node */
  for ( i=1; i<num_goals; i++ ) {
    /* work through all remaining goals */    
    ft = sort_goals[i];
    if ( !node->goals ) {
      /* at this point in the tree we didn't have goal branches yet;
       * get memory for the goal table
       */
      node->goals = ( node_table * ) calloc( 1, sizeof( node_table ) );
      MEMO(node_table);
      CHECK_MEMORY(node->goals);
    }

    /* now insert our goal into the goal table and let node be
     * the new node where that leads us.
     *
     * NOTE: if the goal is already there, then the return value of
     *       sub_insert is a pointer to the adress of the already
     *       existing node
     */
    node = sub_insert( node->goals,
		       ft->hashval, ft->uid_block, ft->uid_mask );
    node->min_way = min( node->min_way, --way );
  }
  for ( i=0; i<num_critics; i++ ) {
    /* now we do just the same thing for the critics */
    ft = critics[i];
    if ( !node->critics ) {
      node->critics = ( node_table * ) calloc( 1, sizeof( node_table ) );
      MEMO(node_table);
      CHECK_MEMORY(node->critics);
    }
    node = sub_insert( node->critics,
		       ft->hashval, ft->uid_block, ft->uid_mask );
    node->min_way = min( node->min_way, --way );
  }

  free_sub_tree( node );

  /* for completness check: count the number of stored sets
   * at first level off time;if it stays the same
   * at a time step after same_as_prev_flag, then 
   * problem is unsolvable.
   *
   * you don't believe that ? ask jana koehler or the guys 
   *                          who wrote graphplan.
   */
  if ( same_as_prev_flag && time == first_full_time ) current_Scount++;

}


BOOLEAN memoized( goal_array goals, int num_goals,
		  goal_array critics, int num_critics )

{

  int i;/* indizes */
  node_list node;/* our current tree node */
  vertex_list ft;/* helper */
  /* need an extra array for sorted goals, same as in memoize, see above */
  static goal_array sort_goals;
  static BOOLEAN first_call = TRUE;

  if ( first_call ) {
    for ( i=0; i<MAX_GOALS; i++ ) {
      sort_goals[i] = ( vertex_list ) calloc( 1, sizeof( vertex_list_elt ) );
      CHECK_MEMORY(sort_goals[i]);
    }
    first_call = FALSE;
  }

  if ( num_goals == 0 ) {
    return FALSE;
  } 

  for ( i=0; i<num_goals; i++ ) {
    sort_goals[i]->hashval = goals[i]->hashval;
    sort_goals[i]->uid_block = goals[i]->uid_block;
    sort_goals[i]->uid_mask = goals[i]->uid_mask;
    sort_goals[i]->memo_start = goals[i]->memo_start;
  }

  quicksort( sort_goals, 0, num_goals - 1 );
  quicksort( critics, 0, num_critics - 1 );

  /* this is the 'normal' memoising check */
  if ( straight_memoized( sort_goals, 0, num_goals,
			  critics, num_critics) ) {
    simple_hits++;
    return TRUE;
  }

  if ( !do_subset ) return FALSE;

  /* do subset is set; first do a kind of partial check: start normal
   * memoising from goal 2 to goal num_goals - 1, if we then hit
   * a null_critics++, we found a subset
   */
  for ( i=1; i<num_goals; i++ ) {
    if ( straight_memoized( sort_goals, i, num_goals,
			    critics, num_critics) ) {
      partial_hits++;
      return TRUE;
    }
  }

  /* now it's time for the real subset check:
   * try to look up one goal after the other, if we found one, search the tree
   * and continue with the remaining goals if search failed.
   */
  for ( i=0; i<num_goals; i++ ) {
    ft = sort_goals[i];
    node = ft->memo_start;
    if ( !node ) continue;
    if ( node->min_way > num_goals - i - 1 + num_critics ) continue;
    if ( sub_memoized( sort_goals, num_goals, i + 1,
		       critics, num_critics, 0,
		       node ) ) {
      subset_hits++;
      return TRUE;
    }
  }


  /* none of the goals was a success: failure */
  return FALSE;

}


/* helper for memoized; description see above
 */
BOOLEAN straight_memoized( goal_array goals, int start, int num_goals,
                           goal_array critics, int num_critics )

{ 

  int i;/* helpers */
  node_list node;/* stores our current node in the tree */
  vertex_list ft;/* helper */
  int way = num_critics + num_goals - start;/* we have way many facts left */

  /* lookup starting goal from root table */
  ft = goals[start];
  node = ft->memo_start;
  /* didn't find it or don't have enough facts for min length of branch */
  if ( !node || node->min_way > --way ) return FALSE;

  /* now lookup the rest of the goals */
  for ( i=start+1; i<num_goals; i++ ) {
    ft = goals[i];
    if ( !node->goals ) return FALSE;
    node = sub_lookup( node->goals,
		       ft->hashval, ft->uid_block, ft->uid_mask );
    if ( !node || node->min_way > --way ) return FALSE;
    if ( node->min_way == 0 ) return TRUE;/* we can stop here */
  }

  /* same thing for all critics */
  for ( i=0; i<num_critics; i++ ) {
    ft = critics[i];
    if ( !node->critics ) return FALSE;
    node = sub_lookup( node->critics,
		       ft->hashval, ft->uid_block, ft->uid_mask );
    if ( !node || node->min_way > --way ) return FALSE;
    if ( node->min_way == 0 ) {
      return TRUE;
    }
  }

  /* we are through with our pair of sets and didn't hit the end of
   * a branch: the search was unsuccessfull
   */
  return FALSE;

}


/* works through all goals from curr_g to num_goals, and if that is
 * no goal at all, goes on with all critics from curr_c to num_critics,
 * starting at tree-node node
 *
 * NOTE: num_goals and num_critics are constants in the recursion pattern
 */
BOOLEAN sub_memoized( goal_array goals, int num_goals, int curr_g,
                      goal_array critics, int num_critics, int curr_c,
                      node_list node )

{

  int i;/* indicates the current remaining goals / critics */
  vertex_list ft;/* helper */
  node_list new_node;/* stores beginning of new branch */
  int way = num_critics - curr_c + num_goals - curr_g;

  if ( curr_g == num_goals ) {/* goals finished; do critics */

    /* an entry stopped here( empty critic set allowed )->got it */
    if ( node->min_way == 0 ) return TRUE;

    /* we can't go on with a new critic branch here */
    if ( !node->critics || node->min_way > way ) return FALSE;

    /* try a new search for each possible branch */
    for ( i=curr_c; i<num_critics; i++ ) {
      ft = critics[i];
      if ( ( new_node = sub_lookup( node->critics,
		        ft->hashval, ft->uid_block, ft->uid_mask ) ) != NULL )
        /* found this critic; try this branch without this critic,
         *  if it is a failure continue with remaining critics here
         */
        if ( sub_memoized( goals, num_goals, curr_g,
                           critics, num_critics, i + 1,
                           new_node ) ) return TRUE;
    }

    /* no branch was a success */
    return FALSE;

  } else {/* work on the remaining goals */

    /* see if we find a critic subset right here */
    if ( sub_memoized( goals, num_goals, num_goals,
                       critics, num_critics, 0,
                       node ) ) return TRUE;

    /* we can't find a different goal branch */
    if ( !node->goals || node->min_way > way ) return FALSE;

    /* now try a new search for each possible branch */
    for ( i=curr_g; i<num_goals; i++ ) {
      ft = goals[i];
      if ( ( new_node = sub_lookup( node->goals,
                        ft->hashval, ft->uid_block, ft->uid_mask ) ) != NULL )
        /* same stuff as above in critic part of the function */
        if ( sub_memoized( goals, num_goals, i + 1,
                           critics, num_critics, 0,
                           new_node ) ) return TRUE;
    }
   
    /* no new branch was a success */
    return FALSE;
  }

}


/* a simple function for a change: just look up the wanted fact from the
 * given table and return a pointer to it, if you find it,
 * a null pointer otherwise
 */
node_list sub_lookup( node_table *t, 
		      int hv, int ub, int um )

{

  int index;
  node_list node;

  index = ( int ) ( hv & S_HASH );

  for ( node = (*t)[index]; node; node = node->next ) {
    if ( node->hashval != hv ) continue;
    if ( node->uid_block != ub ) continue;
    if ( node->uid_mask != um ) continue;
    return node;
  }

  return NULL;

}


/* also simple: see if the fact is there already, if so, return a pointer 
 * to it, otherwise make a new entry and return a pointer to that one
 */
node_list sub_insert( node_table *t, 
		      int hv, int ub, int um )

{

  int index;
  node_list node;

  if ( ( node = sub_lookup( t, hv, ub, um ) ) != NULL ) return node; 

  index = ( int ) ( hv & S_HASH );

  node = ( node_list ) calloc( 1, sizeof( node_list_elt ) );
  MEMO(node_list_elt);
  CHECK_MEMORY(node);
  node->hashval = hv;
  node->uid_block = ub;
  node->uid_mask = um;
  node->goals = NULL;
  node->critics = NULL;
  node->min_way = MAX_GOALS * 2 + 1;/* this is longer than any path can be */
  node->next = (*t)[index];
  (*t)[index] = node;

  return node;

}


/* you should know about that one
 *
 * if you don't: look it up in
 *   T. Ottmann / P.Widmayer 
 *   Algorithmen und Datenstrukturen, 3. Auflage
 *   page 85/86, Quicksort-Varianten, median of three quicksort
 */
void quicksort( goal_array a, int l, int r )

{

  int v, i, j, m;
  vertex_list t;

  if ( r > l ) {
    m = ( int ) ( r + l ) / 2;
    if ( a[l]->hashval > a[r]->hashval ) {
      t = a[l];
      a[l] = a[r];
      a[r] = t;
    }
    if ( a[l]->hashval > a[m]->hashval ) {
      t = a[l];
      a[l] = a[m];
      a[m] = t;
    }
    if ( a[r]->hashval > a[m]->hashval ) {
      t = a[r];
      a[r] = a[m];
      a[m] = t;
    }
    i = l - 1;
    j = r;
    v = a[r]->hashval;
    while( i < j ) {
      do i++; while ( a[i]->hashval < v );
      do j--; while ( j >= 0 && a[j]->hashval > v );
      if ( i < j ) {
        t = a[i];
        a[i] = a[j];
        a[j] = t;
      }
    }
    t = a[i];
    a[i] = a[r];
    a[r] = t;
    quicksort( a, l, i - 1 );
    quicksort( a, i + 1, r );
  }

}


void free_sub_tree( node_list node )

{

  int i;
  node_list n, t;

  if (node->goals) {
    for ( i=0; i<S_HSIZE; i++ ) {
      n=(*(node->goals))[i];
      while ( n ) {
	t = n->next;
	free_sub_tree( n );
	free(n);
	bytes_memo -= sizeof(node_list_elt);
	n=t;
      }
    }
    free(node->goals);
    bytes_memo -= sizeof(node_table);
    node->goals = NULL;
  }
  if (node->critics) {
    for ( i=0; i<S_HSIZE; i++ ) {
      n=(*(node->critics))[i];
      while ( n ) {
	t = n->next;
	free_sub_tree( n );
	free(n);
	bytes_memo -= sizeof(node_list_elt);
	n=t;
      }
    }
    free(node->critics);
    bytes_memo -= sizeof(node_table);
    node->critics = NULL;
  }

}

