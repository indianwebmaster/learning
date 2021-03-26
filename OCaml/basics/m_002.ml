print_string "\nmutable variable (references/pointers)\n";;
let x = ref 10 ;;
x;;
!x;;

let y = ref 10;;
if x = y then print_string "= success. deep compare of contents\n" else print_string "= failure. shallow compare of pointers\n" ;;
if x == y then print_string "== success. deep compare of contents\n" else print_string "== failure. shallow compare of pointers\n" ;;
if !x == !y then print_string "== success. compare by value\n" else print_string "== failure. not compare by value\n" ;;


print_string "\nfor/while loops\n";;
for x = 1 to 10 do
	print_int x;
	print_newline ();
done;;

let x = ref 10 ;;
while !x > 0 do
	print_string "Value of x = ";
	print_int !x;
	print_string "\n";
	x := !x - 1;
done ;;