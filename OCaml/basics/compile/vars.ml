let a = 1;;
print_int a;;
print_string "\n";;
let a_ = 2;;
print_int a_;;
print_string "\n";;
let _a = 3;;
print_int _a;;
print_string "\n";;

(*
let 5a = 4;
print_int 5a;
print_string "\n";;

let Ax = 4;;
print_int Ax;;
print_string "\n";;

let _ = 5;;
print_int _;;
print_string "\n";;
*)

let ival = int_of_string Sys.argv.(1);;

let multipl5 x =
	let v = x * 5 in 
	(
		let my_fun y =
			y*y in
				let f = my_fun v in
				(
					print_int f;
					print_string "\n";
				);
		print_int v;
		print_string "\n";
	);;


multipl5 ival;;