print_string "\nTuples\n";;

let atuple = (1,2,3,4,5);;
let btuple = (1,2,'c','d',"e","f",false);;

let max a b = if a > b then a else b;;
max 3 4;;

let max2 (a,b) = if a > b then a else b;;
max2 (4,5);;

let emp () = print_string "\n\tNo args function\n";;

emp ();;


print_string "\nExpression matching\n";;
let int_to_month i = match i with
1 -> "Jan"
| 2 -> "Feb"
| 3 -> "Mar"
| 4 -> "Apr"
| 5 -> "May"
| 6 -> "Jun"
| 7 -> "Jul"
| 8 -> "Aug"
| 9 -> "Sep"
| 10 -> "Oct"
| 11 -> "Nov"
| 12 -> "Dec"
| _ -> "UNK" ;;

int_to_month 44;;

let int_to_week = function 
1 -> "Sun"
| 2 -> "Mon"
| 3 -> "Tue"
| 4 -> "Wed"
| 5 -> "Thu"
| 6 -> "Fri"
| 7 -> "Sat"
| a -> "UNK" ;;

int_to_week 3;;


