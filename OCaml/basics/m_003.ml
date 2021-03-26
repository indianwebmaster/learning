print_string "\nFunctions\n";;
let max x y = if x > y then x else y ;;
max 4 5;;
max 4.5 5.5;;
max "abc" "bcd";;
max true false;;

let min x y = 
	(
		if x < y then
			x
		else
			y;
	)
;;
min 4 5;;
min 4.5 5.5;;

print_string "\nLamba Functions\n";;
fun x y -> if x > y then x else y;;

(fun x y -> if x > y then x else y) 4 5;;

let lmax = fun x y -> if x > y then x else y;;
lmax 4 5 ;;



print_string "\nhigher order functions\n";;
let myfunc f x y = f x y;;
myfunc lmax 4 5;;


let a = 100 and b = 20;;
let minmax x y = if x < y then max x y else min x y;;
minmax a b;;

let i_mult x y = x * y;;
i_mult 2 3;;
(i_mult 3) 4;;

