(* File IO *)
(* in_channel   out_channel --- stdin	stdout	stderr *)
(* open_out - opens a file for writing 
	open_out_bin
	open_in - opens a file for reading
	open_in_bin

	output
	output_string - writing string to output channel
	output_char, output_binary_int

	input
	input_line - read a string from input channel
	input_char, input_binary_int

	close_out
	close_in
*)
let my_print_int x =
	print_int x;
	print_newline
;;

let in_file = open_in "/var/log/syslog" in
	let line = input_line in_file in
		close_in in_file;
		print_endline line
;;

let out_file = open_out "/tmp/ocaml_out" in
	output_string out_file "test string\n";
	close_out out_file
;;