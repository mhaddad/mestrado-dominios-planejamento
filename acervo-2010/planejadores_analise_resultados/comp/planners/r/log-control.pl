/* solve_a_goal rules for logistics domain */
/* to make sense of these rules, refer to file "logistics" which
is the specification of the domain used by the planner. Tha main difference
is that in the PDDL specification, there is only one at(x,y) fluent. But
here, we have at3(x,y) refering to a package x at certain airport y,
at4(x,y) refering to a package x at a certain location y, and etc. */

holds_plan_log(incity(X,Y),_) :-
    holds_plan([inUcity1(X,Y)],[]);
    holds_plan([inUcity2(X,Y)],[]).
holds_plan_log(at(X,Y),P) :-
    holds_plan([at3(X,Y)],P);
    holds_plan([at4(X,Y)],P);
    holds_plan([at5(X,Y)],P);
    holds_plan([at6(X,Y)],P);
    holds_plan([at7(X,Y)],P);
    holds_plan([at8(X,Y)],P).
holds_plan_log(in(X,Y),P) :-
    holds_plan([in9(X,Y)],P);
    holds_plan([in10(X,Y)],P).

airport(X) :- pdomain(airport,D), member(X,D).
airplane(X) :- pdomain(airplane,D), member(X,D).
truck(X) :- pdomain(truck,D), member(X,D).


solve_a_goal(at3(Obj,Apt),A,G,_,P) :-
    holds_plan_log(at(Obj,X),P),
    X\==Apt,
    ((airport(X), airplane(Apn), 
      ((holds_plan_log(at(Apn,X),P), G=[], A=loadUairplane13(Obj,Apn,X));
       G=[at7(Apn,X)]));
     (holds_plan_log(incity(X,C),P),
      truck(T), holds_plan_log(at(T,L),P),holds_plan_log(incity(L,C),P),
      ((holds_plan_log(at(T,X),P), G=[], A=loadUtruck12(Obj,T,X));
       G=[at6(T,X)]))).
solve_a_goal(at3(Obj,Apt),A,G,_,P) :-
    holds_plan_log(in(Obj,X),P),
    ((airplane(X),
      ((holds_plan_log(at(X,Apt),P),
	G=[], A=unloadUairplane17(Obj,X,Apt));
       G = [at7(X,Apt)]));
     ((holds_plan_log(at(X,Apt),P),
	G=[], A=unloadUtruck15(Obj,X,Apt));
       (holds_plan_log(at(X,L),P),
	holds_plan_log(incity(L,C1),P),holds_plan_log(incity(Apt,C2),P),
	((C1=C2,G=[at5(X,Apt)]);
	 (airport(Apt1),holds_plan_log(incity(Apt1,C1),P),
	  G=[at3(Obj,Apt1)]))))).

solve_a_goal(at4(Obj,L),A,G,_,P) :-
    holds_plan_log(at(Obj,X),P),
    X\==L,
    holds_plan_log(incity(X,C),P),
    truck(T), holds_plan_log(at(T,L),P),holds_plan_log(incity(L,C),P),
    ((holds_plan_log(at(T,X),P), G=[], A=loadUtruck12(Obj,T,X));
       G=[at6(T,X)]).
solve_a_goal(at4(Obj,L),A,G,_,P) :-
    holds_plan_log(in(Obj,X),P),
    holds_plan_log(at(X,L1),P),
    holds_plan_log(incity(L1,C1),P),
    holds_plan_log(incity(L,C2),P),
    ((airplane(X),
      ((C1=C2,
	A=unloadUairplane17(Obj,X,L1),G=[]);
       (airport(Apt),holds_plan_log(incity(Apt,C2),P),
	G = [at7(X,Apt)])));
     (((holds_plan_log(at(X,L),P),
	G=[], A=unloadUtruck16(Obj,X,L));
	((C1=C2,G=[at5(X,L)]);
	 (airport(Apt1),holds_plan_log(incity(Apt1,C2),P),
	  G=[at3(Obj,Apt1)]))))).

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
        subtract(Loc1,Apt1,Loc2),
	findall(package(X), member(package(X),Init93), Pack),
	subtract(Init93,Pack,Init94),
	findall(X, member(package(X),Pack), Pack1),
	findall(truck(X), member(truck(X),Init94), Tru),
	subtract(Init94,Tru,Init95),
	findall(X, member(truck(X),Tru), Tru1),
	findall(airplane(X), member(airplane(X),Init95), Apn),
	subtract(Init95,Apn,Init),
	findall(X, member(airplane(X),Apn), Apn1),
	Domains = [[package, Pack1],
	           [truck, Tru1], [city, City1], [location, Loc2],
		   [airport, Apt1], [airplane, Apn1]].


