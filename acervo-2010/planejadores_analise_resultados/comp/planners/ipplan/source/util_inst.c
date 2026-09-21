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
static char rcsid[] = "$Id: util_inst.c,v 1.2 1998/05/27 16:25:30 ipp Exp ipp $";
#endif /* lint */

/*
 * some helpfunctions for instantiating
 */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */



token token_from_token_list( token_list tlist )
{
  char help[MAX_LENGTH] = "";
  token_list current;
  token result;
  
  for ( current = tlist; current; current = current->next ) {
    strcat( help, current->item );
    if ( current->next ) strcat( help, CONNECTOR );
  }
  result = ( token ) calloc( 1 + strlen( help ), sizeof( char ) );
  CHECK_MEMORY(result);
  strcpy( result, help );
  return result;
}


/* converts list of ( list of strings ) into list of strings
 * by connecting items of ( list of strings ) with the CONNECTOR character)
 *
 * is used by instantiate_first_parameter ( in instantiate.c ),
 * del_ALL_quantifiing ( same file ) and build_inst_effect_list ( also same )
 */
token_list token_list_from_fact_list( fact_list flist )

{

  token_list result, current;
  char help[MAX_LENGTH] = "";
  
  if ( !flist ) return NULL;

  result = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
  CHECK_MEMORY(result);
  for ( current = flist->item; current; current = current->next ) {
    strcat( help, current->item );
    if ( current->next ) strcat( help, CONNECTOR );
  }

  result->item = ( char * ) calloc( 1 + strlen( help ), sizeof( char ) );
  CHECK_MEMORY(result->item);
  strcpy( result->item, help );

  result->next = token_list_from_fact_list( flist->next );
  return result;

}


/* most inner helpfunction for copy_replace_op,
 * dealing with a token_list
 */
token_list copy_replace_tlist( token_list tlist, char *dest, char *source )

{

  token_list temp_token;

  if ( !tlist ) return NULL;

  temp_token = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
  CHECK_MEMORY(temp_token);
  if ( strcmp( tlist->item, dest ) == SAME ) {
    temp_token->item = ( char * ) calloc( 1+strlen( source ),sizeof( char ));
    CHECK_MEMORY(temp_token->item);
    strcpy( temp_token->item, source );
  } else {
    temp_token->item = (char *) calloc(1+strlen( tlist->item ),sizeof(char));
    CHECK_MEMORY(temp_token->item);
    strcpy( temp_token->item, tlist->item );
  }
  temp_token->next = copy_replace_tlist( tlist->next, dest, source );
  return temp_token;

}


/* second inner helpfunction for copy_replace,
 * dealing with a fact_list
 */
fact_list copy_replace_flist( fact_list flist, char *dest, char *source )

{

  fact_list temp_fact;

  if ( !flist ) return NULL;

  temp_fact = ( fact_list ) calloc( 1, sizeof( fact_list_elt ) );
  CHECK_MEMORY(temp_fact);
  temp_fact->item = copy_replace_tlist( flist->item, dest, source );
  temp_fact->next = copy_replace_flist( flist->next, dest, source );
  return temp_fact;

}


/* helpfunction for copy_replace,
 * dealing with an effect_list
 */
effect_list copy_replace_efflist( effect_list effects,char *dest,char *source)

{

  effect_list temp_effect;

  if ( !effects ) return NULL;

  temp_effect = ( effect_list ) calloc( 1, sizeof( effect_list_elt ) );
  CHECK_MEMORY(temp_effect);
  temp_effect->quantified_variables = effects->quantified_variables;
  temp_effect->conditions =
               copy_replace_flist( effects->conditions, dest, source);
  temp_effect->add_effects =
               copy_replace_flist( effects->add_effects, dest, source);
  temp_effect->del_effects =
               copy_replace_flist( effects->del_effects, dest, source);
  
  temp_effect->next = copy_replace_efflist( effects->next, dest, source );
  return temp_effect;

}


/* makes copy of given uninstantiated operator op,
 * replacing string dest with string source whenever
 * finding the first; removing first parameter from list;
 * thereby instantiates op's first parameter with source
 * ( cause dest = first parameter, see instantiate_first_parameter 
 * in instantiate.c )
 */
op_list_elt copy_replace_op( op_list_elt op, char *dest, char *source )

{

  op_list_elt result;
  fact_list temp1;
  token_list temp2, temp3;

  temp1 = ( fact_list ) calloc( 1, sizeof( fact_list_elt ) );
  CHECK_MEMORY(temp1);
  temp2 = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
  CHECK_MEMORY(temp2);
  temp3 = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
  CHECK_MEMORY(temp3);
  temp3->item = source;
  temp3->next = NULL;
  temp2->item = dest;
  temp2->next = temp3;
  temp1->item = temp2;
  temp1->next = op.params_objects;
  result.params_objects = temp1;

  result.params = op.params;

  result.name = op.name;

  result.preconds = copy_replace_flist( op.preconds, dest, source );

  result.effects = copy_replace_efflist( op.effects, dest, source );

  result.next = NULL;

  return result;

}


op_list_elt copy_op( op_list_elt op )

{

  op_list_elt result;

  result.params = op.params;

  result.name = op.name;

  result.preconds = op.preconds;

  result.effects = op.effects;

  result.params_objects = op.params_objects;

  result.next = NULL;

  return result;

}


/* makes copy of factlist, removing given item of it
 *
 * is used by instantiate_first_parameter ( in instantiate.c )
 * and build_inst_effect_list( same file )
 */
fact_list copy_remove( fact_list flist, fact_list rm )

{

  fact_list temp;

  if ( !flist ) return NULL;

  temp = ( fact_list ) calloc( 1, sizeof( fact_list_elt ) );
  CHECK_MEMORY(temp);
  if ( flist == rm ) {
    if ( flist->next ) { 
      temp->item = flist->next->item;
      temp->next = flist->next->next;
    } else {
      free( temp );
      temp = NULL;
    }  
  } else {
    temp->item = flist->item;
    temp->next = copy_remove( flist->next, rm );
  }

  return temp;

}


/* makes copy of given effect, replacing dest with source
 * in the conditions, add_effects and del_effects lists
 * and removing the first quantified variable
 *
 * is called by build_inst_effect_list
 */
effect_list_elt copy_replace_effect( effect_list_elt effect,
                                     char *dest, char *source)

{

  effect_list_elt result;

  result.quantified_variables = effect.quantified_variables->next;
  result.conditions = copy_replace_flist( effect.conditions, dest, source);
  result.add_effects = copy_replace_flist( effect.add_effects, dest, source);
  result.del_effects = copy_replace_flist( effect.del_effects, dest, source);
  
  result.next = NULL;

  return result;

}


char *make_name( op_list_elt op )

{

  char help [MAX_LENGTH] = "", *result;
  fact_list i_param, i_fact;

  strcat( help, op.name );
  for ( i_param=op.params; i_param; i_param=i_param->next ) {
    for ( i_fact=op.params_objects; i_fact; i_fact=i_fact->next )
      if ( strcmp( i_fact->item->item, i_param->item->item ) == SAME ) break;
    strcat( help, CONNECTOR );
    strcat( help, i_fact->item->next->item );
  }
  result = ( char * ) calloc( 1 + strlen( help ), sizeof( char ) );
  CHECK_MEMORY(result);
  strcpy( result, help );
  return result;

}


token_list make_objects( op_list_elt op )

{

  token_list result = NULL, temp;
  fact_list i_ob;

  for ( i_ob=op.params_objects; i_ob; i_ob=i_ob->next ) {
    temp = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
    CHECK_MEMORY(temp);
    temp->item = i_ob->item->next->item;
    temp->next = result;
    result = temp;
  }

  return result;

}

void check_instantiation(fact_list f_list, char* action)
{
  token_list t_token;
  fact_list t_fact;

  for (t_fact = f_list; t_fact != NULL; t_fact = t_fact->next)
    {
      for (t_token = t_fact->item; t_token != NULL; t_token = t_token->next)
	{
	  if ('?' == *(t_token->item))
	    {
	      fprintf(stderr, "\nipp: uninstantiated variable found at:");
	      if (action)
		fprintf(stderr, "\nipp: operator \"%s\" > %s", action, t_token->item);
	      else
		fprintf(stderr, "\nipp: all-quantified goal in fact file > %s", t_token->item);
	      fprintf(stderr, "\nipp: Check your input files for typing errors.\n\n");
	      OUTPUT_FILE;
	      exit(1);
	    }
	}
    }
}
