let rec fib2 n =
match n with
  0 -> 0
  |1 -> 1
  |_ -> fib2(n-1) + fib2(n-2)
;;

fib2 0;;
fib2 1;;
fib2 2;;
fib2 3;;
fib2 4;;
fib2 5;;
fib2 6;;
