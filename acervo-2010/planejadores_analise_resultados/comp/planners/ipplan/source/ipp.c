/* Test version using lex&yacc files */




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
 * main routine for extended graphplan algorithm
 *
 * basic algorithm written feb/mar/apr 1997 by joerg hoffmann
 *
 * inspired by graphplan and jana koehler
 *
 * does the following:
 *
 *           -  reads in specified operator and fact files
 *           -  removes uninstantiable operators
 *           -  calculates all instantiations of remaining operators
 *           -  builds graph until non-exclusive goals are reached first time
 *           -  searches for a plan:
 *                while ( not found plan at time ) do
 *                  build next graph layer;
 *                  time++;
 *                end
 *           -  prints final information to stdout
 *
 * additional features:
 * 
 *       by frank rittinger:
 *
 *           -  saves graph structure into text file for display, if wanted  
 *
 *       by michael brenner:
 *
 *           - removing irrelevant facts and operators. written may/june 1997
 *             inspired by theoretical works by bernhard nebel:
 *             powerful heuristics to deal with unnecessary information
 *             which would expand the graph and make problem unsolvable
 */


#include "ipp.h" /* defines, data structures, fn prototypes, global variables */
#include "rifo.h" /* all definitions for removing irrelevants needed by the files:
		    fbackchain.c, sets.c, rifohash.c, rifoutils.c, rifoio.c */

/*
 * global variables
 */


/* technical variables */
char *act_filename;
int lineno = 1;
inst_effect_list help_inst_effect_list;/* used for del_ALL_quantifiing */
BOOLEAN minimize = TRUE;/* has to do with recursive op choice in fn search */
int total_time=0;
struct tms gstart, gend; /* helpers */

/* globally important variables */

/* domain constants */
char *gdomain_name;
op_list loaded_ops;/* loaded, uninstantiated operators */
op_list loaded_axioms;/* axioms as in UCPOP before being changed to ops */
operator_list operators;/* list of instantiated operators */
token_list initial_facts;/* the initial facts */
effect_list raw_goal_facts;/* not yet preprocessed goal facts */
token_list goal_facts;/* the goal facts */
fact_list orig_constant_list;/* to store all typed objects */
fact_list orig_initial_facts;/* stores initials as fact_list */
fact_list negated_preds = NULL;/* needed for NOT preprocessing */ 
fact_list global_object_fl;/* fast finding of types and their objs */
type_tree_list global_type_tree_list;/* type hierarchy (PDDL) */

/* have to do with completeness check */
BOOLEAN same_as_prev_flag = FALSE;/* is set when graph has levelled off */
int first_full_time;/* stores time when graph has levelled off */
int previous_Scount = -1;/* previous num hashes at first full time */
int current_Scount = 0;/* current num hashes at that time */

/* the actual graph: two arrays of hashtables */
hashtable fact_table[3][MAX_PLAN+1], op_table[3][MAX_PLAN+1];
int rifo_active_part = 0;

/* option preset values */
int max_nodes = MAX_MAX_NODES;/* max number of nodes at one level */
BOOLEAN do_subset = TRUE;/* flag: use subset check in memoizing ? */
int display_info = 1;/* level of run time info printed */
int do_heuristic = 0;/* edge ordering strategy : preset none */
BOOLEAN rem_inertia = TRUE;/* remove inertia ? */

/* memoizing stuff */
int simple_hits = 0;/* just for info: */
int partial_hits = 0;
int subset_hits = 0;/* different memoize types */

long bytes_graph = 0;
long bytes_memo = 0;

/* for searching */
goal_array *goals_at;
goal_array *ops_at;
goal_array *critics_at;
SS_at_type *SS_at;
int *num_goals_at;
int *num_ops_at;
int *num_critics_at;
int *num_SS_at;

int num_ints = 0;

int num_of_actions_tried = 0;/* info */


/* variables for removing irrelevants */
operator_list save_operators; /* store loaded operators when running RIFO */
token_list save_initial_facts; 
int rifo_display_info = 1;
int mindepth = 1, maxdepth = 20;
int setlistthres = 10;
int unionstrategy = -1;
int oplevel = 1, factlevel = 1;
rifo_hashtable_t rel_fct_table, rel_op_table;
operator_list save_operators;
token_list constant_tl = NULL;  /* to store all typed objects as: name_type */
long memused = 0;
long memmaxused = 0;
long nodes_visited = 0;
rifo_hashtable_t objects_table;
settype *primary_fact_set, *secondary_fact_set; /* first and second part of relevant initial facts */

char problemName[MAX_LENGTH]; /* the problem name */
FILE * outputFile = NULL; /* the output file fd */

/* RIFO meta-strategy */
int ground_ops_count = 0; /* number of ops helps to determine the strategy */
int objects_count = 0;    /* as does the number of objects */
BOOLEAN complete_rifo_run = TRUE;

void print_rifo_options();

int main( int argc, char *argv[] )
{
  int exit_status = 0; /* indicates at end if plan was found, used for PURIFY */
  char ops_file_name[MAX_LENGTH] = "";
  char fct_file_name[MAX_LENGTH] = "";
  char path[MAX_LENGTH]  = "";/* common path for both files */
  char ops_file[MAX_LENGTH]  = "";/* resulting name for ops file */
  char fct_file[MAX_LENGTH]  = "";/* same for fct file */

  char save_name[MAX_LENGTH] = "graph";/* preset saving name */
  char part_save_name[MAX_LENGTH];
  char plan_output_file_name[MAX_LENGTH]  = "";/* save a plan in this file */
  token_list inertia;/* stores inertia literal names */

  op_list goal_predecessor, single_goal_op; /* preprocess goals */
  BOOLEAN write_graph = FALSE;/* write graph to output files ? */
  int min_time = 0, i;/* specified minimal planning time */
  BOOLEAN reached_goals;/* stores return value of build_graph */
  BOOLEAN found_plan = FALSE;/* stores return value of search_plan */
  fact_list fl_dummy;

  char option, rifo_option;/* command line interpretation */

  int build_time, plan_time, this_trial_time=0;
  int preproc_time, inst_time;/* store times */

  int method, level; /* commmand line parameters */
  struct tms rifo_start, rifo_end;
  int rifo_time;
  int rifo_on=0; /* 0 rifo not used (default), 1 ipp+rifo, 2 stop after rifo */
  BOOLEAN do_meta = TRUE;

  int strategy_count; /* used to count down possible ways to use rifo */

  /* no options entered: print usage */
  if (argc == 1) {
    printf("\nusage of ipp:\n");

    printf("\nOPTIONS   DESCRIPTIONS\n\n");
    printf("-o <str>    operator file name\n");
    printf("-f <str>    fact file name\n");
    printf("-p <str>    path for operator and fact file\n\n");
    printf("-S          don't do partial and complete subset check in memoizing\n");
    printf("-I          don't remove inertia from planning problem\n\n");
    printf("-h <num>    heuristic ordering of add edges( preset: 0 )\n");
    printf("     0    : none\n");
    printf("     1    : ( sum of pre values / num preconds )\n");
    printf("     2    : ( product of ( sum of pre values ) )\n\n");
    printf("-W          write complete graph to text files after planning\n");
    printf("-n <str>    specify name for graph output files( preset: graph )\n");
    printf("\n-i <num>  run-time information level( preset: 1 )\n");
    printf("     0    : only cpu time and num of actions info\n");
    printf("     1    : plan time info and final plan\n");
    printf("     2    : info on memoizing hits\n");
    printf("     3    : display loaded operators and facts\n");
    printf("     4    : show the instantiable ops\n");
    printf("     5    : show all the possible instantiations of those\n");
    printf("     6    : say which inertia are removed\n");
    printf("\nRun ipp with RIFO (Remove Irrellevant Facts and Operators):\n");
    printf("-rr <int>   global rifo options:\n");
    printf("     0    : only run ipp (default)\n");
    printf("     1    : use ipp with rifo\n");
    printf("     2    : stop after runnng rifo\n");
    printf("...to see all other RIFO options, just call IPP with option -rh\n" );

    printf("\nNOTE: if only an operator file <name> is specified,\n");
    printf("      default value for fact file is also <name>\n");
    printf("      similar if only fact file is specified.\n\n");
    exit( 1 );
  }

  /* read and interpret command line arguments */
  while ( --argc && ++argv ) {
    if ( *argv[0] == '-' && ( (strlen(*argv) == 2) || ( (*argv)[1] == 'r') ) ) {
      /*each option has 1 letter, except for RIFO options: -r + one letter */
      option = *++argv[0];
      switch ( option ) {/* first check the flags */
      case 'S':
        do_subset = FALSE;
        break;
      case 'M':
        do_meta = FALSE;
        break;
      case 'W':
        write_graph = TRUE;
        break;
      case 'I':
        rem_inertia = FALSE;
        break;
      case 'r':
	rifo_option = *++argv[0];
	switch( rifo_option ) { /* RIFO options */
	case 'h':
	  print_rifo_options();
	  break;
	default:
	  if ( --argc && ++argv ) { /* option specified */
	    switch( rifo_option ) {
	    case 'l':
	      sscanf( *argv,"%d",&level );
	      switch ( level ) {
	      case 3:
		factlevel = 2;
		oplevel = 2;
		break;
	      case 2:
		factlevel = 2;
		oplevel = 1;
		break;
	      case 1:
		factlevel = 1;
		oplevel = 1;
		break;
	      case 0:
		factlevel = 0;
		oplevel = 0;
		break;
	      }
	      break;
	    case 'u':
	      sscanf( *argv,"%d",&unionstrategy );
	      break;
	    case 'm':
	      sscanf( *argv,"%d",&method );
	      switch ( method ) {
	      case 1:
		unionstrategy = 0;
		break;
	      case 2:
		unionstrategy = -10000;
		break;
	      case 3:
		unionstrategy = -1;
		break;
	      case 4:
		unionstrategy = 1;
		break;
	      }
	      break;
	    case 'r':
	      sscanf( *argv,"%d",&rifo_on );
	      break;
	    case 'i':
	      sscanf( *argv,"%d",&rifo_display_info );
	      break;
	    case 'n':
	      sscanf( *argv,"%d",&mindepth );
	      break;
	    case 'x':
	      sscanf( *argv,"%d",&maxdepth );
	      break;
	    case 't':
	      sscanf( *argv,"%d",&setlistthres );
	      break;
	    }
	  } else {/* something wrong with the option */
	    printf("\nipp: wrong usage with rifo options\n\n");
	    exit( 1 );
	  }
	  break;
	} 
	break; /* end of RIFO options */
      default:
        if ( --argc && ++argv ) { /* option specified */
	  switch ( option ) { /* examine the option letter */
	  case 'o':
	    strncpy(ops_file_name, *argv, MAX_LENGTH);
	    break;
	  case 'f':
	    strncpy(fct_file_name, *argv, MAX_LENGTH);
	    break;
          case 'm':
            sscanf(*argv, "%d", &max_nodes);
            break;
          case 'i':
            sscanf(*argv, "%d", &display_info);
            break;
          case 'h':
            sscanf(*argv, "%d", &do_heuristic);
            break;
          case 'p':
	    strncpy(path, *argv, MAX_LENGTH);
            break;
          case 'n':
	    strncpy(save_name, *argv, MAX_LENGTH);
            break;
          case 'z':
	    strncpy(plan_output_file_name, *argv, MAX_LENGTH);
            break;
	  default:
	    printf( "\nipp: unknown option: %c entered\n\n", option );
	    exit( 1 );
	    break;
	  }
        } else {/* something wrong with the option */
	  printf("\nipp: unknown option\n\n");
	  exit( 1 );
        }
      }
    } else {/* option has more than one letter or no '-' prefix */
      printf("\nipp: wrong usage\n\n");
      exit( 1 );
    }
  }

  /* unknown heuristc entered */
  if (  do_heuristic > 2 ) {
    printf( "\nipp: unknown heuristic entered\n\n" );
    exit( 1 );
  }


 /* too large max_nodes as argument of -m specified (Jana 17/9) */ 
  if (  max_nodes > MAX_MAX_NODES ) {
    printf( "\nipp: -m %d exceeds MAX_MAX_NODES bound of %d\n", 
               max_nodes,  MAX_MAX_NODES );  
    exit( 1 );
  }

  /* no input name at all entered */
  if ( !ops_file_name[0] && !fct_file_name[0] ){
    printf( "\nipp: at least one inputfile name needed\n\n" );
    exit( 1 );
  }

  /* only one entered ? => copy from other */
  if ( !ops_file_name[0] ) strncpy( ops_file_name, fct_file_name, MAX_LENGTH);
  if ( !fct_file_name[0] ) strncpy( fct_file_name, ops_file_name, MAX_LENGTH);

 /* add path info, complete file names will be stored in
   * ops_file and fct_file
   */
  strcat( ops_file, path );
  strcat( fct_file, path );
  strcat( ops_file, ops_file_name );
  strcat( fct_file, fct_file_name );


  /********************************************************************
   * From now on all errors will go into an output file, if one was
   * specified.
   *******************************************************************/

  /* open the output file, if desired */
  if (*plan_output_file_name)
    {
      if ( !(outputFile = fopen(plan_output_file_name, "a+" )) ) 
	{
	  fprintf(stderr, "Cannot open file %s.", plan_output_file_name);
	  OUTPUT_FILE;
	  exit( 1 );
	}
    }

  get_fct_file_name( fct_file );

  /* print problem name first */
  if (outputFile)
    fprintf(outputFile, "\n\n%s\n", problemName);

  load_ops_file( ops_file ); /* it is important for the pddl language
				to define the domain before reading
				the problem */

  load_fct_file( fct_file );

  build_orig_constant_list();

  times( &gstart );

  preprocess_axioms();

  preprocess_pl1_facts(); /* find normal forms for pl1 expression
			     in preconditions, goals and effect conditions */

  /* preprocessing: enable to use negated facts */
  preprocess_not();  /* globals changed: negated_preds, orig_initial_facts */

  times( &gend );
  preproc_time = ( ( gend.tms_utime - gstart.tms_utime +
		     gend.tms_stime - gstart.tms_stime  ));
  total_time =+ preproc_time;

  /* convert initials to graph storage */
  initial_facts = token_list_from_fact_list( orig_initial_facts );

  /* check if there are only conjuctive or all-quantified goals, and if
   * so remove the REACHGOAL operator */
  /* ATTENTION: BIG Problem if this simple routine is used. This is really
     a big bug in IPP now... */
//   goal_predecessor = NULL;
//   if ( single_goal_op = conjuctive_goals( loaded_ops, &goal_predecessor ) )
//     {
//       /* we don't need the REACHGOAL operator, but are able to use
// 	 our own goal_facts structure (this enables us to use GAM) */
//       free_complete_token_list( goal_facts );
//       goal_facts = token_list_from_fact_list( single_goal_op->preconds );
//       if ( goal_predecessor )
// 	goal_predecessor->next = single_goal_op->next;
//       else
// 	loaded_ops = single_goal_op->next;
//       free( single_goal_op->name );
//       free_complete_effect_list( single_goal_op->effects );
//     }

  /* display info on loaded operators and fact, if wanted */
  if ( display_info > 2 ) {
    printf( "\nloaded operators are:\n" );
    print_ops( loaded_ops );
    printf( "\nloaded facts are:\n" );
    print_fct( orig_constant_list, initial_facts, goal_facts );
    printf( "\n" );
  }

  times( &gstart );
  /* remove operators that cannot be instantiated with given facts */
  remove_uninstantiable_ops( &loaded_ops, orig_constant_list );

  /* display info on not removed operators, if wanted */
  if ( display_info > 3 ) {
    printf( "\nnot removed operators are:\n" );
    print_ops( loaded_ops );
    printf( "\n" );
  }

  /* just for fun ( makes output look nicer ) */
  if ( display_info < 3 ) printf( "\n" );

  /* find out which literals are inertia */
  inertia = get_inertia( orig_initial_facts, loaded_ops );

  /* calculate all possible instantiations 
   * and store them in global list operators
   */
  instantiate( loaded_ops, orig_initial_facts, inertia, orig_constant_list );  

  /* find and remove all facts that are never deleted from the
   * global op and fact lists
   */
  if ( rem_inertia )
    handle_inertia( inertia );

  /* this one goes through all instantiated operators, looking
   * for effects with identical conditions that might occur due to
   * removal of inertia or eq - conditions
   *
   * is defined in inertia.c, which doesn't make sense but saves us from
   * yet another file of c code
   */
  merge_identical_effects(); 
  times( &gend );
  inst_time = ( ( gend.tms_utime - gstart.tms_utime +
		  gend.tms_stime - gstart.tms_stime  ));
  total_time =+ inst_time;

  /* display info on instantiated operators, if wanted */
  if ( display_info > 4 ) {
    printf( "\n Original instantiated operators are:\n\n" );
    print_operators( operators );
    printf("\n" );
  }

  printf( "\nipp: spent %.2f seconds in preprocessing", preproc_time / 100.0);
  printf( "\nipp: spent %.2f seconds instatiating ground ops\n\n", inst_time / 100.0);
  

  if ( do_meta )
    {
      /* Before entering the RIFO meta strategy loop, check which
	 strategy seems to be promissing */

      if ( (ground_ops_count > OPS_THRESH && objects_count > OBJ_THRESH))
	strategy_count = 2;
      else if ( objects_count > OBJ_THRESH )
	strategy_count = 1;
      else
	strategy_count = 0;
      if ( display_info )
	printf( "\n%d ground operators, %d objects (in ocl: %d), %d initials",
		ground_ops_count, objects_count, 
		fact_list_length( orig_constant_list ),
		token_list_length( initial_facts ) );
      
      if ( strategy_count >= 1 )
	/* store all information that might be changed by rifo
	   in order to rebuild it (using reset_original_ipp_information() )
	   if rifo strategy fails */
	save_original_ipp_information();
    }
  else
    if ( rifo_on )
      save_original_ipp_information();


  do {    /* will terminate when a plan is found or rifo_on == FALSE */

    if ( do_meta )
      {
	switch ( strategy_count ) {
	case 2: rifo_on = TRUE; oplevel = 2; factlevel = 2; 
                unionstrategy = 1; break;
	case 1: rifo_on = TRUE; oplevel = 1; factlevel = 2;
                unionstrategy = 1;break;
	case 0: rifo_on = FALSE; reset_original_ipp_information(); break;
	}
	printf( "\n==> RIFO strategy: %d (%s)\n\n", strategy_count,
		rifo_on ? "RIFO active" : "RIFO inactive" );
      }

    /* jetzt muessen n paar globals fuer den planer neu gesetzt werden.
     */
    min_time = 0;
    same_as_prev_flag = FALSE;
    previous_Scount = -1;
    current_Scount = 0;

    /* remove irrelevant facts and operators. 
       globals changed     : operators, initial_facts;
       restore old values with reset_original_ipp_information() */
    rifo_time = 0;
    if ( rifo_on ) {
      reset_original_ipp_information();
      times( &gstart );
      /* start RIFO */
      if ( !find_relevant_initial_facts( complete_rifo_run ) )
	strategy_count = 0; /* if RIFO wasn't successful, don't use it again */
      complete_rifo_run = FALSE;
      times( &gend );
      rifo_time = ( ( gend.tms_utime - gstart.tms_utime +
		      gend.tms_stime - gstart.tms_stime  ));
      if ( rifo_display_info )
	{
	  printf( "rifo: %.2f secs used to remove irrelevant facts and operators\n", 
		  rifo_time / 100.0);
	  printf( "      %.2f MBytes\n",( double )memused/( 1024.0*1024.0 ) );
	  printf( "      %ld search nodes visited\n\n",nodes_visited );
	}
      if ( rifo_on == 2 ) /* just see rifo working and stop afterwards */
	{
	  OUTPUT_FILE;
	  exit( 0 );
	}
    }
    
    /* begin timing */
    times( &gstart );
    /* build graph until non-exclusive goals are reached */
    reached_goals = build_graph( &min_time );
    /* get building time */
    times( &gend );
    build_time = ( ( gend.tms_utime - gstart.tms_utime +
		     gend.tms_stime - gstart.tms_stime  ));
    times( &gstart );
    
    if ( !reached_goals ) {
      found_plan = FALSE;
      if ( min_time < MAX_PLAN ) {
	/* graph has leveled off and goals are still not reached */
	printf("\nipp: problem unsolvable: can't reach non exclusive goals\n\n");
      } else {
	/* we didn't even have time to find the goals */
	printf( "\nipp: MAX_PLAN too small( preset value: %d )\n\n", MAX_PLAN );
      }
    } else {
      if ( min_time ) {
	/* found goals at level higher than 0; start searching for a plan */
	for ( ; min_time < MAX_PLAN; min_time++ ) {
	  if ( ( found_plan = search_plan( min_time ) ) == TRUE ) break;
	  /* couldn't find plan; check for unsolvability */
	  if ( same_as_prev_flag ) {
	    /* start after graph has leveled off */
	    if ( previous_Scount == current_Scount ) {
	      /* nothing has changed in last step -> unsolvable */
	      break;
	    } else {
	      /* still improvements going on */
	      previous_Scount = current_Scount;
	    }
	  }
	  /* we must continue search with one more layer */
	  build_graph_layer( FALSE );
	}
	/* search finished; */
	if ( found_plan ) {
	  /* either we found a plan, */
	  if ( display_info ) print_plan( min_time );
	  if (outputFile) 
	    {
	      write_plan_to_file(min_time );
	    }
	  /* print info on memoizing hits, if wanted */
	  if ( display_info ) {
	    printf("\nipp: had %7d simple memoizing hits", simple_hits);
	    if ( do_subset ) {
	      printf("\nipp  had %7d partial memoizing hits", partial_hits);
	      printf("\nipp: had %7d subset memoizing hits", subset_hits);
	    }
	    printf("\n\n");
	  }
	} else {
	  if ( min_time < MAX_PLAN ) {
	    /* or there is no plan for the problem, */
	    printf( "\nipp: problem proved unsolvable\n\n" );
	    /* print info on memoizing hits, if wanted */
	    if ( display_info ) {
	      printf("\nipp: had %7d simple memoizing hits", simple_hits);
	      if ( do_subset ) {
		printf("\nipp: had %7d partial memoizing hits", partial_hits);
		printf("\nipp: had %7d subset memoizing hits", subset_hits);
	      }
	      printf("\n\n");
	    }
	  } else {
	    /* or we didn't give the planner enough time */
	    printf("\nipp: MAX_PLAN too small( preset value: %d )\n\n",MAX_PLAN);
	  }
	}
      } else {/* corresponds to if ( min_time ) */
	printf( "\nipp: goals are contained in initial state\n\n" );
	found_plan = TRUE;
      }
    }
    
    /* calculate and print running time */
    times( &gend );
    plan_time = ( ( gend.tms_utime - gstart.tms_utime +
		    gend.tms_stime - gstart.tms_stime  ));
    
    printf( "\nipp: number of actions tried: %8d\n\n", num_of_actions_tried );
    
    printf( "\nipp: spent %.2f seconds initial building graph", build_time / 100.0);
    printf( "\nipp: spent %.2f seconds searching for plan", plan_time / 100.0);
    this_trial_time = build_time + plan_time + rifo_time;
    printf( "\n==>   %.2f seconds in this trial\n", this_trial_time / 100.0);
    printf( "    + %.2f seconds for preprocessing, instantiation & other trials\n",
	    total_time / 100.0);
    total_time = this_trial_time + total_time;
    if ( !found_plan && rifo_on && do_meta )
      printf( "\nipp:  %.2f seconds total time so far\n\n", total_time / 100.0);
    else
      printf( "ipp:  %.2f seconds total time\n\n", total_time / 100.0);    
    
    if ( strategy_count )
      strategy_count--;
    rifo_active_part++;

  } while ( !found_plan && rifo_on && do_meta );
  /* RIFO meta strategy loop ends here */


  if (outputFile)
    {
      if ( found_plan )
	fprintf(outputFile, "\n%d\n", total_time * 10);
      else
	{
	  if ( min_time < MAX_PLAN )
	    fprintf( outputFile, "IPP proved that there is " );
	  OUTPUT_FILE;	  
	}
    }
  if ( display_info ) {
    printf("\nmemory use for graph: %.1f Kbytes",
	   (float) bytes_graph/1024);
    printf("\nmemory use for memoizing: %.1f Kbytes\n\n",
	   (float) bytes_memo/1024);
  }

  /* create the graph files, if required */
  if ( write_graph ) {
    printf("\nipp: writing graphs\n\n");
    for ( i=0; i<=rifo_active_part; i++ ) {
      sprintf( part_save_name, "%s%d", save_name, i );
      if ( !SaveGraph( part_save_name, min_time, i ) )
	printf("\nipp: error writing graph\n\n");
    }
  }

  if (found_plan)
    {
      exit_status = 0;
    }
  else
    {
      exit_status = 1;
    }

  if (outputFile)
    {
      fclose(outputFile);
    }

  exit( exit_status );
}

void print_rifo_options()
{
  printf("\nRIFO (Remove Irrelevant Facts and Operators) Options for IPP:\n");
  printf("-rr <int>    global rifo options:\n");
  printf("     0     : only run ipp (default)\n");
  printf("     1     : use ipp with rifo\n");
  printf("     2     : stop after runnng rifo\n");
  printf("-ri <int>    run time information:\n"); 
  printf("     0     : none\n");
  printf("     1     : statistics (default)\n");
  printf("     2     : remaining initial facts\n");
  printf("     3     : remaining ground operators\n");
  printf("     4     : deleted initial facts, deleted ground operators\n");
  printf("     5     : complete backchaining process, debug information\n");
  printf("-rn <int>    specify min depth in backchaining (default 1)\n");
  printf("-rx <int>    to specify max depth in backchaining (default 20)\n");
  printf("-rt <int>    to specify threshold for set list length (default 10)\n");
  printf("-rm <int>    union method as in the paper: (default is 3)\n");
  printf("     1     : use all considered initial facts\n");
  printf("     2     : use all (stored) minimal sets \n");
  printf("     3     : use all cardinality-minimal sets, \n");
  printf("     4     : pick one cardinality-minimal set\n");
  printf("-rl <int>    combined selection as described in the paper:\n");
  printf("             (default is 1)\n");
  printf("     1     : select relevant objects\n");
  printf("     2     : select relevant initial facts\n");
  printf("     3     : select ground ops\n");
  printf("-rh          gives this list\n");
  
  OUTPUT_FILE;
  exit(0);
}
