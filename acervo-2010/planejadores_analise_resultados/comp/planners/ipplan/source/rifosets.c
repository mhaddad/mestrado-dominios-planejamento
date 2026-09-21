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


/*
 * set operations for RIFO 
 */


#include "ipp.h"
#include "rifo.h"

int allowsupers = 0;      /* allow supersets in set lists */



/* returns new set with one member (or none if member = NOELEMENT ) */
settype * make_set( int member )
{
  register int i;
  register settype_t s;

  s = MALLOC( sizeof( settype ) );
  s->memcount = 0;
  for ( i=0;i<SETARSIZE;i++ ) s->members[i] = 0;
  if ( member != NOELEMENT ) 
    {
      if ( ( member >= 0 ) && ( member < MAXSETSIZE ) ) 
	return set_insert_el( s,member );
      else
	fatal_error( "Member index in make_set too large\n" );
    }
  return s;
}



/* returns a list of sets with one set as the only element */
set_list make_set_list( int member )
{
  set_list sl;

  sl = MALLOC( sizeof( set_elt ) );
  sl->next = NULL;
  sl->item = make_set( member );
  return sl;
}



/* returns 1 if set is empty */
int set_empty( settype_t s )
{
  int i;
  for( i=0; i<SETARSIZE; i++ )
    if ( s->members[i] != 0 ) return 0;
  return 1;
}



/* returns 1 if all sets are empty */
int set_empty_list( set_list sl )
{
  while ( sl ) {
    if ( !set_empty( sl->item ) ) return 0;
    sl = sl->next;
  }
  return 1;
}



/* copies second argument into first one and returns pointer */
settype * set_copy( settype *result, settype *set )
{
  register int i;

  if ( !result ) result = make_set( NOELEMENT );
  for ( i=0; i<SETARSIZE; i++ ) result->members[i] = set->members[i];
  result->memcount = set->memcount;
  return result;
}



/* builds union over two sets. if docount = 1, update size of set */
settype * set_union( settype *result, settype *set1, settype *set2, int docount )
{
  register int i,b,m;
  register unsigned long w;

  if ( !result ) 
    result = make_set( NOELEMENT );
  m = 0;
  for ( i=0; i<SETARSIZE; i++ ) 
    {
      result->members[i] = set1->members[i] | set2->members[i];
      if ( docount ) 
	{
	  w = result->members[i];
	  for ( b=0; b<32; b++ ) 
	    {
	      if ( w&1 ) m++;
	      w=( w>>1 & 0x7FFFFFFF );
	    }
	}
    }
  if ( docount )
    result->memcount = m;
  else
    result->memcount = -1;
  return result;
}
  


/* builds the union over all sets in a given set_list. 
   Differences according to unionstrategy:
   unionstrategy>0: take first 'unionstrategy' sets 
   unionstrategy<0: take all best sets (-1) or best and second best sets (-2) ...  */
settype * set_union_list( set_list sl, int maxsets )
{
  settype *result;
  register int i;
  register int maxsize = sl->item->memcount;

  result = make_set( NOELEMENT );
  if ( unionstrategy > 0 ) /* take first 'unionstrategy' elements */
    for ( i=0; ((i<maxsets) && sl); i++,(sl = sl->next) ) 
      result = set_union( result,result,sl->item,0 );
  else if ( unionstrategy < 0 )
    { /* take all sets with abs(unionstr.)'th minimal number of elements */
      while ( sl && maxsets ) 
	{
	  while ( ( sl ) && ( sl->item->memcount <= maxsize ) ) 
	    {
	      result = set_union( result,result,sl->item,0 );
	      sl = sl->next;
	    }
	  maxsets++;
	  if ( sl && maxsets )
	    maxsize = sl->item->memcount;
	}
    }
  else /* just one set */
    { 
      result = set_union( result, result, sl->item, 0);
    }
  result = set_union( result, result, result, 1 );
  return result;
}



/* insert one element (int member = code for fact/typed object) into set */
settype * set_insert_el( settype *result, int member )
{

  if ( !result ) 
    return make_set( member );
  else if ( set_member( member,result ) ) 
    return result;
  else 
    {
      if ( ( member >= 0 ) && ( member < MAXSETSIZE ) ) 
	{
	  result->memcount++;
	  result->members[( member/32 )] |= ( long unsigned )1<<( member%32 );
	  return result;
	} 
      else
	{
	  printf( "Member index %d in set_insert_el too large\n", member );
	  OUTPUT_FILE;
	  exit( 1 );
	} 
    }
  return result;
}



/* returns 1 if member is element of set */
int set_member( int member, settype *set )
{
  return ( set->members[( member/32 )] & ( long unsigned )1<<( member%32 ) );
}



/* returns 1 if s1 is subset or equals s2 */
int set_subseteq( settype *set1, settype *set2 )
{
  register int i;

  if ( set1->memcount > set2->memcount ) 
    return 0;
  else 
    for ( i=0; i<SETARSIZE; i++ )
      if ( ( set1->members[i] & set2->members[i] ) != set1->members[i] )
	return 0;
  return 1;
}



/* returns 1 if s1 = s2 */
int set_eq( settype *set1, settype *set2 )
{
  register int i;

  if ( set1->memcount != set2->memcount ) 
    return 0;
  else 
    for ( i=0; i<SETARSIZE; i++ )
      if ( set2->members[i] != set1->members[i] )
	return 0;
  return 1;
}



/* returns length of set_list (no. of sets) */
int set_list_length( set_list sl )
{
  register int i = 0;

  while ( sl ) 
    {
      i++;
      sl = sl->next;
    }
  return i;
}



/* returns copy of given set_list */
set_list set_copy_list( set_list list )
{
  set_list sl;

  if ( !list ) 
    return NULL;
  else {
    sl = MALLOC( sizeof( set_elt ) );
    sl->item = set_copy( NULL,list->item );
    sl->next = set_copy_list( list->next ); /* recursion */
    return sl;
  }
}




void set_free_list( set_list list )
{
  set_list temp;

  while ( list ) {
    temp = list->next;
    FREE( sizeof( settype ),list->item ); 
    FREE( sizeof( set_elt ),list ); 
    list = temp;
  }
}



/* merges newset into sl. sl stays ordered, smallest sets will be found
   at the beginning.
   different behavior according to unionstrategy:
   if unionstrategy = 0 simply build union over all elements in one set */
void set_merge_into_list( set_list *sl, int *length, 
			  settype *newset, int newmem )
{
  int removed;
  register set_list temp, temp2, newel;

  if ( unionstrategy == 0 ) 
    {
      if ( !(*sl) ) 
	*sl = make_set_list( NOELEMENT );
      (*sl)->item = set_union( ( *sl )->item,( *sl )->item,newset,1 );
      return; 
    }
  else if ( !allowsupers ) 
    {
      for ( temp=*sl; temp; temp=temp->next ) 
	if ( set_subseteq( temp->item,newset ) ) return; /* new set is a superset */
      removed = 1;
      while ( removed ) { /* remove supersets of new set */
	for ( temp=*sl; temp; temp=temp->next )
	  if ( set_subseteq( newset,temp->item ) ) break; /* new set is subset */
	if ( temp ) 
	  { /* remove old set */
	    ( *length )--;
	    if ( temp == *sl ) 
	      {
		*sl = ( *sl )->next;
		FREE( sizeof( settype ),temp->item ); 
		FREE( sizeof( set_elt ),temp ); 
	      } 
	    else 
	      {
		temp2 = *sl; 
		while ( temp2->next != temp ) temp2 = temp2->next;
		temp = temp->next;
		FREE( sizeof( settype ),temp2->next->item ); 
		FREE( sizeof( set_elt ),temp2->next ); 
		temp2->next = temp;
	      }
	  } 
	else removed = 0;
      }
    } 
  else 
    { /* allow super sets but remove identical sets */
      for ( temp=*sl; temp; temp=temp->next ) 
	if ( set_eq( temp->item,newset ) ) return; /* new set is a equal */
    }
  newel = MALLOC( sizeof( set_elt ) );
  if ( newmem ) newel->item = set_copy( NULL,newset );
  else newel->item = newset;
  ( *length )++; 
  if ( ( *sl == NULL ) || ( newset->memcount <= ( *sl )->item->memcount ) ) {
    newel->next = *sl;
    *sl = newel;
  } 
  else 
    {
      temp = *sl;
      while ( temp->next && ( temp->next->item->memcount < newset->memcount ) ) 
	{
	  temp = temp->next;
	}
      newel->next = temp->next;
      temp->next = newel;
    }
}



/* recursively merge two set_lists. help function for set_merge_lists() */
set_list rec_set_merge_lists( set_list s1, set_list s2 )
{
  int nolength = 0;

  if ( !s1 ) return s2;
  set_merge_into_list( &s2, &nolength, s1->item, 0 );
  return rec_set_merge_lists( s1->next,s2 ); /* should free s1, but ... */
}



/* merges two set_lists */
set_list set_merge_lists( set_list s1, set_list s2 )
{
  set_list res, temp;
  int i;

  if ( rifo_display_info >= 5 ) 
    {
      print_set_list( s1, ">>>> Merge s1 = " );
      print_set_list( s2, ">>>> Merge s2 = " );
    }
  res = rec_set_merge_lists( s1, s2 );
  if ( res ) 
    {
      temp = res;
      for ( i = 0; ( ( i < ( setlistthres-1 ) ) && temp ); i++ )
	temp = temp->next;
      if ( temp ) 
	{
	  set_free_list( temp->next );
	  temp->next = NULL;
	}
    }
  if ( rifo_display_info >= 5 ) 
    {
      print_set_list( res, ">>>> Merge res = " );
    }
  return res;
}



/* build all possible unions over one set out of s1 and one out of s2.
   build a new set_list out of the resulting sets */
set_list set_multiply_lists( set_list s1, set_list s2 )
{
  set_list res = NULL;
  set_list s2beg = s2;
  set_list s1beg = s1;
  set_list temp;
  int resnum = 0;
  settype newset;
  register int i;

  if ( rifo_display_info >= 5 ) 
    {
      print_set_list( s1, ">>>> Multiply s1 = " );
      print_set_list( s2, ">>>> Multiply s2 = " );
    }
  if ( unionstrategy == 0 ) 
    { /* collect everything in one set */
      if ( s1 && s2 ) 
	{
	  set_union( s1->item,s1->item,s2->item,1 );
	  set_free_list( s2 );
	} 
      else 
	{ 
	  set_free_list( s1 );
	  set_free_list( s2 );
	  s1 = NULL;
	}
    if ( rifo_display_info >= 5 ) 
      {
	print_set_list( s1, ">>>> Multiply res = " );
      }
    return s1;
  } 
  else 
    { /* make a real set multiplication */
      while ( s1 ) 
	{
	  s2 = s2beg;
	  while ( s2 ) 
	    {
	      set_merge_into_list( &res, &resnum,
				   set_union( &newset,s1->item,s2->item,1 ), 1 );
	      s2 = s2->next;
	    }
	  s1 = s1->next;
	}
      
      if ( resnum > setlistthres ) 
	{ /* cut list down if longer than thresshold */
	  temp = res;
	  for ( i = 0; i < ( setlistthres-1 ); i++ ) 
	    {
	      if ( temp == NULL ) fatal_error( "Wrong set_list length\n" );
	      temp = temp->next;
	    }
	  if ( temp ) 
	    {
	      set_free_list( temp->next );
	      temp->next = NULL;
	    }
	}
      
      /* free original lists */
      set_free_list( s1beg );
      set_free_list( s2beg );
      
      if ( rifo_display_info >= 5 ) 
	{
	  print_set_list( res, ">>>> Multiply res = " );
	}
      return res;
    }
}
