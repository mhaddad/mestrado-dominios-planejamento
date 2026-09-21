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

/* 	$Id: utilities.c,v 1.5 1998/05/27 16:25:30 ipp Exp ipp $	 */

#ifndef lint
static char vcid[] = "$Id: utilities.c,v 1.5 1998/05/27 16:25:30 ipp Exp ipp $";
#endif /* lint */


#include"ipp.h"
#include<ctype.h>


/* These are helper functions that might be used everywhere */

fact_list new_fact_list(void)
{
  fact_list result;

  result = ( fact_list ) calloc( 1, sizeof( fact_list_elt ) );
  CHECK_MEMORY(result);
/*   if (!result) */
/*     { */
/*       fprintf(stdout, "%s", NO_MEMORY); */
/*       fprintf(outputFile, "%s", NO_SOLUTION); */
/*       exit(2); */
/*     } */

  result->item = NULL; 
  result->next = NULL;
  return result;
}

token_list new_token_list(void)
{
  token_list result;
  result = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
  CHECK_MEMORY(result);
/*   if (!result) */
/*     { */
/*       fprintf(stdout, "%s", NO_MEMORY);  */
/*       fprintf(outputFile, "%s", NO_SOLUTION); */
/*       exit(2); */
/*     } */

  result->item = NULL; 
  result->next = NULL;
  return result;
}

effect_list new_effect_list(void)
{
  effect_list result;

  result = ( effect_list ) calloc( 1, sizeof( effect_list_elt ) );
  CHECK_MEMORY(result);
/*   if (!result) */
/*     { */
/*       fprintf(stdout, "%s", NO_MEMORY); */
/*       fprintf(outputFile, "%s", NO_SOLUTION); */
/*       exit(2); */
/*     } */

  result->quantified_variables = NULL;
  result->conditions = NULL;
  result->del_effects = NULL;
  result->add_effects = NULL;
  result->next = NULL;
  return result;
}

token new_token(int size)
{
  char* tok;

  tok = (char*) calloc(size, sizeof(char));
  CHECK_MEMORY(tok);
/*   if (!tok) */
/*     { */
/*       fprintf(stdout, "%s", NO_MEMORY); */
/*       fprintf(outputFile, "%s", NO_SOLUTION); */
/*       exit(2); */
/*     } */
  return tok;
}

op_list new_axiom_op_list(void)
{
  static int count = 0;
  token name;
  
  count++;
  name = new_token( strlen(HIDDEN_STR)+strlen(AXIOM_STR)+3+1 );
  sprintf( name, "%s%s%d", HIDDEN_STR, AXIOM_STR, count );
  
  return new_op_list( name );
}

op_list new_op_list( token name )
{
  op_list act_op;
  act_op = ( op_list ) calloc( 1, sizeof( op_list_elt ) );
  CHECK_MEMORY(act_op);
  if ( name )
    {
      act_op->name = new_token( strlen( name ) + 1 );
      strcpy( act_op->name, name );
    }
  else
    name = NULL;
  act_op->preconds = NULL;
  act_op->params = NULL;
  act_op->params_objects = NULL;
  act_op->next = NULL;
  act_op->number_of_real_params = 0; /* only for PDDL to hide some params */
  return act_op;
}

operator_list new_ground_operator( token name )
{
  operator_list act_op;
  act_op = ( operator_list ) calloc( 1, sizeof( operator_list_elt ) );
  CHECK_MEMORY(act_op);
  act_op->name = new_token( strlen( name ) + 1 );
  strcpy( act_op->name, name );
  act_op->preconditions = NULL;
  act_op->effects = NULL;
  act_op->objects = NULL;
  act_op->next = NULL;
  return act_op;
}

type_tree new_type_tree( token name )
{
  type_tree act_type;
  
  if (!name)
    return NULL;
  act_type = ( type_tree ) calloc( 1, sizeof( type_tree_elt ) );
  CHECK_MEMORY(act_type);
  act_type->name = new_token( strlen( name ) + 1 );
  strcpy( act_type->name, name );
  act_type->sub_types = NULL;
  return act_type;
}

type_tree_list new_type_tree_list( token name )
{
  type_tree_list act_type_list;
  
  act_type_list = ( type_tree_list ) calloc( 1, sizeof( type_tree_list_elt ) );
  CHECK_MEMORY(act_type_list);
  if ( name )
    act_type_list->item = new_type_tree( name );
  else
    act_type_list->item = NULL;
  act_type_list->next = NULL;
  
  return act_type_list;
}

type_tree main_type_tree()
{
  type_tree_list ttl;

  for ( ttl = global_type_tree_list; ttl; ttl = ttl->next )
    if ( strcmp( ttl->item->name, STANDARD_TYPE ) == SAME )
      return ttl->item;
  return NULL;
}

/* steps recursively through type tree and searches for name */
type_tree find_branch( token name, type_tree root )
{
  type_tree p;
  type_tree_list ttl;

  if ( !root )
    return NULL;
  if ( strcmp( root->name, name ) == SAME )
    return root;
  if ( !root->sub_types )
    return NULL;
  for ( ttl=root->sub_types; ttl; ttl=ttl->next )
    if (p = find_branch( name, ttl->item ) )
      return p;
  return NULL; 
}

/* calls itself recursively to get all objects that are of the types and
   subtypes of ttl */
fact_list build_object_list_from_ttl( type_tree_list ttl, 
				      fact_list types_done )
{
  fact_list f, td, std;
  token_list t, tl_dummy, st;
  type_tree_list sttl;

  if ( !ttl )
    return types_done;
  
  types_done = build_object_list_from_ttl( ttl->next, types_done );

  if ( t = type_already_known( ttl->item->name, types_done ) )
    return types_done;

  td = new_fact_list();
  t = td->item = new_token_list();
  /* begin with the name of the type... */
  t->item = copy_token( ttl->item->name );
  for ( f = orig_constant_list; f; f = f->next )
    {
      /* ...followed by objects of that type. */
      if ( strcmp( f->item->next->item, ttl->item->name ) == SAME )
	{
	  t->next = new_token_list();
	  t = t->next;
	  t->item = copy_token( f->item->item );
	}
    }
  /* now append the objects of the subtypes */
  std =  build_object_list_from_ttl( ttl->item->sub_types, types_done );
  /* now we can be sure that for each subtype a list with all
     objects of that type is somewhere in std. We simply take these
     lists and copy all of them into a new one for the supertype */
  for ( sttl = ttl->item->sub_types; sttl; sttl = sttl->next )
    {
      st = type_already_known( sttl->item->name, std );
      if ( st )
	{
	  t->next = copy_complete_token_list( st, &tl_dummy );
	  t = tl_dummy;
	}
    }
  td->next = std;
  return td;
}

token_list type_already_known( token name, fact_list types )
{
  fact_list f;

  for ( f = types; f; f = f->next )
    if ( strcmp( f->item->item, name ) == SAME )
      return f->item->next;
  return NULL;
}


void build_orig_constant_list()
{
  fact_list f, nextf, of, end;
  token_list t;
  BOOLEAN do_count;

  global_object_fl = build_object_list_from_ttl( global_type_tree_list, 
						 NULL );
  free_complete_fact_list( orig_constant_list );
  orig_constant_list = NULL;
  for ( f = global_object_fl; f; f = nextf )
    {
      nextf = f->next;
      if ( strcmp( f->item->item, STANDARD_TYPE ) == SAME )
	do_count = TRUE;
      else
	do_count = FALSE;
      for ( t = f->item->next; t; t = t->next )
	{
	  if ( !orig_constant_list )
	    orig_constant_list = end = new_fact_list();
	  else
	    {
	      end->next = new_fact_list();
	      end = end->next;
	    }
	  end->item = new_token_list();
	  end->item->item = copy_token( t->item );
	  end->item->next = new_token_list();
	  end->item->next->item = copy_token( f->item->item );
	  if ( do_count )
	    {
	      /* count objects for RIFO meta strategy */
	      objects_count++;
	    }
	}
    }
}


void add_to_type_tree( fact_list t_list, type_tree tree )
{
  type_tree branch = tree;
  type_tree_list new_branch;
  token this_type; 
  token super_type;

  /* step through list and build a hierarchy of types */
  for( ; t_list; t_list=t_list->next )
    {
      this_type = t_list->item->item;
      if ( !t_list->item->next ) 
	{
	  printf( "\n%s: error at '%s'.\n", act_filename, this_type );
	  OUTPUT_FILE;
	  exit( 1 );
	}
      super_type = t_list->item->next->item;
      if ( strcmp( branch->name, super_type ) != SAME )
	branch = find_branch( super_type, tree );
      if ( !branch ) 
	{
	  printf( "\n%s: unknown type '%s'.\n", act_filename, super_type );
	  OUTPUT_FILE;
	  exit( 1 );
	}
      /* now the type is a subtype of the one currently looked at 
	 in the type tree */
      new_branch = new_type_tree_list( this_type );
      new_branch->next = branch->sub_types;
      branch->sub_types = new_branch;
    }
}


void print_type_tree_list( type_tree_list root, int indent )
{
  int i;
  for(i=0;i<2*indent; i++ ) printf( " " );
  if ( root ) 
    {
      if ( !root->item || !root->item->name )
	{
	  printf( "\n%s: internal error: no type name specified.\n", 
		  act_filename );
	  OUTPUT_FILE;
	  exit( 1 );
	}
      else
	printf( "%s\n", root->item->name );
      if ( root->item->sub_types )
	print_type_tree_list( root->item->sub_types, indent+1 );
      if ( root->next )
	print_type_tree_list( root->next, indent );
    }
}

/* 'blowing up' a token list to get a fact list in which all
   token_lists only contain one token ... 
   this is only needed to be able to pass operator instatiation
   even when a (ex-goal) operator in 'uninstatiated format doesn't 
   need instatiation at all */
void factlist_from_tokenlist( fact_list *fl, token_list tl )
{
  fact_list *act_f;
  token_list act_t;

  for( act_f=fl, act_t=tl; act_t; 
       act_f = &((*act_f)->next), act_t=act_t->next )
    {
      *act_f = new_fact_list();
      (*act_f)->item = new_token_list();
      (*act_f)->item->item = act_t->item;
    }
}

token copy_token( token s )
{
  token d;
  
  d = new_token( strlen( s ) + 1 );
  strcpy( d, s );
  return d;
}

/*
 * This function copies a token_list by creating a new
 * token_list_elt for every element in source and
 * copying the item and next pointer to the new token_list_elt.
 * Then the function calls itself with the next element of source.
 *
 * returns: the start of the new token_list
 */
token_list copy_token_list( token_list source )
{
  token_list dummy;

  return copy_complete_token_list( source, &dummy );
  /* if it were sure that copy_token_list() would be used only
     when the tokens are never changed, copy_token_list() could
     be implemented without strcpy() */
}

token_list copy_complete_token_list( token_list source, token_list *end )
{
  token_list temp;

  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_token_list();
      if ( source->item )
	{
	  temp->item = new_token( strlen( source->item ) + 1 );
	  strcpy( temp->item, source->item );
	}
      temp->next = copy_complete_token_list( source->next, end );
      if ( !temp->next )
	*end = temp;
    }
  return temp;
}


fact_list copy_fact_list( fact_list source )
{
  fact_list temp;

  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_fact_list();
      temp->item = source->item;
      temp->next = copy_fact_list( source->next );
    }
  return temp;
}

fact_list copy_complete_fact_list( fact_list source, fact_list *end )
{
  fact_list temp;
  token_list dummy;

  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_fact_list();
      temp->item = copy_complete_token_list( source->item, &dummy );
      temp->next = copy_complete_fact_list( source->next, end );
      if ( !temp->next )
	*end = temp;
    }
  return temp;
}

effect_list copy_complete_effect_list( effect_list source, effect_list* end )
{
  effect_list temp;
  fact_list dummy;

  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_effect_list();
      temp->quantified_variables = 
	copy_complete_fact_list( source->quantified_variables, &dummy );
      temp->conditions =
	copy_complete_fact_list( source->conditions, &dummy );
      temp->add_effects =
	copy_complete_fact_list( source->add_effects, &dummy );
      temp->del_effects =
	copy_complete_fact_list( source->del_effects, &dummy );
      temp->next = copy_complete_effect_list( source->next, end );
      if ( !temp->next )
	*end = temp;
    }
  return temp;
}

op_list copy_complete_op( op_list source )
{
  op_list temp;
  fact_list dummy;
  effect_list edummy;
  
  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_op_list( source->name );
      temp->params = 
	copy_complete_fact_list( source->params, &dummy );
      temp->preconds =
	copy_complete_fact_list( source->preconds, &dummy );
      temp->effects =
	copy_complete_effect_list( source->effects, &edummy );
      temp->number_of_real_params =
	source->number_of_real_params;
      temp->next = NULL;
    }
}

op_list copy_complete_op_list( token name, op_list source, op_list *end )
{
  op_list temp;
  fact_list dummy;
  effect_list edummy;

  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_op_list( name );
      temp->params = 
	copy_complete_fact_list( source->params, &dummy );
      temp->preconds =
	copy_complete_fact_list( source->preconds, &dummy );
      temp->effects =
	copy_complete_effect_list( source->effects, &edummy );
      temp->number_of_real_params =
	source->number_of_real_params;
      temp->next = copy_complete_op_list( name, source->next, end );
      if ( !temp->next )
	*end = temp;
    }
  return temp;
}

void free_complete_token_list( token_list source )
{
  if ( source )
    {
      free_complete_token_list( source->next );
      if ( source->item )
	free( source->item );
      free( source );
    }
  return;
}

void free_complete_fact_list( fact_list source )
{
  if ( source )
    {
      free_complete_fact_list( source->next );
      free_complete_token_list( source->item );
      free( source );
    }
  return;
}

void free_complete_effect_list( effect_list source )
{
  /*
  if ( source )
    {
      free_complete_effect_list( source->next );
      free_complete_fact_list( source->quantified_variables );
      free_complete_fact_list( source->conditions );
      free_complete_fact_list( source->add_effects );
      free_complete_fact_list( source->del_effects );
      free( source );
    }
  return;
  */
}

void free_complete_op_list( op_list source )
{
  /*
  if ( source )
    {
      free_complete_op_list( source->next );
      free_complete_fact_list( source->parameters );
      free_complete_fact_list( source->preconds );
      free_complete_fact_list( source->effects );
      free( source );
    }
  return;
  */
}

operator_list copy_operator_list( operator_list source )
{ 
  operator_list temp;

  if ( !source )
    {
      temp = NULL;
    }
  else
    {
      temp = new_ground_operator( source->name );
      temp->preconditions = source->preconditions;
      temp->effects = source->effects;
      temp->objects = source->objects;
      temp->next = copy_operator_list( source->next );
    }
  return temp;
}

char* strupcase( char* from )
{
  char* to;
  char* res = (char*) calloc( strlen( from )+1, sizeof(char) );
  CHECK_MEMORY(res);
  to = res;
  if ( !(*from) ) return NULL;
  for( ; *from; to++, from++ )
    *to = (char) toupper( (int) *from );
  *to = 0;
  return res;
}


/* scans a list of effects and builds a new, reduced one, in which
   non-conditional and non-quantified effects are merged into one
   effect */
effect_list merge_literal_effects( effect_list e )
{
  effect_list result = new_effect_list();
  fact_list f;
  effect_list eff, dummy;

  result->add_effects = new_fact_list();
  result->del_effects = new_fact_list();
  /* result will contain all atomic effects in the end*/
  result->next = e;
  for( eff=result; eff->next; )
    {
      if ( ( !(eff->next->quantified_variables) ) && ( !(eff->next->conditions) ) )
	{ /* just an atomic effect, so append its add and del effects */
	  for ( f=result->add_effects; f->next; f=f->next )
	    ;
	  f->next = eff->next->add_effects;
	  for ( f=result->del_effects; f->next; f=f->next )
	    ;
	  f->next = eff->next->del_effects;
	  /* skip this effect, it is included into atomics */
	  dummy = eff->next;
	  eff->next = eff->next->next; 
	  free( dummy );
	}
      /* if quantified ot conditional, do nothing */
      else
	{
	  eff=eff->next;
	}
    }
  f = result->add_effects->next;
  free( result->add_effects );
  result->add_effects = f;
  f = result->del_effects->next;
  free( result->del_effects );
  result->del_effects = f;
  return result;
}


fact_list make_adl_fact( int c )
{
  fact_list result;

  result = new_fact_list();
  result->item = new_token_list();
  result->item->item = new_token( 2 );
  result->item->item[0] = (char) c;
  result->item->item[1] = 0;
  return result;
}

int get_adl_token( fact_list f )
{
  if ( ( !f ) || ( !f->item ) || ( !f->item->item ) )
    return 0;
  else if ( (int) f->item->item[0] > ENDNOT_CONST ) 
    {
      if ( f->item->item[0] == '?' )
	return VAR_CONST;
      else
	return LIT_CONST;
    }
  else
    return (int) f->item->item[0];
}


void write_plan_to_file(int time )
{
  BOOLEAN first = TRUE;
  int not_hidden = 0;
  int i, j, p;
  vertex_list op;
  op_list oop;

  fprintf( outputFile, "(" );

  for ( i = 0; i < time; i++ ) 
    {
      for ( j = 0; j < num_ops_at[i]; j++ ) 
	{
	  op = ops_at[i][j];
	  if ( op->is_noop ) continue; /* don't print noops */
	  if ( op->name[0] == HIDDEN_STR[0] ) continue; /* don't print 
							   axioms */
	  for( p=0; op->name[p]; p++ )
	    if ( ( op->name[p] == CONNECTOR[0] ) ||
		 ( op->name[p] == HIDDEN_STR[0] ) )
	      break;
	  /* find operator name and get the number of real parameters
	     (this means that all other params are in fact PDDL :VARS */
	  for( oop=loaded_ops; oop; oop = oop->next )
	    {
	      if ( ( strncmp( op->name, oop->name, p ) == SAME ) &&
		   ( ( !oop->name[p] ) ||
		     ( oop->name[p] == HIDDEN_STR[0] ) ) )
		{ /* if it is sure that the names are the same, then
		     we found what we searched for: the operator that
		     will give us the information about the number of
		     params needed */
		  not_hidden = oop->number_of_real_params;
		  break;
		}
	    }
	  if ( !oop )
	    {
	      printf( "\nerror: no loaded_op found for %s\n", op->name );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  if ( !first )
	    fprintf( outputFile, "\n" );
	  first = FALSE;
	  /* print out this op's name */
	  fprintf( outputFile, "(%s", oop->name );
	  if ( not_hidden )
	    {
	      /* okay, it's the same op, but now find out if there are still
		 hidden things after position p */
	      for ( ; op->name[p] != CONNECTOR[0] ; p++ )
		if ( !op->name[p] )
		  {
		    printf( "\nerror: CONNECTOR not found in %s[%d]\n", op->name, p );
		    OUTPUT_FILE;
		    exit( 1 );
		  }
	      /* now p points to connector */
	      for ( ; op->name[p]; p++ )
		{
		  if ( op->name[p] == CONNECTOR[0] )
		    {
		      if (not_hidden--) 
			fprintf( outputFile, " " );
		      else 
			break;
		    }
		  else
		    fprintf( outputFile, "%c", op->name[p] );
		}
	    }
	  fprintf( outputFile, ")" );
	}
    }  
  fprintf( outputFile, ")" );
}

