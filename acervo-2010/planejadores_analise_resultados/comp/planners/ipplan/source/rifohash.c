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

#include "ipp.h"
#include "rifo.h"

int num_created;
int rifo_hash( char *key, int size );

#define BIGPRIME 8000977
/* extern int NUMINTS; */

/**FOR BETTER PRINTING: remember to take out!!!!**/
/* #define HSIZE1 1                             */
#define HSIZE1 HSIZE



/* returns hash value of token key */
int rifo_hash( token key, int size )
{
  int h;
  for( h=0; *key != '\0'; key++ )  
    h = ( h*256 + ( *key ) ) % size;
  return h;
}



/* searches for key and returns pointer to hash entry or NULL if not found */
rifo_hashentry_t rifo_lookup_from_table( rifo_hashtable_t htable, token key )
{
  rifo_hashentry_t l;
  int hval = rifo_hash( key, BIGPRIME );
  int index = hval % HSIZE1;
  for( l = htable[index]; l != NULL; l = l->next ) {
    if ( hval == l->hashval && strcmp( key,l->key ) == SAME ) return l;
  }
  return NULL;
}



/* inserts token but ONLY IF IT'S NOT THERE ALREADY. Returns pointer to hash entry */
rifo_hashentry_t rifo_insert_token( rifo_hashtable_t htable, token t )
{
  rifo_hashentry_t retval;
  if ( ( retval = rifo_lookup_from_table( htable, t ) ) == NULL ) 
    retval = rifo_insert_into_table( htable, t );
  return retval;
}



/* insert token into hashtable. return hashentry */
rifo_hashentry_t rifo_insert_into_table( rifo_hashtable_t htable, token key )
{
  rifo_hashentry_t l;
  int hval = rifo_hash( key, BIGPRIME );
  int index = hval % HSIZE1;
  l = ( rifo_hashentry_t ) CALLOC( 1, sizeof( rifo_hashentry ) );
  l->key = ( char * ) CALLOC( 1 + strlen( key ), sizeof( char ) );
  strcpy( l->key, key ); /* key: the token itself */
  l->hashval = hval;   /* hashval: hash value calculated by rifo_hash() */
  l->factnode = NULL;  /* factnode, opnode: which fact/operator is represented */
  l->opnode = NULL;
  l->used_facts = NULL; /* set of needed facts to get this node */
  l->memcode = -1;      /* new element */
  l->lastdepth = 0;     /* cached on which level last time */
  l->next = htable[index]; /* chain of entries with same hash value */
  htable[index] = l;
  ++num_created;  /**global, use for info purposes **/
  return l;
}



/* if flag=0 ( INIT ), just reset. Otherwise,
 * go from where you left off last ( use static vars to hold state ).
 * Return NULL if no more.
 * NOTE: this is DANGEROUS the way it's written since can't interleave
 * with different hash tables, etc.  Should really have flag be state.
 */
rifo_hashentry_t rifo_get_next( rifo_hashtable_t h, int flag )
{
  static int i;
  static rifo_hashentry_t current;
  rifo_hashentry_t temp;
 
  if ( flag==0 ) {i = 0; current = h[0]; return NULL;}
  while ( 1 ) 
    {
      if ( current != NULL ) {
	temp = current;
	current = current->next;
	return temp;
      } 
      else 
	{
	  if ( ( ++i ) >= HSIZE1 ) return NULL;
	  current = h[i];
	}
    }
}


