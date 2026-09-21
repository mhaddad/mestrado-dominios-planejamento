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
static char rcsid[] = "$Id: util_build.c,v 1.2 1998/05/27 16:52:21 ipp Exp ipp $";
#endif /* lint */

/*
 * some helpfunctions for building the graph
 */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

/* checks if given facts are in fact_table[time],
 * and if no pair of them is exclusive of each other
 *
 */
BOOLEAN are_there_non_exclusive( token_list facts, int time )

{

  static goal_array ft;/* used to store found fact-vertexes */

  token_list i_token;/* index */
  int num = 0, i, j;/* num is number of facts found, i and j indizes */

  /* find and store all the fact vertexes */
  for ( i_token = facts; i_token; i_token = i_token->next ) {
    ft[num] = lookup_from_table( fact_table[rifo_active_part][time], i_token->item );
    if ( !ft[num] ) return FALSE;/* not found one fact */
    num++;
  }

  /* check for mutual exclusion */
  for ( i = 0; i < num; i++ )
    for ( j = i + 1; j < num; j++ )
      if ( ARE_MUTEX( ft[i], ft[j] ) ) return FALSE;/* found bad pair */

  return TRUE;

}


/* checks if given facts are in fact_table[time],
 * and if no pair of them is exclusive of each other;
 * if so, returns them in VAR parameters ft and num
 *
 */
BOOLEAN get_them_non_exclusive( token_list facts, int time,
                                 goal_array *ft, int *num )

{

  token_list i_token;/* index */
  int i, j;/* indizes */

  *num = 0;/* num will be number of stored facts */

  /* find and store all the fact vertexes */
  for ( i_token = facts; i_token; i_token = i_token->next ) {
    (*ft)[*num] = lookup_from_table( fact_table[rifo_active_part][time], i_token->item );
    if ( !(*ft)[*num] ) return FALSE;/* not found one fact */
    (*num)++;
  }

  /* check for mutual exclusion */
  for ( i = 0; i < *num; i++ )
    for ( j = i + 1; j < *num; j++ )
      if ( ARE_MUTEX( (*ft)[i], (*ft)[j] ) ) return FALSE;/* found bad pair */

  return TRUE;

}


/* checks if given facts are in fact_table[time],
 * if so, returns them in VAR parameters ft and num
 */
BOOLEAN get_them( token_list facts, int time,
		  goal_array *ft, int *num )

{

  token_list i_token;/* index */

  *num = 0;/* num will be number of stored facts */

  /* find and store all the fact vertexes */
  for ( i_token = facts; i_token; i_token = i_token->next ) {
    (*ft)[*num] = lookup_from_table( fact_table[rifo_active_part][time], i_token->item );
    if ( !(*ft)[*num] || (*ft)[*num]->is_dummy ) return FALSE;/* not found one fact */
    (*num)++;
  }

  return TRUE;

}


/* helpfunction for apply_operator;
 * inserts v at beginning of e and returns pointer to
 * extended list
 */
edge_list insert_edge( edge_list e, vertex_list v )

{

  edge_list new_edge = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
  CHECK_MEMORY(new_edge);
  GRAPH(edge_list_elt);
  new_edge->next = e;
  new_edge->endpt = v;

  return new_edge;

}


/* helpfunction for apply_operator;
 * inserts v at end of e and returns pointer to
 * extended list
 */
edge_list insert_edge_at_end( edge_list e, vertex_list v )

{

  edge_list new_edge;

  if ( e == NULL ) {
    new_edge = ( edge_list ) calloc( 1, sizeof( edge_list_elt ) );
    CHECK_MEMORY(new_edge);
    GRAPH(edge_list_elt);
    new_edge->endpt = v;
    new_edge->next = NULL;

    return new_edge;
  } else {
    e->next = insert_edge_at_end( e->next, v );

    return e;
  }

}


/* helpfunction for apply_operator;
 * inserts v with conditions t 
 * at beginning of e and returns pointer to
 * extended list
 */
cond_edge_list insert_cond_edge( cond_edge_list e,
                                 vertex_list v,
                                 edge_list t )

{

  cond_edge_list new_edge = ( cond_edge_list )
                            calloc( 1, sizeof( cond_edge_list_elt ) );
  CHECK_MEMORY(new_edge);
  GRAPH(cond_edge_list_elt);
  new_edge->next = e;
  new_edge->endpt = v;
  new_edge->conditions = t;

  return new_edge;

}


/* helpfunction for apply_operator;
 * inserts v with conditions t 
 * at beginning of e and returns pointer to
 * extended list
 */
cond_edge_list insert_sort_cond_edge( cond_edge_list e,
				      vertex_list v,
				      edge_list t )

{

  cond_edge_list result = NULL, i_ce, prev;

  cond_edge_list new_edge = ( cond_edge_list )
    calloc( 1, sizeof( cond_edge_list_elt ) );
  CHECK_MEMORY(new_edge);
  GRAPH(cond_edge_list_elt);
  new_edge->endpt = v;
  new_edge->conditions = t;

  /* ">" = least constrained, "<" = most constrained */
  /* currently the most constrained precondition is always tried first */
  if ( !e || v->heuristic < e->endpt->heuristic ) {
    new_edge->next = e;
    result = new_edge;
  } else {
    prev = e;
    for ( i_ce = e->next; i_ce; i_ce=i_ce->next ) {
      if ( v->heuristic < i_ce->endpt->heuristic ) break;
      prev = prev->next;
    }
    prev->next = new_edge;
    new_edge->next = i_ce;
    result = e;
  }
        
  return result;

}


/* helpfunction for apply_operator;
 * inserts v with conditions t 
 * at end of e and returns pointer to
 * extended list
 */
cond_edge_list insert_cond_edge_at_end( cond_edge_list e,
                                        vertex_list v,
                                        edge_list t )

{

  cond_edge_list new_edge;

  if ( e == NULL ) {
    new_edge = ( cond_edge_list ) calloc( 1, sizeof( cond_edge_list_elt ) );
    CHECK_MEMORY(new_edge);
    GRAPH(cond_edge_list_elt);
    new_edge->endpt = v;
    new_edge->conditions = t;
    new_edge->next = NULL;

    return new_edge;
  } else {
    e->next = insert_cond_edge_at_end( e->next, v, t );

    return e;
  }

}


/* helpfunction for build_graph_layer;
 * sets up uid s for given vertex with given 'number'
 * of vertex in hashtable
 */
void set_uid( vertex_list v, int id )

{

  v->uid_block = id / 32;
  v->uid_mask = 1 << ( id % 32 );

  if ( id / 32 == num_ints ) num_ints++;

}


/* helpfunction, called from make_noop_layer in build_graph.c
 * assigns prefix "noop_" to given string
 */
char *make_noop_string( char *str )

{

  char *result;

  result = ( char * ) calloc( 2+strlen( str ) + strlen( NOOP ), 
			      sizeof( char ) );
  CHECK_MEMORY(result);
  bytes_graph += (2+strlen(str) +strlen(NOOP)) * sizeof(char);
  sprintf( result, "%s%s%s", NOOP, CONNECTOR, str );

  return result;

}
