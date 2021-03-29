(* parent2 - opens child1 and child2, instead of calling it directly *)
(* Compile as ocamlc -I subdir -o parent3 child1.ml child2.ml subdir/child3.ml parent3.ml *)
(*
	With either ocamlc or ocamlopt, the resulting binary is self contained and can be moved/run from anywhere.

	For ocamc to see Child3, you see to set OCAMLPATH=subdir before launching ocaml
*)

open Child1;;
open Child2;;
open Child3;;

hello();;
today();;
really ();;
