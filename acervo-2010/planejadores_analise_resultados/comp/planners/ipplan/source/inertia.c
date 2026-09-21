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
static char rcsid[] = "$Id: inertia.c,v 1.1 1998/05/25 08:16:55 ipp Exp ipp $";
#endif /* lint */

/* function for handling inertias
 *   void handle_inertia(token_list inertia )
 */


#include"ipp.h"/* defines, data structures, fn prototypes, global variables */


token_list get_inertia( fact_list init, op_list ops )

{

  fact_list i_fact, i_add, i_del;
  token_list result = NULL, temp, i_iner;
  token lit;
  effect_list i_ef;
  op_list i_op;

  for ( i_fact = init; i_fact; i_fact = i_fact->next ) {
    lit = i_fact->item->item;
    for ( i_iner = result; i_iner; i_iner=i_iner->next )
      if ( strcmp( i_iner->item, lit ) == SAME ) break;
    if ( i_iner ) continue;
    for ( i_op = ops; i_op; i_op=i_op->next ) {
      for ( i_ef = i_op->effects; i_ef; i_ef=i_ef->next ) {
        for ( i_add = i_ef->add_effects; i_add; i_add = i_add->next ) 
          if ( strcmp( i_add->item->item, lit ) == SAME ) break;
        if ( i_add ) break;
        for ( i_del = i_ef->del_effects; i_del; i_del = i_del->next ) 
          if ( strcmp( i_del->item->item, lit ) == SAME ) break;
        if ( i_del ) break;
      }
      if ( i_ef ) break;
    }
    if ( i_op ) continue;
    temp = ( token_list ) calloc( 1, sizeof( token_list_elt ));
    temp->item = lit;
    temp->next = result;
    result = temp;
  }

  return result;

}

        
/* the main function; simply goes through all initial facts, and if they
 * are inertia, removes them from the initial and goal state as well as
 * from all precondition and effect condition lists in the instantiated
 * operators.
 */
void handle_inertia( token_list inertia_names )

{

  /* some indizes */
  token_list i_token, j_token;
  operator_list i_op;
  inst_effect_list i_ef;
  int i = 0;
  char c;

  BOOLEAN had_one = FALSE;/* did we have an inertia yet? for printing */

  /* for all initial facts */
  for ( i_token = initial_facts; i_token; i_token = i_token->next ) {

    for ( j_token = inertia_names; j_token; j_token = j_token->next ) {
      i = 0;
      while ( c = j_token->item[i] )
        if ( i_token->item[i++] != c ) break;
      if ( !c && i_token->item[i] == CONNECTOR[0] ) break;
    }

    if ( j_token ||
	 is_instantiated_inertia( i_token->item ) ) {/* fact is an inertia */ 

      /* print out what's done, if required */
      if ( display_info > 2 ) {
	if ( !had_one ) {
	  printf( "\nipp: removing inertia: %s\n", i_token->item );
	  had_one = TRUE;
	} else {
	  printf( "                       %s\n", i_token->item );
        }
      }

      /* remove fact from all relevant lists */
      remove_inertia( i_token->item, &initial_facts );
      remove_inertia( i_token->item, &goal_facts );
      for ( i_op = operators; i_op; i_op = i_op->next ) {
        remove_inertia( i_token->item, &(i_op->preconditions) );
        for ( i_ef = i_op->effects; i_ef; i_ef = i_ef->next ) {
          remove_inertia( i_token->item, &(i_ef->conditions) );
        }
      }

    }
  }

  /* schnick schnack to the power of 3 */
  if ( display_info > 2 && had_one ) printf( "\n" );

}


/* a little bit tricky due to pointer handling...
 *
 * NOTE: we assume that a fact doesn't appear more than a single time in
 *       one precondition, initial, goal or effect condition list.
 *       seems to make sense.
 */
void remove_inertia( token str, token_list *list )

{

  /* bla bla */
  token_list i_token, previous;

  /* don't remove facts from empty lists, after all we don't have
   * inverse elements here
   */
  if ( !(*list) ) return;

  /* is it the first in our list ? */
  if ( strcmp( (*list)->item, str ) == SAME ) {
    (*list) = (*list)->next;
    return;
  }

  /* ... and how about the rest of it ? */
  previous = (*list);
  for ( i_token = (*list)->next; i_token; i_token = i_token->next ) {

    if ( strcmp( i_token->item, str ) == SAME ) {
      previous->next = i_token->next;
      break;
    }

    previous = i_token;
  }

}
    
/* helper for merging effects;
 *
 * returns TRUE gdw the two lists of strings contain the same elements
 * with no concern of their ordering
 * easy to understand, hopefully
 */
BOOLEAN are_same_hoffmann( token_list c1, token_list c2 )

{

  token_list t1, t2;

  for ( t1 = c1; t1; t1 = t1->next ) {
    for ( t2 = c2; t2; t2 = t2->next ) 
      if ( strcmp( t2->item, t1->item ) == SAME ) break;
    if ( !t2 ) break;
  }
  if ( t1 ) return FALSE;

  for ( t2 = c2; t2; t2 = t2->next ) {
    for ( t1 = c1; t1; t1 = t1->next ) 
      if ( strcmp( t2->item, t1->item ) == SAME ) break;
    if ( !t1 ) break;
  }
  if ( t2 ) return FALSE;

  return TRUE;

}


/* helper for merging effects, as it's name might suggest;
 *
 * puts the effects in list j that are not already contained in i
 * into i
 */
void merge_effects( inst_effect_list i, inst_effect_list j )

{

  token_list t1, t2, temp;

  for ( t1 = j->add_effects; t1; t1 = t1->next ) {
    for ( t2 = i->add_effects; t2; t2 = t2->next )
      if ( strcmp( t2->item, t1->item ) == SAME ) break;
    if ( !t2 ) {
      temp = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
      temp->item = ( char * ) calloc( strlen( t1->item ) + 1, sizeof( char ) );
      strcpy( temp->item, t1->item );
      temp->next = i->add_effects;
      i->add_effects = temp;
    }
  }

  for ( t1 = j->del_effects; t1; t1 = t1->next ) {
    for ( t2 = i->del_effects; t2; t2 = t2->next )
      if ( strcmp( t2->item, t1->item ) == SAME ) break;
    if ( !t2 ) {
      temp = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
      temp->item = ( char * ) calloc( strlen( t1->item ) + 1, sizeof( char ) );
      strcpy( temp->item, t1->item );
      temp->next = i->del_effects;
      i->del_effects = temp;
    }
  }

  /* free the memory for unnecessary effect; 
   *
   * currently out of order cause freeing memory is no hobby of mine
   */
  if ( 0 ) {
    t1 = j->conditions;
    while ( t1 ) {
      t2 = t1->next;
      free( t1 );
      t1 = t2;
    }
    t1 = j->add_effects;
    while ( t1 ) {
      t2 = t1->next;
      free( t1 );
      t1 = t2;
    }
    t1 = j->del_effects;
    while ( t1 ) {
      t2 = t1->next;
      free( t1 );
      t1 = t2;
    }
  }

}


/* called by main after instantiation and removing irrelevants is finished;
 * currently not sure wether it should be called before or after running
 * rifo
 */
void merge_identical_effects( void )

{

  operator_list i_op;
  inst_effect_list i_ef, j_ef, prev;

  /* for all operators */
  for ( i_op = operators; i_op; i_op = i_op->next ) {
    /* compare each effect */
    for ( i_ef = i_op->effects; i_ef; i_ef = i_ef->next ) {
      prev = i_ef;
      /* with each other effect */
      for ( j_ef = i_ef->next; j_ef; j_ef = j_ef->next ) {
	/* merge them, if their conditions are same */
        if ( are_same_hoffmann( i_ef->conditions, j_ef->conditions ) ) {
          merge_effects( i_ef, j_ef ); 
	  /* and throw the old effect out of it */
	  prev->next = j_ef->next;
	  if ( 0 ) free( j_ef );/* free if you like */
	} else {
	  prev = prev->next;
	}
      }
    }
  }

}


BOOLEAN is_instantiated_inertia( token t )

{

  operator_list i_op;
  inst_effect_list i_ef;
  token_list i;

  /* for all operators */
  for ( i_op = operators; i_op; i_op = i_op->next ) {
    /* compare each effect */
    for ( i_ef = i_op->effects; i_ef; i_ef = i_ef->next ) {
      for ( i = i_ef->del_effects; i; i = i->next )
	if ( strcmp( i->item, t ) == SAME ) return FALSE;
    }
  }

  return TRUE;

}
