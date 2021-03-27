exception Error;;
exception Failure of string;;
exception Failure2params of string*int;;


let str_concat (s1:string) (s2:string) : string =
	if s1 = "" && s2 = "" then raise (Failure2params("Error!",2))
	else if s1 = "" then raise Error
	else if s2 = "" then raise (Failure "Error!")
	else (s1^" "^s2)
;;

let my_fun() = 
	let s = 
		try
			str_concat Sys.argv.(1) Sys.argv.(2)
		with 
			Error -> "Error!"
			| Failure "Error!" -> "Failure!"
			| Failure2params("Error!",2) -> "Both inputs are empty"
			| Invalid_argument("index out of bounds") -> "Need two strings on input"	(* existing exception *)
	in
	print_string (s^"\n")
;;

my_fun()