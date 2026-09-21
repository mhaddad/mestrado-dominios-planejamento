/* another way to specify control information for the logistics domain:
   domain dependent information about unachievable goals. it seems to work
   almost as well as control-log.pl */


/* unachievable goals */

/* a truck cannot go to another city */

unachievable(G) :- 
	(member(at5(T,A),G);member(at6(T,A),G)),
	initial_state(S),
	(holds([inUcity1(A,C)],S);holds([inUcity2(A,C)],S)),
	(holds([at5(T,L)],S);holds([at6(T,L)],S)),
	(holds([inUcity1(L,C1)],S);holds([inUcity2(L,C1)],S)),
	C\==C1.

/* an airplane cannot go to a location */

unachievable(G) :-
	member(at8(_,_),G).


/* process an untyped logistics problem as given in Track2 of AIPS-00 */
/* uncomment the following line if the given problem is untyped*/

%problem_need_to_be_processed.

preprocess_problem(_,Init9,Goal,Domains,Init,Goal) :-
	findall(airport(X), member(airport(X),Init9), Apt),
	subtract(Init9,Apt,Init91),
	findall(X, member(airport(X),Apt),Apt1),
	findall(city(X), member(city(X),Init91), City),
	subtract(Init91,City,Init92),
	findall(X, member(city(X),City),City1),
	findall(location(X), member(location(X),Init92), Loc),
	subtract(Init92,Loc,Init93),
	findall(X, member(location(X),Loc), Loc1),
	findall(package(X), member(package(X),Init93), Pack),
	subtract(Init93,Pack,Init94),
	findall(X, member(package(X),Pack), Pack1),
	findall(truck(X), member(truck(X),Init94), Tru),
	subtract(Init94,Tru,Init95),
	findall(X, member(truck(X),Tru), Tru1),
	findall(airplane(X), member(airplane(X),Init95), Apn),
	subtract(Init95,Apn,Init),
	findall(X, member(airplane(X),Apn), Apn1),
        subtract(Loc1,Apt1,Loc2),
	Domains = [[package, Pack1],
	           [truck, Tru1], [city, City1], [location, Loc2],
		   [airport, Apt1], [airplane, Apn1]].


