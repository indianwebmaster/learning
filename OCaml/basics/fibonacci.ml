(* 
Description: Returns x raised to the power p.
Assumptions: p is non-negative, and we will not test your code for integer overflow cases 
*)

let rec fibonacci x = 
(
	if x <= 1 then x else x + fibonacci (x-1);
);;

fibonacci 0;;
fibonacci 1;;
fibonacci 3;;
fibonacci 6;;