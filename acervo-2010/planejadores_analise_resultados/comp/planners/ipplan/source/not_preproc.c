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
/* 	$Id: not_preproc.c,v 1.3 1998/05/26 09:24:39 ipp Exp ipp $	 */

#ifndef lint
static char vcid[] = "$Id: not_preproc.c,v 1.3 1998/05/26 09:24:39 ipp Exp ipp $";
#endif /* lint */

#include "ipp.h"

/*
 * function prototypes
 */
token_list get_types_from_constlist(fact_list pred, fact_list var);
token_list copy_token_list(token_list source);
void append_to_effects(token name, token_list args, fact_list* effect);
token_list types_of_pred_args(fact_list predicate, 
			      op_list op, 
			      effect_list eff);
void build_neg_predlist(fact_list pred, token_list f_types);
void store_fact_list(fact_list i, fact_list* start, fact_list* last);
void store_token_list(token_list i, token_list* start, token_list* last);
int not_in_list( token_list pred, fact_list list );
BOOLEAN is_in_negated_preds(token name, fact_list f_list, token_list f_types);

void print_factlist(fact_list list);

/*
 * return a token in which NOT_PRED is replaced by NOT_STR 
 * - in that way building a new (negated) predicate 
 */
token replace_not(token tok)
{
  token result;
  
  result = new_token(1 + strlen( tok ) + strlen( NOT_STR ));

  strcpy( result, NOT_STR );
  strcat( result, tok+1 );

  free(tok);
  return result;
}

/*
 * This function goes over the goals and looks for negated
 * predicates. A global list (negated_preds) is built with 
 * all negated predicates and their types.
 * The NOT symbol will be exchanged with the NOT_STR.
 * Special care is taken of negated eq-predicates.
 */
void transform_goals(void)   
{
  fact_list g; /* walks through conditions and effects */
  effect_list f_goal; /* walks through the original goals */
  token_list f_types; /* holds the list of types for every
		       * predicate; each f_types->item is a type
		       */

  /* walk through all goals */
  for (f_goal = raw_goal_facts; f_goal; f_goal = f_goal->next)
    {
      /* walk through goal conditions */
      for (g = f_goal->conditions; g; g = g->next)
	{
	  /* check if a goal condition is negated */
	  if (NOT_PRED == g->item->item[0])
	    {
	      /* check if the goal condition is "not eq" */
	      if (strcmp(NOT_EQ_PRED, g->item->item))
		{
		  /* if it is negated and is not an eq predicate
		   * get its types and append to the list of
		   * negated predicates(negated_preds)
		   */
		  f_types = 
		    get_types_from_constlist(g, f_goal->quantified_variables);
		  build_neg_predlist(g, f_types);
		}
	      g->item->item = replace_not( g->item->item );
	    }
	}
      /* Walk through add_effects, this is where the actual goal 
       * is saved. Just like the conditions.
       */
      for (g = f_goal->add_effects; g; g = g->next)
	{
	  if (NOT_PRED ==  g->item->item[0])
	    {
	      if (strcmp(NOT_EQ_PRED, g->item->item))
		{
		  /* Here we must look for the types in the global list
		   * of objects and in the quantified variables of that
		   * goal effect, because it could be a quantified goal.
		   */
		  f_types = 
		    get_types_from_constlist(g, f_goal->quantified_variables);
		  build_neg_predlist(g, f_types);
		}
	      g->item->item = replace_not( g->item->item );
	    }
	}
    }
}

/* 
 * This function looks for the types of the arguments of the predicate
 * pred. It looks in the global list orig_constant_list and in the
 * fact_list var. var is either NULL or the list of quantified variables
 * for a given goal effect. 
 * Arguments:
 * fact_list pred: the predicate with its arguments we want the types of
 * fact_list var: a list of variable-type pairs
 *
 * returns: a list of types where every token_list->item a typename is
 */
token_list get_types_from_constlist(fact_list pred, fact_list var)
{
  token_list result = NULL; /* the beginning of the type-list */
  token_list arg; /* arg->item holds the actual variable */
  fact_list f_const;
  token_list t_const;
  token_list f_token; /* temp, a new entry for the list of types */
  token_list last = NULL; /* pointer to the last element 
			   * of the types-list */
  fact_list v; /* traverses the var list, usually quantified variables */

  /* walk through the list of variables of the predicate */
  for (arg = pred->item->next; arg; arg = arg->next)
    {
      /* check if a variable-list is supplied and if the item is 
       * a variable(variables must start with a '?')
       */ 
      if (var && ('?' == arg->item[0]))
	{ /* arg->item is a quantified variable => look in var */
	  for (v = var->next; v; v = v->next)
	    {
	      if (!strcmp(v->item->item, arg->item))
		{
		  /* we found the variable */
		  f_token = new_token_list();
		  f_token->item = new_token(strlen(v->item->next->item)+1);
		  
		  strcpy(f_token->item, v->item->next->item);
		  
		  store_token_list(f_token, &result, &last);
		}
	    }
	}
      /* no variable-list was supplied and predicate argument was 
       * an object => look in the global list of objects
       */
      else
	{
	  /* traverse the global list of all objects, where
	   * the item of f_const is a token_list where the first 
	   * token is the object and the second is the type
	   */
	  for (f_const = orig_constant_list; f_const; f_const = f_const->next)
	    {
	      if (!strcmp(f_const->item->item, arg->item))
		{
		  /* object found */
		  f_token = new_token_list();
		  f_token->item = 
		    new_token(strlen(f_const->item->next->item)+1);
		  
		  strcpy(f_token->item, f_const->item->next->item);
		  
		  store_token_list(f_token, &result, &last);
		}
	    }
	}
    }
  /* return the beginning of the types list */
  return result;
}

/* 
 * we replace "!p" predicate names occurring in preconditions by not-p
 * predicates. If they also occur in ADD effects, the effects need to be 
 * completed. Corresponds exactly to the Gazen/Knoblock Paper at ECP-97 
 */ 
void transform_operators(void)
{
  op_list op; /* the actual operator we manipulate */
  fact_list pred; /* the actual predicate we work on */
  token_list f_types; /* list of types of a predicate */
  /* helper variables for traversing lists or copying strings */
  fact_list pre;
  fact_list f;
  fact_list new;
  fact_list add;
  fact_list f_list;
  effect_list eff;
  effect_list eff_list;
  token_list dummy = NULL;
  token tmp;
  token str1;
  token str2;

  /* traverse the global list of loaded operators, search for 
   * all predicates that appear negated and append them and 
   * their types to the global list negated_preds
   */
  for (op = loaded_ops; op; op = op->next)
    {
      /* traverse the operator preconditions */
      for (pre = op->preconds; pre; pre = pre->next)
	{
	  /* pre->item->item is the name of a predicate */
	  if (NOT_PRED == pre->item->item[0])
	    { 
	      /* the predicate is negated */
	      if (strcmp(NOT_EQ_PRED, pre->item->item))
		{
		  /* The eq-predicate is always ignored, because
		   * we have special eq-preprocessing.
		   * Now get the types of the predicate arguments.
		   * Don't supply an effect(third arg), because
		   * preconditions are not quantified and we only 
		   * have to search in the argument-list of the operator.
		   */ 
		  f_types = types_of_pred_args(pre, op, NULL);
		  build_neg_predlist(pre, f_types);
		}
	      pre->item->item = replace_not(pre->item->item);
	    }
	}
      /* traverse all effects and look in their conditions and their
       * add_effects, because we do not allow DEL-effects anymore
       */
      for (eff = op->effects; eff; eff = eff->next)
	{
	  /* traverse the effect conditions */
	  for (pre = eff->conditions; pre; pre = pre->next)
	    {
	      if (NOT_PRED == pre->item->item[0])
		{
		  if (strcmp(NOT_EQ_PRED, pre->item->item))
		    {
		      /* here we supply the effect(eff), because if
		       * we have a quantified condition we look for
		       * the variables in the quantified_variables
		       * of the effect we are in
		       */
		      f_types = types_of_pred_args(pre, op, eff);
		      build_neg_predlist(pre, f_types);
		    }
		  pre->item->item = replace_not(pre->item->item);
		}
            }
	  /* traverse the ADD-effects (see comments above) */
	  for (add = eff->add_effects; add; add = add->next)
	    {
	      if (NOT_PRED == add->item->item[0])
		{
		  if (strcmp(NOT_EQ_PRED, add->item->item))
		    {
		      f_types = types_of_pred_args(add, op, eff);
		      build_neg_predlist(add, f_types);
		    }
		  /* Here we do not replace the negated sign with
		   * a string, because the manipulations and tests
		   * with the operator effects will get messy.
		   */
/* 		  add->item->item = replace_not(add->item->item); */
		}
	    }
        }
    }

  /* Now traverse negated_preds and modify for every
   * predicate the operator effects if the predicate
   * is in the operator 
   */
  for (pred = negated_preds; pred; pred = pred->next)
    {
      for (op = loaded_ops; op; op = op->next)
	{
	  for (eff_list = op->effects; eff_list; eff_list = eff_list->next)
	    {
	      /* traverse ADD-effects of the operator op */
	      for (f_list = eff_list->add_effects; 
		   f_list; 
		   f_list = f_list->next)
		{
		  /* The ADD-effect is negated.
		   * => replace with negated pred and append to DEL effects
		   */
		  if ((NOT_PRED == f_list->item->item[0]))
		    {
		      append_to_effects(f_list->item->item+1,
					f_list->item->next,
					&eff_list->del_effects);
		      f_list->item->item = replace_not(f_list->item->item);
		    }
		  /* the ADD-effect is not negated but equal to pred
		   * => append the negated predicate to DEL effects
		   */
		  
		  else if ((NOT_PRED != f_list->item->item[0]) &&
			   (!strcmp(f_list->item->item, pred->item->item)))
		    {
		      str1 = new_token(strlen(f_list->item->item)+
				       strlen(NOT_STR) + 1);

		      sprintf(str1, "%s%s", NOT_STR, f_list->item->item);
		      
		      append_to_effects(str1,
					f_list->item->next,
					&eff_list->del_effects);
		    }      
		}
	      /* Now traverse all DEL-effects, although it does not
	       * make sense to negate a DEL-effect; but we allow it.
	       * This works just like the ADD-effects, just 
	       * exchange 'add' and 'del'.
	       */
	      for (f_list = eff_list->del_effects; 
		   f_list; 
		   f_list = f_list->next)
		{
		  /* The DEL-effect is negated.
		   * Here it is not important if pred and eff are equal.
		   * Since all DEL-effects that appear negated, but do
		   * not appear in any precondition or effect-condition,
		   * (hence they are not in negated_preds)
		   * must also be replaced and appended to DEL-effects.
		   */
		  if ((NOT_PRED == f_list->item->item[0]))
		    {
		      append_to_effects(f_list->item->item+1,
					f_list->item->next,
					&eff_list->add_effects);
		      f_list->item->item = replace_not(f_list->item->item);
		    }
		  /* the DEL-effect is not negated but equal to pred */
		  else if ((NOT_PRED != f_list->item->item[0]) &&
			   (!strcmp(f_list->item->item, pred->item->item)))
		    {
		      str2 = new_token(strlen(f_list->item->item)+
				       strlen(NOT_STR) + 1);

		      sprintf(str2, "%s%s", NOT_STR, f_list->item->item);
		      
		      append_to_effects(str2,
					f_list->item->next,
					&eff_list->add_effects);
		    }      
		}
	    }
	}
    }
}

/* Appends a new effect to the list of ADD-effects or
 * DEL-effects. Actually the new effects are not appended
 * but inserted at the beginning.
 * Only effects that are not allready in the list are inserted.
 *
 * name: the name of the new effect
 * args: the arguments of the new effect
 * effect: the effect-structure where the new effect is inserted
 *
 * returns: nothing
 */
void append_to_effects(token name, token_list args, fact_list* effect)
{
  fact_list new_effect;   /* the newly created effect */
  fact_list f_list;       /* traverses effects */
  BOOLEAN insert = TRUE;  /* whether to insert or not */

  /* check if pred is allready in effect-list */
  for (f_list = *effect; f_list; f_list = f_list->next)
    {
      if (is_in_negated_preds(name, f_list, args))
	{
	  insert = FALSE;
	  break;
	}
    }  

  if (insert)
    {
      /* make copy of pred with a list of arguments */
      new_effect = new_fact_list();
      new_effect->item = new_token_list();
      new_effect->item->item = new_token(strlen(name) + 1);
      
      strcpy(new_effect->item->item, name);
      
      /* make a copy of the old argument-list and append it
       * to the effect
       */
      new_effect->item->next = copy_token_list(args);
      
      /* insert into list */
      new_effect->next = *effect;
      *effect = new_effect;
    }
}

/*
 * builds a list of the types of the args of a predicate 
 * the types are searched in the global list of all objects,
 * the operator arguments or the quantified variables of the 
 * effect if an effect is supplied
 *
 * predicate: the predicate and its arguments
 * op: the operator, we found the predicate in
 * eff: the effect, we found the predicate in, optional
 *
 * returns: types_list, a token_list where every token is a type
 */
token_list types_of_pred_args(fact_list predicate, op_list op, effect_list eff)
{
  fact_list var_list;		/* variables of the operator */
  token_list t_list;		/* variables of the predicate */
  token_list types_list = NULL; /* the list of types that is returned */
  token_list new_elem;		/* a new token to be inserted */
  token_list last = NULL;       /* last element of the types list */
  token_list i;                 /* helpers to traverse lists */
  fact_list f_const;
  token_list f_token;
  fact_list q_list;
  BOOLEAN found = TRUE;

  /* 
   * search the arguments of the predicate in 
   * the parameterlist(op->params) of the operator
   * and save their types to types_list
   * 
   * predicate->item->next = first variable of predicate
   * var_list->item->item = a variable of the operator 
   * var_list->item->next->item = type of the above
   */
  /* walk through the list of variables of the predicate */
  for (t_list = predicate->item->next; t_list; t_list = t_list->next)
    {
      found = FALSE;

      /* If we have a quantified effect, we must search for the 
       * variables in the list of the quantified variables.
       * There may also be not fully instantiated predicates
       * => if the variable doesn't start with a '?' look in the 
       * orig_constants for the type of that object. 
       */

      if ('?' != t_list->item[0])
	{
	  /* t_list->item is a constant => search 
	   * in orig_constants
	   */
	  for (f_const = orig_constant_list; f_const; f_const = f_const->next)
	    {
	      if (!strcmp(f_const->item->item, t_list->item))
		{
		  f_token = new_token_list();
		  f_token->item = 
		    new_token(strlen(f_const->item->next->item)+1);
		  
		  strcpy(f_token->item, f_const->item->next->item);
		  
		  store_token_list(f_token, &types_list, &last);
		  found = TRUE;
		  break;
		}
	    }
	}
      else 
	{
	  /* It is a variable, now first look in the quantified_variables
	   * of that effect.
	   */
	  if (eff) /* only search here if eff is supplied */
	    {
	      for (q_list = eff->quantified_variables; 
		   q_list; 
		   q_list = q_list->next)
		{
		  if (!strcmp(q_list->item->item, t_list->item))
		    {
		      f_token = new_token_list();
		      f_token->item = 
			new_token(strlen(q_list->item->next->item)+1);
		      
		      strcpy(f_token->item, q_list->item->next->item);
		      
		      store_token_list(f_token, &types_list, &last);
		      found = TRUE;
		      break;
		    }
		}
	    }
	  /* If we didn't find the variables in the quantified_variables,
	   * we walk through the parameters of the operator 
	   * and search there.
	   */
	  for (var_list = op->params; 
	       !found && var_list; 
	       var_list = var_list->next)
	    {
	      if (!strcmp(t_list->item, var_list->item->item))
		{			/* the variable is found */
		  /* create token */
		  i = new_token_list();
		  i->item = new_token(strlen(var_list->item->next->item)+1);
		  
		  strcpy(i->item, var_list->item->next->item);
		  
		  store_token_list(i, &types_list, &last);
		  found = TRUE;
		  break;
		}
	    }
	}
      /* if no type was found, there was an error! */
      if (FALSE == found)
	{
	  fprintf(stderr, "\a\nipp:   *******************************");
	  fprintf(stderr, "\nipp:   Error in not-preprocessing.");
	  fprintf(stderr, "\nipp:   Type of argument %s for %s was not found.\n", 
		  t_list->item, predicate->item->item);
	}

    }
  /* return the beginning of the type_list */
  return types_list;
}

/*
 * Build list of all negated predicates with the types of their args.
 * negated_preds is a fact_list with the predicate stored in the first 
 * token and the types in the following tokens of the item(which is a
 * token_list).
 * Only predicates that are not allready in the list are inserted.
 */
void build_neg_predlist(fact_list pred, token_list f_types)
{
  token_list pred_types;
  fact_list f_list;
  fact_list new_pred;
  BOOLEAN insert = TRUE;

  /* Special case for first predicate, when negated_preds is NULL */
  if (!negated_preds)
    {
      insert = TRUE;
    }
  else
    {
      /* walk through list and check if predicate is allready in list */
      for (f_list = negated_preds; f_list; f_list = f_list->next)
	{
	  /* the first arg is the predicate name without the '!' => +1 */
	  if (is_in_negated_preds(pred->item->item+1, f_list, f_types))
	    {
	      insert = FALSE;
	      break;
	    }
	}
    }
  
  /* if we found out that the predicate is new => insert it */
  if (insert)
    {
      new_pred = new_fact_list();
      new_pred->item = new_token_list();
      new_pred->item->item = new_token(strlen(pred->item->item+1)+1);

      /* insert name of predicate */
      strcpy(new_pred->item->item, pred->item->item+1);

      /* append the type list of that predicate */
      new_pred->item->next = f_types;

      /* append to list */
      new_pred->next = negated_preds;
      negated_preds = new_pred;
    }
}

/* This function searches for a predicate in negated_preds
 * and takes special care of predicates that have the same
 * name but different types.
 *
 * name: the predicate name (without the NOT in front of it )
 * f_list: the list where we search for the predicate in
 * f_types: a list of the types of the predicate
 *
 * returns: TRUE if the predicate is found in the list. 
 */
BOOLEAN is_in_negated_preds(token name, 
			   fact_list f_list, 
			   token_list f_types)
{
  token_list t_list;          /* holds the types pf the predicate */
  BOOLEAN is_in_list = FALSE; /* the return value */

  if (!strcmp(name, f_list->item->item))
    {
      is_in_list = TRUE;
      /* if the predicate is in the list, we also have to compare
       * the types, because we allow the same predicates with
       * different types
       */
      t_list = f_list->item->next; /* the types of the negated_preds */
      
      /* we asume that the order of the types is always the same,
       * then we can traverse the list in parallel
       */
      while (t_list && f_types)
	{
	  if (!strcmp(t_list->item, f_types->item))
	    {
	      /* if the types are the same, check next type */
	      t_list = t_list->next;
	      f_types = f_types->next;
	      is_in_list = TRUE;
	    }
	  else
	    {
	      is_in_list = FALSE;
	      break;
	    }
	}
      /* now we must check, if one predicate had more variables
       * than the other, although it's not very nice; but we 
       * allow it!
       */
      if (t_list || f_types)
	{
	  /* the first types were equal but one predicate
	   * had more variables => they are different
	   */
	  is_in_list = FALSE;
	}
    }
  return is_in_list;
}

/* 
 * Build a single linked list of token_lists.
 * The new element is appended at the end.
 *
 * i: the token_list that is inserted
 * start: the start of the list where i will be inserted
 * last: the last element of that list
 *
 * returns: nothing
 */
void store_token_list(token_list i, token_list* start, token_list* last)
{
  if (!*last) /* first element */
    {
      *last = i;
      *start = i;
    }
  else
    {
      (*last)->next = i;
    }
  i->next = NULL;
  *last = i;
}


token_list get_objects_of_type( token type_name )
{
  fact_list objs;

  for ( objs = global_object_fl; objs; objs = objs->next )
    {
      if ( strcmp( objs->item->item, type_name ) == SAME )
	/* found list of objects with type type_name, now
	   set objs to the first one */
	break;
    }
  if ( objs )
    return objs->item->next;
  else 
    return NULL;
}

/* uses all objects of a type attaching them to the end
   of every (yet incompletely instantiated) list of 
   predicates. Same method as in rec_build_exgoal_fl() */
fact_list rec_inst_pred( fact_list facts, token_list typelist )
{
  /* facts is a list of incomplete token_lists, which
     is splitted and multiplied so that all objects
     of the next type needed can be concatenated */
  token_list o, objs = NULL;
  token_list end = NULL;
  fact_list t=NULL;
  fact_list result=NULL;

  if ( !typelist )
    return facts;

  /* first search objects of type 'typelist->item'... 
     'types' is a global fact_list built during fact file scanning
     using build_type_list(), each token_list begins
     with a type name followed by all objects of that type */
  for ( t=global_object_fl; t; t=t->next )
    if ( strcmp( t->item->item, typelist->item ) == SAME )
      /* if the list beginning with the
	 right type name is found, continue with 2nd
	 element */
      objs = t->item->next;

  if ( !objs )
    { /* no objects of type typelist->item were found, which may mean
	 that there is a typing error or that there are no objects of
	 that type (which will lead to uninstatiability of the operator) */
      return NULL;
    }
  /* ...then split and copy facts and build a new list for every 
     possible next parameter instatiation */
  result = t = new_fact_list();

  for ( ; facts; facts=facts->next )
    {
      for ( o=objs; o; o=o->next )
	{
	  t->next = new_fact_list();
	  t->next->item = copy_tl_return_end( facts->item, &end );
	  end->next = new_token_list();
	  end->next->item = o->item;
	  t = t->next;
	}
    } 
  return rec_inst_pred( result->next, typelist->next );
}


/* returns a fact_list in which each token_list is one
   fully instantiated predicate */
fact_list instantiate_pred( token name, token_list typelist )
{
  fact_list result;
  
  result = new_fact_list();
  result->item = new_token_list();
  result->item->item = name;
  /* frank memory leak, result geht verloren.
   * es wuerde genuegen nur name zu uebergeben, aber die
   * Funktion rec_inst_pred() braucht eine fact_list, da
   * in rec_inst_pred() die Funktion copy_tl_return_end
   * aufgerufen wird und diese eine fact_list braucht.
   * copy_tl_return_end wird auch von anderen Funktionen
   * benutzt und kann nicht so einfach geaendert werden
   */
  result = rec_inst_pred( result, typelist );
  return result;
}

/* 
 * All predicates that appear negated are fully instantiated and
 * then they are inserted into the orig_initial_facts(global),
 * if they do not appear allready not negated.
 *
 * returns: nothing
 */
void transform_initials()
{
  fact_list i_list=NULL;
  fact_list pred=NULL;
  fact_list new_initial;
  fact_list end = NULL;
  fact_list old_i_list;

  for (pred = negated_preds; pred; pred = pred->next)
    {
      /* get a list with all possible instatiations of actual predicate */
      i_list = instantiate_pred( pred->item->item,
				 pred->item->next);
      
      /* now step through the list, find those facts that
	 are not in initial state and add their negation */
      while (i_list)
	{
	  /* include negations of those instations that do not appear
	     in the initial fact list */
	  if (not_in_list(i_list->item, orig_initial_facts))
	    {
	      /* create negated form of i_list and insert into 
	       * orig_initial_facts
	       */
	      new_initial = new_fact_list();
	      new_initial->item = new_token_list();
	      new_initial->item->item = 
		new_token(strlen(i_list->item->item) + 1 + strlen(NOT_STR));

	      sprintf(new_initial->item->item, 
		      "%s%s", NOT_STR, i_list->item->item);

	      new_initial->item->next = i_list->item->next;

	      new_initial->next = orig_initial_facts;
	      orig_initial_facts = new_initial;

/* 	      free(i_list->item->item); */
	      i_list = i_list->next;
	    }
	  else
	    {
/* 	      old_i_list = i_list; */
	      i_list = i_list->next;
/* 	      free(old_i_list); */
	    }
	}
    }
}

/* Checks if predicate is allready in list, 
 * we have to check the types again...
 *
 * pred: the predicate, we search for
 *       the first token is the name and the following are the arguments
 * list: the list where we search in
 *       every item is a token_list like the above
 *
 * returns: TRUE if the item is not in the list
 */
int not_in_list( token_list pred, fact_list list )
{
  BOOLEAN not_in_list = TRUE; /* the return value */
  fact_list fact;             /* helpers to traverse lists */
  token_list t_list;
  token_list f_pred;

  /* traverse the list where we search a predicate */
  for (fact = list; fact; fact = fact->next)
    {
      /* stop if we found the predicate in the list */
      if (FALSE == not_in_list)
	{
	  break;
	}

      /* use a helper variable to keep pred */
      f_pred = pred;

      /* traverse the items of the fact_lists */
      for (t_list = fact->item; t_list && f_pred; t_list = t_list->next)
	{
	  if (!strcmp(t_list->item, f_pred->item))
	    {
	      /* if the name of the predicate is equal
	       * traverse the arguments and compare them
	       */
	      f_pred = f_pred->next;
	      not_in_list = FALSE;
	    }
	  else
	    {
	      /* we didn't find it, stop */
	      not_in_list = TRUE;
	      break;
	    }
	}
    }

  return not_in_list;
}

/* 
 * do several changes to the loaded goals, initials and
 * operators to replace NOT and enable ipp to handle
 * all kinds of negated predicates 
 */
void preprocess_not(void)
{
  fact_list i_list;
  token_list i_token;

  /* only removes not in goal predicates 
     globals changed: raw_goal_facts */ 
  transform_goals(); 
  
  /* removes not in ops and completes effects, 
     globals changed: loaded_ops */
  transform_operators(); 

  /* adds new not-predicates to initital state, 
     globals changed: orig_initial_facts */
  transform_initials(); 

  /* display info on the negated predicates */
  if (6 == display_info)
    {
      printf("\nThe negated predicates and their types:\n");
      for ( i_list = negated_preds; i_list; i_list = i_list->next ) 
	{
	  for ( i_token = i_list->item; i_token; i_token = i_token->next )
	    {
	      printf( "%s ", i_token->item );
	    }
	  printf("\n");
	}
      printf("\nInitial facts (after adding negated predicates):\n");
      print_factlist( orig_initial_facts );
    }
}
