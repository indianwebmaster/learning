(*
Type: int -> int -> int
Description: Returns x raised to the power p.
Assumptions: p is non-negative, and we will not test your code for integer overflow cases
*)
let rec pow x p = 
	if p = 1 then x else x * pow x (p-1);;

pow 3 1;;
pow 3 2;;
pow (-3) 3;;