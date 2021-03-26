let c1 = ref 0;;
  let rec fib3 x = 
  incr c1;
  match x with
    0 -> 0
    | 1 -> 1
    |_ -> fib3(x-1) + fib3(x-2)
;;

fib3 10;;
!c1;;
