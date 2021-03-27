let my_print_int x =
	print_int x;
	print_string "\n"
;;

let myfun ~x:i ~y:j = 
 	i + j
 ;;

my_print_int (myfun ~x:4 ~y:5);;
my_print_int (myfun ~y:5 ~x:4);;

let myfun2 ~x ~y = 
 	x + y
 ;;

my_print_int (myfun2 ~x:4 ~y:5);;
my_print_int (myfun2 ~y:5 ~x:4);;

(* optional params *)
let myfun3 ?(x=0) ~y = 
	x + y
;;
my_print_int (myfun3 ~x:4 ~y:5);;
my_print_int (myfun3 ~y:5 ~x:4);;
my_print_int (myfun3 4);;
my_print_int (myfun3 ~x:5 ~y:4);;

let myfun4 ?(x=0) y = 
	x + y
;;
my_print_int (myfun4 4);;
my_print_int (myfun4 ~x:5 4);;