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

let read_whole_file fpath = 
	try
		let in_file = open_in fpath in
			try
				while true do    (* Just an infinite loop *)
					let line = input_line in_file in
						print_endline line
				done
			with End_of_file ->
				close_in in_file
	with Sys_error msg ->
		print_endline (fpath^": File not found("^msg^")")
;;

read_whole_file "/var/log/syslog";;
read_whole_file "abcd";;