(* ***
print_string "\nArguments\n";;

let i = 10;;
let x = 12.2;;
let s = "a string";;
let c = 'm';;

let a = 10 and b = 20 and c = 'e';;
let a = true and b = false;;


print_string "\nConditional Statements\n";;
let a = 5 and b = 10;;
if a < b then print_string ("smaller\n") else print_string ("larger\n");;

if a < b then
(
	let x = 10 in x + 2
) else
begin
	let x = -10 in x * 2
end ;;

let i = 5 and j = 10;;
if i > 5 || j > 5 then
	print_string "OR True\n"
else
	print_string "OR False\n"
;;

let x = 14 and y = 14;;
if (x+y) > 20 then
	if x = y then
		10
	else
		-10
else
	if x = y then
		20
	else
		-20
;;


print_string "\nShallow vs Deep string compare\n";;
let s1 = "a string" and s2 = "a string";;
if s1 = s2 then 
	print_string "= compare success. Deep compare, check contents pointed by pointer\n"
else 
	print_string "= compare failed. Shallow compare, check if pointers are identical\n"
	;;

if s1 == s2 then 
	print_string "== compare success. Deep compare, check contents pointed by pointer\n" 
else 
	print_string "== compare failed. Shallow compare, check if pointers are identical\n"
	;;

*** *)
