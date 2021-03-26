let rec fib n =
  if n > 2 then
    fib(n-1) + fib(n-2)
  else if n == 0 then
    0
  else
    1
;;

#trace fib;;
fib 0;;
fib 1;;
fib 2;;
fib 3;;
fib 4;;
#untrace fib;;
fib 5;;
fib 6;;
