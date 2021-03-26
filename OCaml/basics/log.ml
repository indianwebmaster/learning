(*
log x y
Type: int -> int -> int
Description: Returns the log of y with base x rounded-down to an integer.
Assumptions: You may assume the answer is non-negative, x >= 2, and y >= 1
*)
let rec log b x = if x < b then 0 else 1 + log b (x - b);;

log 4 4;;
log 4 16;;
log 4 15;;
log 4 64;;