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

/* 	$Id: eq_preproc.c,v 1.6 1998/05/29 13:43:39 ipp Exp $	 */

#ifndef lint
static char vcid[] = "$Id: eq_preproc.c,v 1.6 1998/05/29 13:43:39 ipp Exp $";
#endif /* lint */


#include"ipp.h"/* defines, data structures, fn prototypes, global variables */

/* main function for reducing given list to
 * instantiable operators;
 * called by main ( in file plan.c )
 */
void remove_uninstantiable_ops( op_list *ops, fact_list constants )

{

  if ( *ops ) {/* still something to do */
    if ( remove_able( *ops, constants ) ){
      /* remove this operator by assigning it the value of
       * it's successor
       */
      *ops = (*ops)->next;
      /* remove uninstantiable operators in rest of list */
      remove_uninstantiable_ops( ops, constants );
    } else {
      /* leave this op untouched and continue with rest of list */
      remove_uninstantiable_ops( &((*ops)->next), constants );
    }
  }

}

/* helpfunction for remove_uninstantiable_ops:
 *   returns TRUE gdw op cannot be instantiated
 */
BOOLEAN remove_able( op_list op, fact_list constants )

{

  fact_list parameter;/* index for currently examined parameter */
  BOOLEAN result = FALSE;/* that's the result of the test */

  /* check the parameterlist of op */
  for( parameter = op->params; parameter; parameter = parameter->next ) {
    if ( cannot_instantiate( parameter->item, constants ) ) {
      result = TRUE;/* found an uninstantiable parameter */
      break;
    }
  }

  /* remove the uninstantiable effects; if these are all effects,
   * op can as well be removed
   */
  remove_effects( &(op->effects), constants );
  if ( !op->effects ) result = TRUE;

  return result;

}

void remove_effects( effect_list *effects, fact_list constants )

{

  fact_list parameter;

  if ( *effects ) {/* still something to do */
    for ( parameter = (*effects)->quantified_variables;
          parameter; parameter = parameter->next )
      if ( cannot_instantiate( parameter->item, constants ) ) break;
    if ( parameter ) {
      /* remove this effect by assigning it the value of
       * it's successor
       */
      *effects = (*effects)->next;
      /* remove uninstantiable operators in rest of list */
      remove_effects( effects, constants );
    } else {
      /* leave this effect untouched and continue with rest of list */
      remove_effects( &((*effects)->next), constants );
    }
  }

}


/* helpfunction for remove_able:
 *   returns TRUE gdw there's no matching constant for parameter
 */
BOOLEAN cannot_instantiate( token_list param, fact_list constants )

{

  fact_list i_constant;/* index for currently examined constant */
  BOOLEAN result = TRUE;/* that's the result of the test */


  /* check all the constants in given list */
  for( i_constant = constants; i_constant; i_constant = i_constant->next ) {
    if ( strcmp( i_constant->item->next->item, param->next->item ) == SAME ) {
      result = FALSE;/* found one that matches */
      break;
    }
  }

  return result;
}



/* some helpfunctions - allocate memory for new list elements */

meta_fact_list new_meta_fact_list()
{
  meta_fact_list result;
  result = ( meta_fact_list ) malloc( sizeof( meta_fact_list_elt ) );
  result->item = NULL; result->next = NULL;
  return result;
}

/* returns an integer describing if the predicate
   is 'eq', 'not-eq' or something else */
int check_eq( token f )
{
  if ( strncmp( f, EQ_STR, strlen( EQ_STR ) ) == SAME )
      return EQ;
  if ( strncmp( f, NOT_EQ_STR, strlen( NOT_EQ_STR ) ) == SAME )
      return NOT_EQ;
  return ANY_PRED;
}


/* checks if a token consists of two equal strings
   dividided by CONNECTOR */
BOOLEAN args_eq( token two_args )
{
  int pos;
  
  for( pos=1; two_args[pos-1]!=CONNECTOR[0]; pos++ )
    ;
  /* step through both parts of the string until
     end is reached (=equal) or difference
     is detected (=different) */
  while ( two_args[pos] == two_args[0] )
    two_args++;
  if ( two_args[pos] == 0 && two_args[0] == CONNECTOR[0])
    return TRUE;
  else 
    return FALSE;
}



/* tests if conds are contained in the initial facts 
   or if an 'eq()' or 'not-eq()' predicate is false */
BOOLEAN cond_in_initial( token_list conds, token_list initials )
{
  token_list i_c, i_i;
  int pred_type;

  for ( i_c = conds; i_c; i_c=i_c->next ) 
    {
      /* check if eq or not-eq */
      pred_type = check_eq( i_c->item );
      if ( pred_type == EQ )
	{ /* predicate is 'equal' but arguments are different */
	  if ( !args_eq( (i_c->item)+strlen( EQ_STR ) ) )
	    return FALSE;
	}
      else if ( pred_type == NOT_EQ )
	{ /* predicate is 'not-equal' but arguments are the same */
	  if ( args_eq( (i_c->item)+strlen( NOT_EQ_STR ) ) )
	    return FALSE;
	}
      else
	{ /* predicate is neither 'eq' nor 'not-eq',
	   so check if in initial state */
	  for ( i_i = initials; i_i; i_i=i_i->next )
	    if ( strcmp( i_i->item, i_c->item ) == SAME ) break;
	  if ( !i_i ) return FALSE;
	}
    }
  return TRUE;
}



/* make copy of a token_list and save the end of that
   list (...to attach further elements) */
token_list copy_tl_return_end( token_list tl, token_list *end )
{
  token_list t, start;
  
  *end = NULL;
  start = t = new_token_list();
  for( ; tl; tl = tl->next )
    {
      t->next = new_token_list();
      t = t->next;
      t->item = tl->item;
      if ( !tl->next )
	{
	  *end = t;
	}
    }
  return start->next;

}




/**********************************************************************/
/**********************************************************************/
/**********************************************************************/



void preprocess_pl1_facts( void )
{
  /* step through all operator pre- and effect conditions and
     transform these condtions into a format which is processable
     for ipp. */
  loaded_ops = rec_prepoc_op_conditions( loaded_ops );
}


op_list rec_prepoc_op_conditions( op_list op )
{
  op_list result = NULL, cur_op, next_op;
  BOOLEAN splitted = FALSE;
  
  if ( !op )
    return NULL;
  next_op = op->next;
  op->next = NULL;
  
  /* first get a normal form for the effect conditions, if 
     there are any */
  op->effects = rec_get_normal_form_effectcond( op->effects );
  if ( op->effects )
    {
      result = op;
    }
 

  /* then check the preconditions. attention: here new operators
     are built, the old one may be destroyed */
  result = rec_get_normal_form_precond( op ); 

  /* now do the same recursively to the operators that followed
     in the OLD operator list */
  if ( result )
    {
      for ( cur_op=result; cur_op->next; cur_op = cur_op->next )
	; 
      cur_op->next = rec_prepoc_op_conditions( next_op );
    }
  else
    result = rec_prepoc_op_conditions( next_op );
  return result;
}


op_list rec_get_normal_form_precond( op_list op )
{
  op_list result, cur_op, end = NULL, next_op;
  token name;
  int i;
  fact_list end_dummy;

  if ( !op )
    return NULL;
  next_op = op->next;

  if ( !op->preconds )
    { /* if there are no preconditions just skip this one */
      op->next = rec_get_normal_form_precond( next_op );
      return op;
    }

  /* there is at least one precondition which is in pl1 format at the moment,
     now do some transformations to bring it into ipp format.
     Some transformations will leed to operator splitting, so we need
     to add numbers to their names. those numbers will be hidden during
     plan printing and nobody will notice that there are different ops !*/
  name = new_token( 1+strlen(op->name)+strlen(HIDDEN_STR)+3 );
  strcpy( name, op->name );

  /* bring NOT inside */
  op->preconds = transform_to_atomic_negation( op->preconds, FALSE );
  /* now do the real work: eliminate FORALL, EXISTS, OR (IMPLY A B was
   tranformed to not A OR B already) */
  op->preconds = eliminate_quantifiers( op->preconds, &end_dummy );
  result = rec_remove_quants_from_precond( &op->preconds, op );

  /* now do the same recursively to the ops that followed
     in the OLD op list */
  if ( result )
    {
      for ( cur_op=result, i=0; cur_op; cur_op=cur_op->next, i++ )
	{
	  if ( !cur_op->next )
	    end = cur_op;
	  /* while searching the end, adjust the operator names */
	  cur_op->name = new_token( 1+strlen(op->name)+strlen(HIDDEN_STR)+3 );
	  if ( !i )
	    { /* no numbering for the first (maybe only) one */
	      sprintf( cur_op->name, "%s", name ); 
	    }
	  else
	    {
	      sprintf( cur_op->name, "%s%s%d", name, HIDDEN_STR, i);
	    }
	}
      end->next = rec_get_normal_form_precond( next_op );
    }
  else
    {
      result = rec_get_normal_form_precond( next_op );
    }
  return result;
}


effect_list rec_get_normal_form_effectcond( effect_list eff )
{
  effect_list result, cur_eff, next_eff;
  fact_list end_dummy;

  if ( !eff )
    return NULL;
  next_eff = eff->next;
  eff->next = NULL;

  if ( !eff->conditions )
    { /* if there are no effect conditions just skip this one */
      eff->next = rec_get_normal_form_effectcond( next_eff );
      return eff;
    }

  /* there is a condition which is in pl1 format at the moment,
     now do some transformations to bring it into ipp format.
     Some tansformations will leed to a splitting-up of conditional
     effects so that the operator will have more than one
     conditional effect from the current one */

  /* bring NOT inside */
  eff->conditions = transform_to_atomic_negation( eff->conditions, FALSE );
  /* now do the real work: eliminate FORALL, EXISTS, OR (IMPLY A B was
   tranformed to not A OR B already) */
  eff->conditions = eliminate_quantifiers( eff->conditions, &end_dummy );
  result = rec_remove_quants_from_effectcond( &eff->conditions, eff );

  /* now do the same recursively to the effects that followed
     in the OLD effect list */
  if ( result )
    {
      for ( cur_eff=result; cur_eff->next; cur_eff = cur_eff->next )
	;
      cur_eff->next = rec_get_normal_form_effectcond( next_eff );
    }
  else
    result = rec_get_normal_form_effectcond( next_eff );
  return result;
}


fact_list transform_to_atomic_negation( fact_list f, BOOLEAN neg )
{
  int c;
  fact_list result;
  token t, td;

  if ( !f )
    return NULL;

  /* find out the first item in f */
  c = get_adl_token( f );

  result = f;
  switch ( c )
    {
    case LIT_CONST:
      /* it'a literal. if neg == TRUE, it must be negated */
      if ( neg )
	{
	  if ( f->item->item[0] == '!' )
	    {
	      t = new_token( strlen(f->item->item)-1+1 );
	      strcpy( t, (f->item->item)+1 );
	      free( f->item->item );
	      f->item->item = t;
	    }
	  else
	    {
	      t = new_token( strlen(f->item->item)+1+1 );
	      *t = '!';
	      strcpy( t+1, f->item->item );
	      free( f->item->item );
	      f->item->item = t;
	    }
	}
      result->next = transform_to_atomic_negation( f->next, neg );
      break;
    case VAR_CONST: 
    case LBRACK_CONST: 
    case RBRACK_CONST:
      /* do nothing */
      result->next = transform_to_atomic_negation( f->next, neg );
      break;
    case AND_CONST:
      if ( neg )
	{
	  result = make_adl_fact( OR_CONST );
	  result->next = transform_to_atomic_negation(f->next,neg );
	  f->next = NULL;
	  free_complete_fact_list( f );
	}
      else
	{
	  result->next = transform_to_atomic_negation( f->next, neg );
	}
      break;
    case OR_CONST:
      if ( neg )
	{
	  result = make_adl_fact( AND_CONST );
	  result->next = transform_to_atomic_negation(f->next,neg );
	  f->next = NULL;
	  free_complete_fact_list( f );
	}
      else
	{
	  result->next = transform_to_atomic_negation( f->next, neg );
	}
      break;
    case EXISTS_CONST:
      if ( neg )
	{
	  result = make_adl_fact( FORALL_CONST );
	  result->next = transform_to_atomic_negation(f->next,neg );
	  f->next = NULL;
	  free_complete_fact_list( f );
	}
      else
	{
	  result->next = transform_to_atomic_negation( f->next, neg );
	}
      break;
    case FORALL_CONST:
      if ( neg )
	{
	  result = make_adl_fact( EXISTS_CONST );
	  result->next = transform_to_atomic_negation(f->next,neg );
	  f->next = NULL;
	  free_complete_fact_list( f );
	}
      else
	{
	  result->next = transform_to_atomic_negation( f->next, neg );
	}
      break;
    case NOT_CONST:
      /* drop NOT here and move it into the literals */
      result = transform_to_atomic_negation( f->next, 
					     neg ? FALSE : TRUE );
      f->next = NULL;
      free_complete_fact_list( f );
      break;
    case ENDNOT_CONST:
      /* NOT scope is over */
      result = transform_to_atomic_negation( f->next, 
					     neg ? FALSE : TRUE ); 
      f->next = NULL;
      free_complete_fact_list( f );
      break;
    default:
      printf( "error: unknown pl1 constant detected: %d\n", c );
      OUTPUT_FILE;
      exit( 1 );
      break;
    }

  return result;
}

/* f is a first order logic expression, *end will hold the last
   processed item after this function was run, i.e. (*end)->next
   will point to the next item that was not processed yet */
fact_list eliminate_quantifiers( fact_list f, fact_list *end )
{
  int c;
  fact_list result, vars, v, expr, tmp, following, *vinst_fl;
  token_list ol, o;

  if ( !f )
    return NULL;

  /* find out which token comes next */
  c = get_adl_token( f );
  *end = f;

  switch ( c )
    {
    
    case LIT_CONST:
      /* if the actual fact is a simple literal => return it */
      return f;
      break;

    case AND_CONST:
    case OR_CONST:
      /* if it's AND or OR, that's okay, but eliminate quants in the 
	 arguments to AND... */
      while ( get_adl_token((*end)->next) != RBRACK_CONST )
	{
	  (*end)->next = eliminate_quantifiers( (*end)->next, &tmp );
	  *end = tmp;
	}
      /* now *end points to the closing AND bracket */
      *end = (*end)->next;
      return f;

    case FORALL_CONST:
    case EXISTS_CONST:
      /* we have to get the variables bound by the quant, then get
	 the (already quantifier-free) expression and copy it
	 for each possible instantiation of the variable. Finally
	 build the conjuction over all of the new expressions */
      if ( c == FORALL_CONST )
	{
	  result = make_adl_fact( AND_CONST );
	}
      else
	{
	  result = make_adl_fact( OR_CONST );
	}
      *end = f->next; /* skip quantifier and left bracket */
      vars = get_variables( end );
      /* after getting the variables, end points to the expression */
      expr = eliminate_quantifiers( *end, &tmp );
      following = tmp->next;
      tmp->next = NULL;
      /* end points to OR/AND - (*end)->next will be the point where
	 all possible instatiations will be appended */
      for ( v = vars; v; v = v->next )
	{
	  if ( !( ol = type_already_known( v->item->next->item, 
					   global_object_fl ) ) )
	    {
	      printf( "error: type %s for %s not specified.\n",
		      v->item->next->item,  v->item->item );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  vinst_fl = &(result->next);
	  for ( o = ol; o; o = o->next )
	    { /* instatiate v with o */
	      *vinst_fl = copy_complete_fact_list( expr, &tmp );
	      replace_in_fl( v->item->item, o->item, *vinst_fl );
	      vinst_fl = &(tmp->next);
	    }
	  /* now variable v is instatiated, the list of facts was
	     blown up... but our work is yet to start: instantiate
	     the others vars in new new list */
	  expr = result->next;
	  *end = tmp;
	}


      (*end)->next = make_adl_fact( RBRACK_CONST ); /* close AND/OR */
      *end = (*end)->next;
      (*end)->next = following;
      return result;
      break;
    default: 
      printf( "\nstrange first order object %d!\n", c );
      OUTPUT_FILE;
      exit( 1 );
    }
}


effect_list rec_remove_quants_from_effectcond( fact_list* cond,
					       effect_list orig_eff )
{
  effect_list result, el, end;
  fact_list vl, tmp;
  int c;
  
  if ( !(*cond) )
    {
      /* recursion should be ended by the last bracket */
      printf( "error: effect condition is no correct pl1 expression\n" );
      OUTPUT_FILE;
      exit( 1 );
    }

  c = get_adl_token( *cond );

  switch ( c )
    {
    case RBRACK_CONST:
      printf( "\nerror: adl preprocessing went wrong. debug me.\n" );
      OUTPUT_FILE;
      exit ( 1 );
      break;
    case LIT_CONST:
      /* this is the only point where really new effects are produced */
      el = new_effect_list();
      el->quantified_variables = 
	copy_complete_fact_list( orig_eff->quantified_variables, &tmp );
      el->add_effects = copy_complete_fact_list( orig_eff->add_effects, &tmp );
      el->del_effects = copy_complete_fact_list( orig_eff->del_effects, &tmp );
      /* el->next is NULL, now set one single condition */
      el->conditions = *cond;
      /* no copying of *cond necessary here */
      *cond = (*cond)->next;
      el->conditions->next = NULL;
      result = el;
      break;
    case AND_CONST:
      /* skip AND_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      /* get one of the conjunctive effects after another */
      result = rec_remove_quants_from_effectcond( cond, orig_eff );
      for( ; result && (RBRACK_CONST != get_adl_token( *cond )); )
	{ /* still AND */
	  el = rec_remove_quants_from_effectcond( cond, orig_eff );
	  if ( !el )
	    { /* if one of the conjunctive effects is not possible
		 the whole conjunction is not possible */
	      result = NULL;
	      break;
	    }
	  if ( !(*cond) )
	    {
	      printf( "error: AND clause must be terminated with ')'\n" );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  /* build the cartesian product of the elements (elementary
	   operation is conjunction) */
	  result = multiply_effectconds( result, el );
	}
      /* skip RBRACK_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      break;
    case OR_CONST:
      /* skip OR_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      /* get one of the disjunctive effects after another */
      result = end = NULL;
      for( ; RBRACK_CONST != get_adl_token( *cond ); )
	{ /* still OR */
	  el = rec_remove_quants_from_effectcond( cond, orig_eff );
	  if ( !(*cond) )
	    {
	      printf( "error: OR clause must be terminated with ')'\n" );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  if ( !result )
	    {
	      if ( el )
		result = end = el;
	    }
	  else
	    end->next = el;
	  if ( end )
	    for ( ; end->next; end = end->next )
	      ;
	}
      /* skip RBRACK_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      break;
    case EXISTS_CONST:
    case FORALL_CONST:
      printf( "\nerror: quantifier was not eliminated during preprocessing." );
      OUTPUT_FILE;
      exit( 1 );
      break;

    }
  return result;
}


op_list rec_remove_quants_from_precond( fact_list* cond,
					op_list orig_op )
{
  op_list result, ol, end;
  fact_list vl, tmp;
  effect_list e;
  int c;
  
  if ( !(*cond) )
    {
      /* recursion should be ended by the last bracket */
      printf( "error: precondition is no correct pl1 expression\n" );
      OUTPUT_FILE;
      exit( 1 );
    }

  c = get_adl_token( *cond );

  switch ( c )
    {
    case RBRACK_CONST:
      printf( "\nerror: parsing adl expression in precond of %s went wrong. debug me.\n", orig_op->name );
      OUTPUT_FILE;
      exit ( 1 );
      break;
    case LIT_CONST:
      /* this is the only point where really new ops are produced */
      ol = new_op_list( NULL );
      ol->params = 
	copy_complete_fact_list( orig_op->params, &tmp );
      ol->effects = copy_complete_effect_list( orig_op->effects, &e );
      /* ol->next is NULL, now set one single condition */
      ol->preconds = *cond;
      /* no copying of *cond necessary here */
      *cond = (*cond)->next;
      ol->number_of_real_params = orig_op->number_of_real_params;
      ol->preconds->next = NULL;
      result = ol;
      break;
    case AND_CONST:
      /* skip AND_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      /* get one of the conjunctive effects after another */
      if (RBRACK_CONST != get_adl_token( *cond ))
	result = rec_remove_quants_from_precond( cond, orig_op );
      else
	return copy_complete_op( orig_op );
      for( ; result && (RBRACK_CONST != get_adl_token( *cond )); )
	{ /* still AND */
	  ol = rec_remove_quants_from_precond( cond, orig_op );
	  if ( !ol )
	    { /* if one of the conjunctive effects is not possible
		 the whole conjunction is not possible */
	      result = NULL;
	      break;
	    }
	  if ( !(*cond) )
	    {
	      printf( "error: AND clause must be terminated with ')'\n" );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  /* build the cartesian product of the elements (elementary
	   operation is conjunction) */
	  result = multiply_preconds( result, ol );
	}
      /* skip RBRACK_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      break;
    case OR_CONST:
      /* skip OR_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      /* get one of the disjunctive effects after another */
      result = end = NULL;
      for( ; RBRACK_CONST != get_adl_token( *cond ); )
	{ /* still OR */
	  ol = rec_remove_quants_from_precond( cond, orig_op );
	  if ( !(*cond) )
	    {
	      printf( "error: OR clause must be terminated with ')'\n" );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	  if ( !result )
	    {
	      if ( ol )
		result = end = ol;
	      /* if ( !el ): just ignore if there's no possibility */
	    }
	  else
	    end->next = ol;
	  if ( end )
	    for ( ; end->next; end = end->next )
	      ;
	}
      /* skip RBRACK_CONST */
      tmp = *cond;
      *cond = (*cond)->next;
      free( tmp );
      break;
    case EXISTS_CONST:
    case FORALL_CONST:
      printf( "\nerror: quantifier was not eliminated during preprocessing." );
      OUTPUT_FILE;
      exit( 1 );
      break;

    }
  return result;
}

fact_list get_variables( fact_list* last )
{
  fact_list f = *last, result = (*last)->next, tmp;
  int c;
  
  /* first fact in *last is a left bracket */
  for ( *last = f; (*last)->next; *last = (*last)->next )
    {
      c = get_adl_token((*last)->next);
      if ( RBRACK_CONST == c )
	break;
      if ( VAR_CONST != c )
	{
	  printf( "\nerror: non-variable (%s) in parameter list: ",
		adl_string[c] );  
	  printf ( "'%s'\n", (*last)->next->item->item );
	  OUTPUT_FILE;
	  exit( 1 );
	}
    }
  if ( !((*last)->next) )
    {
      printf( "\nerror: variable list doesn't end with ')'\n" );
      printf( "\nbut ends with %s", adl_string[c] );
      printf ( ": %s...\n", (*last)->item->item );
      print_factlist( result );
      OUTPUT_FILE;
      exit( 1 );
    }
  /* up to this point we have a list of variables */
  tmp = (*last)->next;
  (*last)->next = NULL; 
  *last = tmp;
  /* skip bracket */
  tmp = *last;
  *last = (*last)->next;
  free( tmp );
  return result;
}





void replace_in_fl( token old, token new, fact_list source )
{
  fact_list f;
  token_list t;
  token n;

  int len = strlen( new );
  for ( f = source; f; f = f->next )
    {
      for ( t = f->item; t; t = t->next )
	{
	  if ( strcmp( t->item, old ) == SAME )
	    { 		  
	      n = new_token( len );
	      strcpy( n, new );
	      free( t->item );
	      t->item = n;
	    }
	}
    }
}



effect_list multiply_effectconds( effect_list old1, effect_list old2 )
{
  effect_list result = NULL, tmp1, tmp2, end, new_end;
  fact_list last_cond, dummy;

  for ( tmp1 = old1; tmp1; tmp1 = tmp1->next )
    {
      if ( !result )
	result = tmp2 = copy_complete_effect_list( old2, &end );
      else
	{
	  end->next = tmp2 = copy_complete_effect_list( old2, &new_end );
	  end = new_end;
	}
      for ( ; tmp2; tmp2 = tmp2->next )
	{
	  if ( tmp2->conditions )
	    {
	      for ( last_cond=tmp2->conditions; last_cond->next; 
		    last_cond = last_cond->next )
		;
	      last_cond->next = copy_complete_fact_list(tmp1->conditions, 
							&dummy);
	    }
	  else
	    tmp2->conditions = copy_complete_fact_list(tmp1->conditions, 
							&dummy);
	}
    }
  
  free_complete_effect_list( old1 );
  free_complete_effect_list( old2 );
  
  return result;
}


op_list multiply_preconds( op_list old1, op_list old2 )
{
  op_list result = NULL, tmp1, tmp2, end, new_end;
  fact_list last_cond, dummy;

  for ( tmp1 = old1; tmp1; tmp1 = tmp1->next )
    {
      if ( !result )
	result = tmp2 = copy_complete_op_list( NULL, old2, &end );
      else
	{
	  end->next = tmp2 = copy_complete_op_list( NULL, old2, &new_end );
	  end = new_end;
	}
      for ( ; tmp2; tmp2 = tmp2->next )
	{
	  if ( tmp2->preconds )
	    {
	      for ( last_cond=tmp2->preconds; last_cond->next; 
		    last_cond = last_cond->next )
		;
	      last_cond->next = copy_complete_fact_list(tmp1->preconds, 
							&dummy);
	    }
	  else
	    tmp2->preconds = copy_complete_fact_list(tmp1->preconds, 
							&dummy);
	}
    }
  
  free_complete_op_list( old1 );
  free_complete_op_list( old2 );
  
  return result;
}



/**********************************************************************/
/* now some stuff for axioms                                          */
/**********************************************************************/

token_list get_predicate_names_from( fact_list f )
{
  token_list t, result = NULL;

  for ( ; f; f = f->next )
    {
      if ( LIT_CONST == get_adl_token( f ) )
	{
	  t = new_token_list();
	  t->item = new_token( strlen( f->item->item ) + 1 );
	  strcpy( t->item, f->item->item );
	  t->next = result;
	  result = t;
	}
    }
  return result;
}


BOOLEAN axiom_context_in_op_effect( fact_list pre, fact_list eff )
{
  token_list pre_preds, cur_pre;
  token_list eff_preds, cur_eff;

  pre_preds = get_predicate_names_from( pre );
  eff_preds = get_predicate_names_from( eff );
  for ( cur_pre = pre_preds; cur_pre; cur_pre = cur_pre->next )
    {
      for ( cur_eff = eff_preds; cur_eff; cur_eff = cur_eff->next )
	{
	  if ( strcmp( cur_pre->item, cur_eff->item ) == SAME )
	    return TRUE;
	}
    }
}


void preprocess_axioms()
{
  op_list cur_axiom, next_axiom;
  op_list cur_op;
  int c;
  token s;
  effect_list new_effect;
  fact_list dummy;

  for ( cur_axiom = loaded_axioms; cur_axiom; cur_axiom = next_axiom )
    {
      next_axiom = cur_axiom->next;
      /* first find the predicate added by this axiom */
      if ( cur_axiom->effects->add_effects )
	{
	  c = get_adl_token( cur_axiom->effects->add_effects );
	  if ( c != LIT_CONST )
	    { /* this should NEVER happen because axioms are only
		 allowed to have one single unnegated literal effect */
	      printf( "error: effect of axiom %s is incorrect.\n",
		      cur_axiom->name );
	      OUTPUT_FILE;
	      exit( 1 );
	    }
	}
      for ( cur_op = loaded_ops; cur_op; cur_op = cur_op->next )
	{
	  if ( axiom_context_in_op_effect( cur_axiom->preconds, 
					   cur_op->effects->add_effects ) )
	    {
	      token s;
	      fact_list v;
	      /* make a new effect: 
		 forall (params of axiom): add not(effect of axiom) */ 
	      new_effect = new_effect_list();
	      new_effect->del_effects = 
		copy_complete_fact_list( cur_axiom->effects->add_effects, 
					 &dummy );
	      new_effect->quantified_variables =
		copy_complete_fact_list( cur_axiom->params, &dummy );
	      for ( v = new_effect->quantified_variables; v; v = v->next )
		{
		  /* for substitution build new var names */
		  s = new_token( strlen(v->item->item)+2 );
		  sprintf( s, "?%s%s", HIDDEN_STR, v->item->item+1 );
		  replace_in_fl( v->item->item, s, new_effect->del_effects );
		  replace_in_fl( v->item->item, s, v );
		}
	      new_effect->next = cur_op->effects;
	      cur_op->effects = new_effect;
	    }
	}
      /* finally add axiom as operator to loaded_ops */
      cur_axiom->next = loaded_ops;
      loaded_ops = cur_axiom;
    }
}


/****************************************************************/

op_list conjuctive_goals( op_list the_ops, op_list *pred_address )
{
  op_list op, goal_op = NULL;

  if ( strncmp( the_ops->name, GOAL_OP_STR, strlen( GOAL_OP_STR ) )
       == SAME )
    goal_op = the_ops;
  for( op = the_ops; op->next; op = op->next )
    {
      if ( strncmp( op->next->name, GOAL_OP_STR, strlen( GOAL_OP_STR ) )
	   == SAME )
	{
	  if ( goal_op )
	    /* this is not the first goal op we found -> disjunctive
	       goals -> no possibility for simple fact_list goal_facts,
	       sorry GAM... */
	    return NULL;
	  else
	    {
	      goal_op = op->next;
	      *pred_address = op;
	    }
	}
    }
  if ( goal_op )
    /* exactly ONE goal op. Great. GAM may be used */
    return goal_op;
  printf( "\nerror: no goals specified.\n" );
  OUTPUT_FILE;
  exit( 1 );
} 
