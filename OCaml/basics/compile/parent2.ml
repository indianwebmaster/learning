(* parent2 - opens child1 and child2, instead of calling it directly *)
(* Compile as ocamlc -o parent2 child1.ml child2.ml parent2.ml *)

open Child1;;
open Child2;;
hello();;
today();;