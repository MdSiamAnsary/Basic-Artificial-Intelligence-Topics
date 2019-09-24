parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').

grandparent(X,Z):-
	parent(X,Y),parent(Y,Z).





%%	%%%%%%%%%%%
%
%Is there anybody who is a grandparent of somebody.  grandparent(_, _).
%Does Sohel have a grandparent?                      grandparent(_,'Sohel').
%Who is Sohel's grandparent?                         grandparent(X,'Sohel').
%Is Hasib a grandparent of Rebeka?		     grandparent ('Hasib', 'Rebeka').
%
%
%
%
%%	%%%%%%%%%%%%


