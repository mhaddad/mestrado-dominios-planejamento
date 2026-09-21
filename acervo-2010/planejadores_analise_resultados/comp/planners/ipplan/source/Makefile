####### FLAGS

CC      = gcc
CFLAGS	= -O3 -g
LIBS    = -lm

####### Files

TARGET  = ipp
HEADERS = ipp.h rifo.h
SOURCES = ipp.c scan-probname.tab.c scan-fct.tab.c scan-ops.tab.c not_preproc.c eq_preproc.c util_inst.c instantiate.c inertia.c hash.c exclusions.c util_build.c build_graph.c memoize.c util_search.c search_plan.c save_graph.c rifofbackchain.c rifosets.c rifohash.c rifoutils.c utilities.c 

OBJECTS = ipp.o scan-probname.tab.o scan-fct.tab.o scan-ops.tab.o not_preproc.o eq_preproc.o util_inst.o instantiate.o inertia.o hash.o exclusions.o util_build.o build_graph.o memoize.o util_search.o search_plan.o save_graph.o rifofbackchain.o rifosets.o rifohash.o rifoutils.o utilities.o 

####### Implicit rules
.SUFFIXES:

.SUFFIXES: .c .o

.c.o:; $(CC) -c $(CFLAGS) $<

####### Build rules

ipp: $(OBJECTS) $(HEADERS)
	$(CC) -o $(TARGET) $(OBJECTS) $(CFLAGS) $(LIBS)

purip: $(OBJECTS)
	purify $(CC) -o purip $(OBJECTS) $(CFLAGS) $(LIBS)

scan-probname.tab.o: ipp.h scan-probname.tab.c lex.probname.c
	$(CC) $(CFLAGS) -c scan-probname.tab.c -o scan-probname.tab.o

scan-fct.tab.o: ipp.h scan-fct.tab.c lex.fct.c
	$(CC) $(CFLAGS) -c scan-fct.tab.c -o scan-fct.tab.o

scan-ops.tab.o: ipp.h scan-ops.tab.c lex.ops.c
	$(CC) $(CFLAGS) -c scan-ops.tab.c -o scan-ops.tab.o

scan-probname.tab.c: scan-probname.y 
	bison -v -pprobname -bscan-probname scan-probname.y

scan-fct.tab.c: scan-fct.y 
	bison -v -pfct -bscan-fct scan-fct.y

scan-ops.tab.c: scan-ops.y 
	bison -v -pops -bscan-ops scan-ops.y

lex.probname.c: lex-probname.l
	flex -Pprobname lex-probname.l

lex.fct.c: lex-fct.l
	flex -Pfct lex-fct.l

lex.ops.c: lex-ops.l
	flex -Pops lex-ops.l

$(OBJECTS): $(HEADERS)

show:
	@echo $(SOURCES) $(HEADERS)

clean:
	rm -f *.o *.tab.c *.bak *~ *%
