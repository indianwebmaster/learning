let c2 = ref 0;;
let memo = Hashtbl.create 1;;
let rec memo_fib n = 
  incr c2;
  match n with
    |0 -> 0
    |1 -> 1
    |_ ->
      if Hashtbl.mem memo n then
        Hashtbl.find memo n
      else
      begin
        Hashtbl.add memo n (memo_fib(n-1) + memo_fib(n-2));
	Hashtbl.find memo n
      end
;;
