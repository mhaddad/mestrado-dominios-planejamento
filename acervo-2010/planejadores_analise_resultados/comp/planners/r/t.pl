mygo :- 
 consult('aips.qlf'),
 open(ps,read, in),
 read_a_word(in,_),
 read_a_word(in,_),
 read_a_word(in,_),
 read_a_word(in,_),
 read_a_word(in,C),
  read_a_word(in,_),
 read_a_word(in,T),
 string_to_atom(T1,T),
  string_to_list(T1,T2),
  T2 = [_,_,_,X,Y|_],
  string_to_list(T3,[X,Y]),
  string_to_atom(T3,T4),
  term_to_atom(T5,T4),
  ((T5 >= 5,
    concat('kill ', C, C1),
    shell(C1));
   a=a),
  close(in).


