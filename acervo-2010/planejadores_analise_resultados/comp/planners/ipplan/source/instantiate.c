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
 * function for instantiating ops:
 *   void instantiate( op_list, fact_list )
 *   void print_operators( operator_list )
 *
 * makes use of the following functions, taken from util_inst.c:
 *   token_list token_list_from_fact_list( fact_list )
 *   op_list_elt copy_replace_op( op_list_elt, char *, char * )
 *   fact_list copy_remove( fact_list, fact_list )
 *   effect_list_elt copy_replace_effect( effect_list_elt, char *, char * )
 */

#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

void instantiate( op_list ops, fact_list initials,
		  token_list inertia,  fact_list constants )
{

  op_list op_i;

  operators = NULL;

  for( op_i = ops; op_i; op_i = op_i->next )
    inertia_instantiate( *op_i, 0, initials, inertia, constants );

}


/* instantiate ONE operator */
void inertia_instantiate( op_list_elt op, int curr,
			  fact_list initials,
			  token_list inertia,  fact_list constants )

{

  fact_list i_prec, i_init, in_const, i_con;
  token_list i_iner, i_toc;
  op_list_elt help_op;
  int i;

  i_prec = op.preconds;
  for ( i=0; i<curr; i++ ) i_prec = i_prec->next;

  for ( ; i_prec; i_prec=i_prec->next ) {
    /* look for inertia */
    for ( i_iner = inertia; i_iner; i_iner=i_iner->next ) 
      if ( strcmp( i_prec->item->item, i_iner->item ) == SAME ) break;
    if ( i_iner ) break;
    i++;
  }

  if ( !i_prec ) { /* if no inertia are found, instantiate */
    instantiate_first_parameter( op, constants, constants );
    return;
  }

  for ( i_init = initials; i_init; i_init = i_init->next ) {
    if ( matches( op, i_init->item, i_prec->item, &in_const, constants ) ) {
      help_op = copy_op( op ); 
      for ( i_con=in_const; i_con; i_con=i_con->next ) {
	help_op = copy_replace_op( help_op, i_con->item->item,
				   i_con->item->next->item);
      }
      inertia_instantiate( help_op, i + 1,
			   initials, inertia, constants );
    }
  }

}


BOOLEAN matches( op_list_elt op, token_list fact,
		 token_list condition, fact_list *in_const,
		 fact_list constants )

{

  fact_list result = NULL, temp1;
  token_list temp2, temp3, i_param, i_object;

  if ( !( strcmp( fact->item, condition->item ) == SAME ) )
    return FALSE;

  i_object = fact->next;
  for ( i_param = condition->next; i_param; i_param=i_param->next ) {
    if ( i_param->item[0] == '?' ) {
      if ( same_type( op, i_param->item, i_object->item, constants ) ) {
	temp1 = ( fact_list ) calloc( 1, sizeof( fact_list_elt ) );
	temp2 = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
	temp3 = ( token_list ) calloc( 1, sizeof( token_list_elt ) );
	temp3->item = i_object->item;
	temp3->next = NULL;
	temp2->item = i_param->item;
	temp2->next = temp3;
	temp1->item = temp2;
	temp1->next = result;
	result = temp1;
      } else {
	return FALSE;
      }
    } else {
      if ( !( strcmp( i_param->item, i_object->item ) == SAME ) )
	return FALSE;
    }
    i_object = i_object->next;
  }

  *in_const = result;
  return TRUE;

}


BOOLEAN same_type( op_list_elt op, token param, token object,
		   fact_list constants )

{

  fact_list i, j;

  for ( i = op.params; i; i = i->next )
    {
      if ( strcmp( i->item->item, param ) == SAME ) break;
    }
  if ( !i ) 
    {
      printf("\nfound variable %s not declared as param in %s\n",
	     param, op.name );
      OUTPUT_FILE;
      exit( 1 );
    }

  for ( j = constants; j; j = j->next )
    {
      if ( ( strcmp( j->item->item, object ) == SAME ) ) {
	/* same object found somewhere else */
	if ( display_info > 25 )
	  printf( "found object %s of type %s requested type %s for param %s\n",
		  j->item->item, j->item->next->item, 
		  i->item->next->item, param );

	if ( strcmp( j->item->next->item, i->item->next->item ) == SAME )
	  break;
      }
    }

  if ( j ) {
    return TRUE;
  }
  else
    return FALSE;

}   


/* evaluate an eq() or not-eq() fact */ 
BOOLEAN eq_possible( token_list *conds )
{
  token_list new_start = *conds;
  token_list c, last = NULL;
  int pred_type;

  for(c=*conds; c; c=c->next )
    {
      pred_type = check_eq( c->item );
      if ( pred_type == EQ )
	{
	  if ( !args_eq( (c->item)+3 ) )
	    return FALSE;
	  else
	    {
	      if ( last )
		last->next = c->next;
	      else
		new_start = c->next;
	    }
	}
      else if ( pred_type == NOT_EQ )
	{
	  if ( args_eq( (c->item)+7 ) )
	    return FALSE;
	  else
	    {
	      if ( last )
		last->next = c->next;
	      else
		new_start = c->next;
	    }
	}
      else
	{
	  last = c;
	}
    }
  *conds = new_start;
  return TRUE;
}




/* instantiates first parameter of given op with a possible
 * constant from given list and calls itself recursively
 * with now partially instantiated op, one parameter( the first )
 * and one ( the already used ) constant less.
 *
 * all_constants always contains what its name says, needed later by
 * delete_ALL_quantifying
 */
void instantiate_first_parameter( op_list_elt op,
                                  fact_list constants,
                                  fact_list all_constants )

{

  operator_list operator;
  fact_list i_constant, i_param;
  token_list parameter;
  op_list_elt help_op;
  fact_list help_constants, i_fact;

  for ( i_param=op.params; i_param; i_param=i_param->next ) {
    for ( i_fact=op.params_objects; i_fact; i_fact=i_fact->next ) 
      if ( strcmp( i_param->item->item, i_fact->item->item ) == SAME ) break;
    if ( !i_fact ) break;
  } 
  if ( !i_param ) {
    /*op is instantiated;now delete ALL quantifiing and store in global list*/
    operator = ( operator_list ) calloc( 1, sizeof( operator_list_elt ) );
    operator->name = make_name( op );
    /* check if all variables are initiated */
    check_instantiation(op.preconds, op.name);
    operator->preconditions = token_list_from_fact_list( op.preconds );
    /* if one of the preconditions is an eq/not-eq predicate
       with truth value FALSE the operator can never be applied
       because the precondition will never be true - and if
       it's always true the eq/not-eq fact is tautologic and can
       be left out (it is removed in the eq_possible() function) */
    if ( !eq_possible( &(operator->preconditions) ) )
      return; /* instantiated operator can't be used */ 
    
    operator->effects = delete_ALL_quantifying( op.effects, all_constants, op.name );
    operator->objects = make_objects( op );
    operator->next = operators;
    operators = operator;
    ground_ops_count++;
  } else {
    parameter = i_param->item;
    /* step through possible constants... */
    for ( i_constant = constants; i_constant; i_constant = i_constant->next ) {
      /* step through constants that were already used */
      for ( i_fact=op.params_objects; i_fact; i_fact=i_fact->next ) 
	{ 
	if ( strcmp( i_constant->item->item, i_fact->item->next->item )
	     == SAME ) break;
	}
      /* if a constant was already used try another one, continue loop */
      if ( i_fact ) continue;

      /* if type of parameter == type of i_constant */
      if (strcmp(parameter->next->item, i_constant->item->next->item)==SAME) 
	{
	  /* copy op into help_op, replacing parameter with i_constant
	   * and removing parameter from op.params list
	   */
	  help_op = copy_replace_op( op,parameter->item,
				     i_constant->item->item);
	  
	  /* copy constants into help_constants, removing i_constant */
	  help_constants = copy_remove( constants, i_constant );
	  /* now instantiate next parameter */
	  instantiate_first_parameter( help_op, help_constants, all_constants );
	}
    }
  }

}




/* main function for putting the effect list to the simple
 * inst_effect_list format by putting all possible
 * instantiations of the quantified_variables list
 * into the new effect list.
 */
inst_effect_list delete_ALL_quantifying( effect_list effects,
                                         fact_list constants,
					 char* op_name)

{

  inst_effect_list result, current;

  if ( !effects ) return NULL;

  if ( !effects->quantified_variables ) {
    /* no quantified variables : 
     *  simply put lists to new format and continue
     */
    result = ( inst_effect_list ) calloc( 1, sizeof( inst_effect_list_elt ) );
    /* check if all variables are initiated */
    check_instantiation(effects->conditions, op_name);
    result->conditions = token_list_from_fact_list( effects->conditions);
    /* if one of the conditions is an eq/not-eq predicate
       with truth value FALSE the effect can never be applied
       because the effect condition will never be true - and if
       it's always true the eq/not-eq fact is tautologic and can
       be left out (it is removed in the eq_possible() function) */
    if ( !eq_possible( &(result->conditions) ) )
      result = delete_ALL_quantifying( effects->next, constants, op_name );
    else 
      {
	/* check if all variables are initiated */
	check_instantiation(effects->add_effects, op_name);
	result->add_effects = token_list_from_fact_list( effects->add_effects);
	/* check if all variables are initiated */
	check_instantiation(effects->del_effects, op_name);
	result->del_effects = token_list_from_fact_list( effects->del_effects );
	result->next = delete_ALL_quantifying( effects->next, constants, op_name );
      }
  } else {
    /* initialize new help_inst_effect_list */
    help_inst_effect_list = NULL;
    /* build up global list ( help_inst_effect_list )
     * of all possible instantiations
     * of the quantified variables in *effects
     */
    build_inst_effect_list( *effects, constants, op_name );
    /* store start of this list in result
     * and continue recursively at end of this list
     */
    result = help_inst_effect_list;
    for( current = result; current->next; current = current->next );
    current->next = delete_ALL_quantifying( effects->next, constants, op_name );
  }

  return result;

}


/* builds up global list ( help_inst_effect_list )
 * of possible instantiations of given effect_list_elt
 *
 * method: similar to instantiate_first_parameter:
 *   instantiate first quantified variable with possible
 *   constants out of given list, continue recursively
 *   with partially instantiated effect, one variable and one
 *   constant less.
 *   if there are no quantified variables left, then store result
 *   in global list
 */
void build_inst_effect_list( effect_list_elt effect, fact_list constants, char* op_name )

{

  inst_effect_list help;/* used for storing in global list */
  token_list parameter;/* actual quantified variable */
  fact_list i_constant;/* actual constant */
  effect_list_elt help_effect;/* stores partially instantiated effect */
  fact_list help_constants;/* stores shorter constant list */

  if ( !effect.quantified_variables ) {
    /* effect instantiated; store in global list */
    help = ( inst_effect_list ) calloc( 1, sizeof( inst_effect_list_elt ) );
    /* check if all variables are initiated */
    check_instantiation(effect.conditions, op_name);
    help->conditions = token_list_from_fact_list( effect.conditions );
    /* if one of the conditions is an eq/not-eq predicate
       with truth value FALSE the effect can never be applied
       because the effect condition will never be true - and if
       it's always true the eq/not-eq fact is tautologic and can
       be left out (it is removed in the eq_possible() function) */
    if ( eq_possible( &(help->conditions) ) )
      {
	/* check if all variables are initiated */
	check_instantiation(effect.add_effects, op_name);
	help->add_effects = token_list_from_fact_list( effect.add_effects );
	/* check if all variables are initiated */
	check_instantiation(effect.del_effects, op_name);
	help->del_effects = token_list_from_fact_list( effect.del_effects );
	help->next = help_inst_effect_list;
	help_inst_effect_list = help;
      }
    /* else 
       ...just skip it*/
  } else {
    parameter = effect.quantified_variables->item;
    for ( i_constant = constants; i_constant; i_constant = i_constant->next )
      /* if type of parameter == type of constant */
      if (strcmp(parameter->next->item, i_constant->item->next->item)==SAME) {
        /* instantiate first variable */
        help_effect = copy_replace_effect( effect,
                                           parameter->item,
                                           i_constant->item->item );
        /* remove used constant from list */
        help_constants = copy_remove( constants, i_constant );
        /* continue recursively with new values */
        build_inst_effect_list( help_effect, help_constants, op_name );
      }
  }

}


/* prints list of instantiated operators to stdout
 */
void print_operators( operator_list operators )

{

  operator_list i_operator;
  inst_effect_list i_effect;
  token_list i_token;

  for ( i_operator = operators; i_operator; i_operator = i_operator->next ) {
    printf( "%s\n", i_operator->name );
    printf( "preconditions:\n" );
    for ( i_token = i_operator->preconditions; i_token;i_token=i_token->next)
      printf( "%s ", i_token->item );
    printf( "\neffects:\n" );
    for ( i_effect = i_operator->effects; i_effect;i_effect=i_effect->next) {
      for ( i_token = i_effect->conditions; i_token; i_token = i_token->next )
        printf( "%s ", i_token->item );
      if ( i_effect->add_effects ) {
        printf( "=> ADD " );
        for ( i_token = i_effect->add_effects; i_token;i_token=i_token->next)
          printf( "%s ", i_token->item );
        if ( i_effect->del_effects ) {
          printf( "DEL " );
          for(i_token = i_effect->del_effects; i_token;i_token=i_token->next)
            printf( "%s ", i_token->item );
        }
      } else {
        printf( "=> DEL " );
        for ( i_token = i_effect->del_effects; i_token;i_token=i_token->next)
          printf( "%s ", i_token->item );
      }
      printf( "\n" );
    }
    printf( "\n" );
  }

}
