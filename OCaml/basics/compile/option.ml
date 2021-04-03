(* OCAML does not have a NULL value that can be assigned to any variable of any type *)
(* Instead, the built-in type     'a option      is used, as defined as a type as below
	type 'a option =
		| None
		| Some of 'a
	;;
	None case is intended to represent a NULL value, while Some represents all non-NULL values
*)
let x = 10 and y = 20 and z = 0;;
(* let d = y / z;; *) (* By default, this will return an exception div by zero *)

let int_div x y =
	match y with
		| 0 -> None
		|_ -> Some  (x/y);;

let contents x = 
	match x with
		| None -> 0
		| Some n -> n
;;

let x = int_div 10 0 in
	print_int (contents x);
	print_newline () ;
let x = int_div 10 5 in
	print_int (contents x);
	print_newline () ;
;;
