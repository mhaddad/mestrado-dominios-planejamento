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


/*** utility functions for rifo ***/


/* FREE, MALLOC & CALLOC are used to keep track of memory usage */

void FREE( int size, void * ptr )
{
  memused -= size;
  free( ptr ); 
}



void *MALLOC( int size )
{
  void *new;
  char estr[40];

  memused += size;
  memmaxused = MAX( memused, memmaxused );
  new = malloc( size );
  if ( new == NULL ) 
    {
      sprintf( estr, "Could not alloc %d bytes\n", size );
      fatal_error( estr );
  }
  return new;
}



void *CALLOC( int size1, int size2 )
{
  void *new;
  char estr[40];

  memused += size1*size2;
  memmaxused = MAX( memused, memmaxused );
  new = calloc( size1, size2 );
  if ( new == NULL ) {
    sprintf( estr, "Could not calloc %d bytes\n", size1*size2 );
    fatal_error( estr );
  }
  return new;
}


/* stop the program - something seems to be REALLY wrong... */
void fatal_error( char *str )
{
  fprintf( stderr, "%s\n", str );
  OUTPUT_FILE;
  exit( 1 );
}



/* dealing with facts etc */


int equal_facts( token_list f1, token_list f2 )
{
  for( ; f1 && f2; f1 = f1->next, f2 = f2->next )
    if ( !equal_tokens( f1->item, f2->item ) ) 
      return 0;  /* different tokens*/
  if ( f1 || f2 ) return 0;  /* different lengths */
  return 1;
}



/* int really_is_var( char *str ) 
{ 
  return ( str[strlen( str )-1] == '>' );
} */



token_list token_list_from_token( char *str )
{
  char *p = str, *q, temp[MAXSTRLEN];
  token_list_elt dummy, *current;
  current = &dummy;
  while ( *p ) 
    {
      current->next = ( token_list ) MALLOC( sizeof( token_list_elt ) );
      current = current->next;
      for ( q = temp; ( ( *p ) != '\0' ) && ( ( *p ) != CONNECTOR[0] ); *q++ = *p++ );
      if ( ( *p ) == CONNECTOR[0] ) ++p;
      *q = '\0';
      current->item = ( char * ) CALLOC( 1 + strlen( temp ), sizeof( char ) );
      strcpy( current->item, temp );
    }
  current->next = NULL;
  return( dummy.next );
}



/* two in one */
token_list merge_token_lists( token_list tok1, token_list tok2 )
{
  int i;

  token_list_elt dummy;
  token_list res = &dummy, tmp;
  for( i=0; i<2; i++ ) {
    if (i==0) tmp = tok1;
    else tmp = tok2;
    while ( tmp ) {
      res->next = MALLOC( sizeof( token_list_elt ) );
      res = res->next;
      res->item = tmp->item;
      tmp = tmp->next;
    }
  }
  res->next = NULL;
  return dummy.next;
}



void free_token_list( token_list tl )
{
  token_list temp;
  
  while ( tl ) 
    {
      temp = tl->next;
      FREE( strlen( tl->item )+1, tl->item ); 
      FREE( sizeof( token_list_elt ), tl ); 
      tl = temp;
    }
}


/* no. of token_lists if fact_list */
int fact_list_length( fact_list fl )
{
  register int i = 0;

  while ( fl ) 
    {
      i++;
      fl = fl->next;
    }
  return i;
}



/* no. of tokens in token_list */
int token_list_length( token_list tl )
{
  register int i = 0;

  while ( tl ) {
    i++;
    tl = tl->next;
  }
  return i;
}



/* no. of instantiated operators in operator_list */
int op_list_length( operator_list ol )
{
  register int i = 0;

  while ( ol ) 
    {
      i++;
      ol = ol->next;
    }
  return i;
}



/* return 1 if tl contains token str */
int string_in_list( char *str, token_list tl )
{
  while ( tl ) 
    {
      if ( strcmp( tl->item, str ) == SAME ) return 1;
      else tl = tl->next;
    }
  return 0;
}



/* IO functions for rifo */

  
void print_token_list( token_list tokens, int oneline )
{
  while ( tokens ) 
    {
      printf( "%s", tokens->item );
      if ( tokens->next ) 
	{
	  if ( oneline ) printf( " " );
	  else printf( "\n" );
	}
      tokens = tokens->next;
    }
}



void print_one_set( settype *set, char *prefix, int donewline )
{
  int memnum;
  printf( "%s [ ", prefix );
  for ( memnum = 0; memnum < MAXSETSIZE; memnum++ ) 
    if ( set_member( memnum, set ) )
      printf( "%d ", memnum );
  printf( "] " );
  if ( donewline ) printf( "\n" );
}



void print_set_list( set_list sl, char *prefix )
{
  printf( "%s Set-list ( %d )", prefix, set_list_length( sl ) );
  while ( sl ) 
    {
      print_one_set( sl->item, "", 0 );
      sl = sl->next;
    }
  printf( "\n" );
}



/* rifo starting functions */

void save_original_ipp_information()
{
  token_list tdummy;

  save_operators = copy_operator_list( operators );
  save_initial_facts = copy_complete_token_list( initial_facts, &tdummy );
}



void reset_original_ipp_information()
{
  static int first_time = TRUE;
  token_list tdummy;
  
  if ( !first_time )
    {
      printf( "\nResetting original ipp state... " );
      operators = copy_operator_list( save_operators );
      initial_facts = copy_complete_token_list( save_initial_facts, &tdummy );
      printf( "%d ops, %d objects and %d initials.\n\n",
	      op_list_length( operators ),
	      fact_list_length( orig_constant_list ),
	      token_list_length( initial_facts ) );
    }
  else
    {
      first_time = FALSE;
    }
}

