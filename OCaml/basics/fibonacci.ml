(* 
Description: Fn = Fn-1 + Fn-2. F0 = 1, F1=1
*)

let rec fibonacci x = 
(
	if x == 0 then
	  0
	else if x <= 2 then 
	  1 
	else 
	  fibonacci(x-2) + fibonacci (x-1);
);;

fibonacci 0;;
fibonacci 1;;
fibonacci 2;;
fibonacci 3;;
fibonacci 4;;
fibonacci 5;;
fibonacci 6;;
