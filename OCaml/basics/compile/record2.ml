(* record is a labelled collection of values of arbitary types *)
(* fields are declared as label:type, where label begins with _ or lowercase letter *)

type person = { mutable first_name:string; mutable last_name:string; mutable address:string; mutable weight:float; mutable age:int; }

let main() =
	let mst = { first_name="manoj"; last_name="thakur"; address="usa"; weight=101.5; age=52; } in
		Printf.printf "First name is %s of age %d\n" mst.first_name mst.age;
		let mst2 = { first_name="manoj"; last_name="thakur"; address="usa"; weight=101.5; age=52; } in
			Printf.printf "First name is %s of age %d\n" mst2.first_name mst2.age;

			mst.first_name <- "MANOJ";
			mst.last_name <- "THAKUR";
			Printf.printf "First name is %s of age %d\n" mst.first_name mst.age;
	
			(* DOES NOT WORK ... := 
			mst2.first_name := "MANOJ";
			mst2.last_name := "THAKUR";
			Printf.printf "First name is %s of age %d\n" mst2.first_name mst2.age;
			*)
	
			Printf.printf "%B\n" (mst = mst2);		(* Deep compare - works *)
			Printf.printf "%B\n" (mst == mst2);		(* shallow compare - does not work *)
	
			let i = ref 0 in
				i := 10;
				print_int i.contents;
				print_int !i;
				print_newline ();
				(* !i <- 10; -- not valid *)
				i.contents <- 5;
				print_int i.contents;
				print_int !i;
				print_newline ();
;;
	
main ()
