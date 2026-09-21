# The Makefile looks ugly because it is automatically generated.
#
# The Makefile looks basic because it is not intended for people
# developing on the project but only for people who want to be able to
# compile and use the planner.
#
# There is no "make clean" or "make distclean" option. The Makefile
# only generates the executables for the different planner components,
# without creating intermediate files. If you want to get rid of the
# executables, just delete them. To return the planner distribution to
# a pristine state, you might also want to remove the Python bytecode
# files (*.pyc) that are generated when running the Python translator.
# However, there should be no need to ever do that, since Python keeps
# track of whether or not the bytecode files are current and
# regenerates them when needed.

COMPILE=g++ -O3 -Wall -W -Wno-sign-compare -ansi -pedantic -DRELEASE

default: all

.PHONY: default all


PREPROCESS_CC = preprocess/axiom.cc preprocess/causal_graph.cc preprocess/domain_transition_graph.cc preprocess/helper_functions.cc preprocess/max_dag.cc preprocess/operator.cc preprocess/planner.cc preprocess/scc.cc preprocess/state.cc preprocess/successor_generator.cc preprocess/variable.cc
PREPROCESS_H  = preprocess/axiom.h preprocess/causal_graph.h preprocess/domain_transition_graph.h preprocess/helper_functions.h preprocess/max_dag.h preprocess/operator.h preprocess/scc.h preprocess/state.h preprocess/successor_generator.h preprocess/variable.h
preprocess/preprocess: $(PREPROCESS_CC) $(PREPROCESS_H)
	$(COMPILE) -o preprocess/preprocess $(PREPROCESS_CC)
all: preprocess/preprocess

SEARCH_CC = search/axioms.cc search/best_first_search.cc search/blind_search_heuristic.cc search/cache.cc search/causal_graph.cc search/cg_heuristic.cc search/closed_list.cc search/domain_transition_graph.cc search/ff_heuristic.cc search/globals.cc search/goal_count_heuristic.cc search/heuristic.cc search/open_list.cc search/operator.cc search/planner.cc search/search_engine.cc search/state.cc search/successor_generator.cc
SEARCH_H  = search/axioms.h search/best_first_search.h search/blind_search_heuristic.h search/cache.h search/causal_graph.h search/cg_heuristic.h search/closed_list.h search/domain_transition_graph.h search/ff_heuristic.h search/globals.h search/goal_count_heuristic.h search/heuristic.h search/open_list.h search/operator.h search/search_engine.h search/state.h search/successor_generator.h
search/search: $(SEARCH_CC) $(SEARCH_H)
	$(COMPILE) -o search/search $(SEARCH_CC)
all: search/search
