
/* following solve_a_goal rules are adapted from automatically generated
   do1() rules
*/

/* to clear a block, unstack the one on it */

solve_a_goal(clear(X), _, [clear(Y),handempty,on(Y,X)], _, P) :-
	holds_plan([on(Y,X)],P), 
        \+ holds_plan([clear(Y),handempty,on(Y,X)], P).

/* to make the hand empty, drop the one it is holding */

solve_a_goal(handempty,putUdown(X), [],_, P) :-
	holds_plan([holding(X)],P).

/* to hold a block, if it is on table, then use pickup, otherwise, use
   unstack */

solve_a_goal(holding(X), _, [clear(X), handempty,ontable(X)], _,P) :-
	holds_plan([ontable(X)],P), 
 \+ holds_plan([clear(X), handempty,ontable(X)],P).
solve_a_goal(holding(X), _, [clear(X),handempty,on(X,Y)], _,P) :- 
	holds_plan([on(X,Y)],P),
  \+ holds_plan([clear(X),handempty,on(X,Y)], P).


/* these control rules work best when goals are extended to include
   ontable(x) for those that do not need to be on any other block, and
   are pre-sorted */

goal_need_to_be_completed.

complete_goal(G,G1) :-
	findall(ontable(X), (member(on(Y,X),G), \+ member(on(X,Z),G)), G2),
	union(G,G2,G3),
	blocks_goal_ordering(G3,G1).

:- dynamic holds/1.

blocks_goal_ordering(G1,G2) :-
	retractall(holds(_)),
	blocks_goal_ordering_1(G1),
	findall(X,holds(X),G3),
	subtract(G1,G3,G4),
	append(G3,G4,G2).
blocks_goal_ordering_1(G) :-
	member(ontable(X),G),
	assertz(holds(ontable(X))),
	built_tower(X,G),
	fail.
blocks_goal_ordering_1(_).



built_tower(X,G) :-
	member(on(Y,X),G),
        \+ holds(on(Y,X)),
	assertz(holds(on(Y,X))),
        !,
	built_tower(Y,G).
built_tower(_,_).
