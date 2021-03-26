let rec fun1 x = 
  match x with
    0 -> "Zero"
    |_ ->fun2 x
and
  fun2 y = 
    match y with
    1 -> "One"
    |_ -> fun1(y-1)
;;

fun1 5;;
fun1 0;;
fun1 6;;
