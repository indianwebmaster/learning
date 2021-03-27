let rec fib n =
  if n > 2 then
    fib(n-1) + fib(n-2)
  else if n == 0 then
    0
  else
    1
;;

let result = fib 5 in
	print_int result;;
print_string "\n";;

open String;;

let s = sub "TEST_STRING" 2 4 in
  let q = s^"\n" in
    print_string q;;


let s = Sys.argv.(0) in 
	print_string (s^"\n");;


let istr = Sys.argv.(1) in
	let i = int_of_string istr in
		let f = fib i in
			print_int f;;
print_string "\n";;