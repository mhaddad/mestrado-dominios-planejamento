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
static char rcsid[] = "$Id: save_graph.c,v 1.2 1998/05/27 16:48:40 ipp Exp ipp $";
#endif /* lint */

/*
 * file: save_graph.c
 * functions for writing the graph created by the planer IP2 
 * to two external files (one for facts and one for the ops).
 * The format of the files is as follows:
 *
 * '^' stands for the separator defined by SEP
 * level^name^is_noop^is_used
 * PRE^name^name...                list of preconditions
 * EXC^name^name...                list of exclusive nodes in same layer
 * ADD^name^condition^condition... add-effect with conditions
 * ADD...                          there could be more add-edges 
 * DEL^name^condition...           the same as for add-edges
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

#define SEP        "^"         /* the separator for the strings */
#define LEVEL      5           /* size of level as string */
#define SIZE       256         /* length of some temp strings */
#define NOOP       "noop"      /* needed to find noops */
#define NOOP_LEN   4           /* length of noop string */
#define NO_INITIALS "inertia only"

int Error(char *str);
BOOLEAN WriteFirstLine(vertex_list node, int level, FILE *fp);
BOOLEAN WritePreLine(vertex_list node, FILE *fp);
BOOLEAN WriteExcLine(vertex_list node, int time, int type,
		     FILE *fp, int active_part );
BOOLEAN WriteAddLines(vertex_list node, FILE *fp);
BOOLEAN WriteDelLines(vertex_list node, FILE *fp);

/*
 * op_table and fact_table are global variables
 * max_time is the last level from graph creation
 */
BOOLEAN SaveGraph( char *filename, int max_time, int active_part )
{
  FILE *fact_file, *ops_file;
  int time;                /* loopvariable for hashtables */
  vertex_list node;        /* temporaerer VERTEX struct pointer */
  char temp[SIZE];         /* for some temporary use must be carefull to check
		            * for bounds, but SIZE should be sufficient
		            */
  int i_count = 0;         /* used to determine if initial level exists */
  vertex_list_elt t_node;

  /************ Facts ************/
  sprintf( temp, "%s.facts", filename );

  /* open file for writing the facts */
  if((fact_file = fopen( temp, "w")) == NULL){
    sprintf(temp, "Cannot open file %s.", temp);
    Error(temp);
  }
  
  /* go through hashtables and write level by level to file */
  for(time = 0; 1; time++){
    get_next(fact_table[active_part][time], INIT);
    if ( get_next(fact_table[active_part][time], EXEC) == NULL ) break;

    get_next(fact_table[active_part][time], INIT);    
    while((node = get_next(fact_table[active_part][time], EXEC)) != NULL ){
      i_count = 1;
      WriteFirstLine(node, time, fact_file);
      WritePreLine(node, fact_file);
      WriteExcLine(node, time, 0, fact_file, active_part);
      WriteAddLines(node, fact_file);
      WriteDelLines(node, fact_file);
    }
    /* check if no initial facts level exists */
    if (0 == time && 0 == i_count)
      {
	/* create a new node with no edges and a descriptive name */
	t_node.name = (char*) calloc(SIZE, sizeof(char));
	CHECK_MEMORY(t_node.name);
	strcpy(t_node.name, NO_INITIALS);
	t_node.is_used = 0;
	t_node.precond_edges = NULL;
	t_node.add_edges = NULL;
	t_node.del_edges = NULL;
	t_node.is_noop = 0;

	WriteFirstLine(&t_node, 0, fact_file);
	WritePreLine(&t_node, fact_file);
	WriteAddLines(&t_node, fact_file);
	WriteDelLines(&t_node, fact_file);
      }
  }
  fclose(fact_file);

  /************* Operators **************/
  sprintf( temp, "%s.opers", filename );

  /* open file for writing the operators */
  if((ops_file = fopen( temp, "w" )) == NULL){
    sprintf(temp, "Cannot open file %s.", temp);
    Error(temp);
  }
  
  /* go through hashtables and write level by level to file */
  for(time = 0; 1; time++){ /* ops have one layer less than facts */
    get_next(op_table[active_part][time], INIT);
    if ( get_next(op_table[active_part][time], EXEC) == NULL ) break;

    get_next(op_table[active_part][time], INIT);   
    while((node = get_next(op_table[active_part][time], EXEC)) != NULL ){
      /* noops are not written to file, since they carry no information */
      if( !node->is_noop ){
	WriteFirstLine(node, time, ops_file);
	WritePreLine(node, ops_file);
	WriteExcLine(node, time, 1, ops_file, active_part);
	WriteAddLines(node, ops_file);
	WriteDelLines(node, ops_file);
      }
    }
  }
  fclose(ops_file);

  return TRUE;
}

/* Write the level, node-name and is_used to a line */
BOOLEAN WriteFirstLine(vertex_list node, int level, FILE *fp)
{
  fprintf( fp, "%d%s%s%s%d\n", level, SEP, node->name, SEP, node->is_used);

  return TRUE;
}

/* Write all the preconditions into one line */
BOOLEAN WritePreLine(vertex_list node, FILE *fp)
{
  edge_list temp; /* holds list of precond_edges */

  if( (temp = node->precond_edges) ){

    fprintf( fp, "PRE" ); /* PRE is the identifier for preconditions */ 
    
    while(temp){
      /* noops are not writen to the file */
      if( strncmp( temp->endpt->name, NOOP, NOOP_LEN ) )
	fprintf( fp, "%s%s", SEP, temp->endpt->name );
      temp = temp->next;
    }
    fprintf( fp, "\n" ); /* line must end with newline */
  }  
  return TRUE;
}

/* Write all exclusives to one line */
BOOLEAN WriteExcLine(vertex_list node, int time, int type,
		     FILE *fp, int active_part )
{
  edge_list temp; /* holds list of exclusives */
  int i;
  vertex_list o;
  int ex = 0;

  if ( type == 0 ) {
    for ( i=0; i<HSIZE; i++ ) {
      for ( o = fact_table[active_part][time][i]; o; o = o->next ) {
	if ( o == node ) continue;
	if ( ARE_MUTEX( o, node ) ) break;
      }
      if ( o ) {
	ex = 1;
	break;
      }
    }
  }
  if ( type == 1 ) {
    for ( i=0; i<HSIZE; i++ ) {
      for ( o = op_table[active_part][time][i]; o; o = o->next ) {
	if ( o == node ) continue;
	if ( ARE_MUTEX( o, node ) ) break;
      }
      if ( o ) {
	ex = 1;
	break;
      }
    }
  }

  if ( ex ) {

    fprintf( fp, "EXC"); /* EXC is the identifier for exclusives */
    
    if ( type == 0 ) {
      for ( i=0; i<HSIZE; i++ ) {
	for ( o = fact_table[active_part][time][i]; o; o = o->next ) {
	  if ( o == node ) continue;
	  if ( ARE_MUTEX( o, node ) ) {
	    if( strncmp( o->name, NOOP, NOOP_LEN ) )
	      fprintf( fp, "%s%s", SEP, o->name );
	  }
	}
      }
    }
    
    if ( type == 1 ) {
      for ( i=0; i<HSIZE; i++ ) {
	for ( o = op_table[active_part][time][i]; o; o = o->next ) {
	  if ( o == node ) continue;
	  if ( ARE_MUTEX( o, node ) ) {
	    if( strncmp( o->name, NOOP, NOOP_LEN ) )
	      fprintf( fp, "%s%s", SEP, o->name );
	  }
	}
      }
    }
    
  }

  return TRUE;

}


/* Write add-effect and its conditions to one line
 * and repeat as long as there are add-effects
 */ 
BOOLEAN WriteAddLines(vertex_list node, FILE *fp)
{
  edge_list edge;      /* list of conditions of an add_edge */
  cond_edge_list temp; /* holds a conditional add_edge */

  if( (temp = node->add_edges) ){
    while(temp){

      fprintf( fp, "ADD%s%s", SEP, temp->endpt->name );

      if( (edge = temp->conditions) ){
	while(edge){
	  /* noops are not writen to the file */
	  if( strncmp( edge->endpt->name, NOOP, NOOP_LEN ) )
	    fprintf( fp, "%s%s", SEP, edge->endpt->name );
	  edge = edge->next;
	}
      }
      fprintf( fp, "\n" ); /* line must end with newline */
      temp = temp->next;
    }
  }
  return TRUE;
}

/* Write del-effect and its conditions to one line
 * and repeat as long as there are del-effects
 */
BOOLEAN WriteDelLines(vertex_list node, FILE *fp)
{
  edge_list edge;      /* list of conditions of an del_edge */
  cond_edge_list temp; /* holds a conditional del_edge */

  if( (temp = node->del_edges) ){
    while(temp){

      fprintf( fp, "DEL%s%s", SEP, temp->endpt->name );

      if( (edge = temp->conditions) ){
	while(edge){
	  /* noops are not writen to the file */
	  if( strncmp( edge->endpt->name, NOOP, NOOP_LEN ) )
	    fprintf( fp, "%s%s", SEP, edge->endpt->name );
	  edge = edge->next;
	}
      }
      fprintf( fp, "\n" ); /* line must end with newline */
      temp = temp->next;
    }
  }
  return TRUE;
}

int Error(char *str)
{
  printf("%s\n", str);
  OUTPUT_FILE;
  exit(111); /* not from the system used error number */
}
