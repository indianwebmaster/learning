(* union represents union of different types, where each part is given a unique, explicit name *)
(*
	type typename =
		| ID_1 of type_1
		| ID_2 of type_2
		...
		|ID_n of type_n

	type is optional
	ID should always starts with a capital
*)
type number = 
|Zero
|Integer of int
|Real of float
;;

let z = Zero;;
let i = Integer 6;;
let d = Real 1.4;;


let float_of_number n =
	match n with
		| Zero -> 0.0
		| Integer i -> float_of_int i
		| Real r -> r
;;

float_of_number z;;
(* Does not work. Input must be type number, not int
   float_of_number 0;;
*)
float_of_number (Integer 66);;
float_of_number i;;
float_of_number d;;
