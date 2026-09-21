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
static char rcsid[] = "$Id: hash.c,v 1.1 1998/05/25 08:16:55 ipp Exp ipp $";
#endif /* lint */

/*
 * functions for handling graph hashtables:
 *   vertex_list lookup_from_table( hashtable, char * )
 *   vertex_list insert_into_table( hashtable, char * )
 *   vertex_list get_next( hashtable, BOOLEAN )
 */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

/* helpfunction; returns hashvalue of key word;
 *
 * hashing method: ( key mod BIGPRIME ) mod HSIZE 
 */
int hash( char *skey )

{
  char* key = skey;
  int h;

  for( h=0; *key != '\0'; key++ ) h = ( h * 256 + ( *key ) ) % BIGPRIME;

  return h;

}


/* returns pointer to vertex with name key in given hashtable,
 * if there is no vertex with that name, returns NULL
 */
vertex_list lookup_from_table( hashtable t, char *key )

{

  vertex_list v;
  int hval = hash( key );
  int index = hval % HSIZE;

  for( v = t[index]; v; v = v->next ) {
    if ( hval == v->hashval && strcmp( key, v->name ) == SAME ) return v;
  }

  return NULL;

}


/* inserts vertex with name key in given hashtable, if it's not already there;
 * returns pointer to the new vertex
 */
vertex_list insert_into_table( hashtable t, char *key )

{

  vertex_list v;
  int hval = hash( key );
  int index = hval % HSIZE;

  if ( ( v = lookup_from_table( t, key ) ) != NULL ) return v;

  v = ( vertex_list ) calloc( 1, sizeof( vertex_list_elt ) );
  CHECK_MEMORY(v);
  GRAPH(vertex_list_elt);
  v->name = ( char * ) calloc( 1 + strlen( key ), sizeof( char ) );
  CHECK_MEMORY(v->name);
  bytes_graph+=(1+strlen(key)) * sizeof(char);
  strcpy( v->name, key );
  v->hashval = hval;
  v->is_noop = FALSE;
  v->my_noop = NULL;
  v->add_edges = NULL;
  v->del_edges = NULL;
  v->precond_edges = NULL;
  v->is_true = 0;
  v->is_used = 0;
  v->is_goal = 0;
  v->is_critic = 0;
  v->heuristic = 1.0;
  v->is_dummy = FALSE;
  v->next = t[index];
  t[index] = v;

  return v;

}

/* inserts noop vertex with name key in given hashtable,
 * if it's not already there;
 * returns pointer to the new vertex
 */
vertex_list insert_noop_into_table( hashtable t, char *key )
{
  vertex_list v;
  int hval = hash( key );
  int index = hval % HSIZE;

  if ( ( v = lookup_from_table( t, key ) ) != NULL ) return v;

  v = ( vertex_list ) calloc( 1, sizeof( vertex_list_elt ) );
  CHECK_MEMORY(v);
  GRAPH(vertex_list_elt);
  v->name = ( char * ) calloc( 1 + strlen( key ), sizeof( char ) );
  CHECK_MEMORY(v->name);
  bytes_graph+=(1+strlen(key)) * sizeof(char);
  strcpy( v->name, key );
  free(key); /* frank memory leak */

  v->hashval = hval;
  v->is_noop = FALSE;
  v->my_noop = NULL;
  v->add_edges = NULL;
  v->del_edges = NULL;
  v->precond_edges = NULL;
  v->is_true = 0;
  v->is_used = 0;
  v->is_goal = 0;
  v->is_critic = 0;
  v->heuristic = 1.0;
  v->next = t[index];
  t[index] = v;

  return v;
}

/* can be used to get the vertexes out of a given hashtable one by one;
 * first call with second argument TRUE, so that the static variables
 * i and current, which hold the current position in the hashtable,
 * are initialised; then call with second argument FALSE
 * until return value is NULL
 */
vertex_list get_next( hashtable t, BOOLEAN initialise )

{

  static int i;
  static vertex_list current;
  vertex_list temp;

  if ( initialise ) {
    i = 0;
    current = t[0];
    return NULL;
  }

  while ( TRUE ) {
    if ( current ) {
      temp = current;
      current = current->next;
      return temp;
    } else {
      if ( (++i) >= HSIZE ) return NULL;
      current = t[i];
    }
  }

}
