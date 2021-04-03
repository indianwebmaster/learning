(* Date and Time *)
(* Unix module needs adding unix.cma on the ocamlc command line. Like ocamlc unix.cma -o file file.ml *)
(* same is also needed for Str module with str.cma *)
(* On the command line  ocaml, you need to use the #load "unix.cma";; directive *)
print_float (Unix.time ());;
let t = Unix.localtime (Unix.time ());;
print_int t.tm_mon;;
print_int t.tm_year;;
(* Unix.tm = { Unix.tm_sec = 48; tm_min = 20; tm_hour = 10; tm_mday = 27; tm_mon = 2;
 					tm_year = 121; tm_wday = 6; tm_yday = 85; tm_isdst = true}
*)
