(* parent uses functions from child1 and child2 *)
(* if filename is child2.ml, the module name becomes Child2. *)
(* Compile as ocamlc -o parent child1.ml child2.ml parent.ml *)
Child1.hello ();;
Child2.today ();;