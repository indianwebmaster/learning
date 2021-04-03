(* name conflics are less likely when modules are used *)
(* keyword module and keyword struct.
	module names must always start with a capital letter
	module Modulename =
	struct
		....
	end
*)
(* Every .ml file is converted to a module *)
(* Thus file1.ml is converted to module File1 *)
(* Modules within modules can be accessed using the dot structure *)
module Module1 =
	struct
		let name = "first"
	end
;;

module Module2 =
	struct
		let name = "last"
		let fun1 () = "Done!"
	end
;;

Printf.printf "First Last = %s %s\n" Module1.name Module2.name;;

let fn = Module1.name in
	let ln = Module2.name in
		Printf.printf "First Last = %s %s\n" fn ln
;;


		
