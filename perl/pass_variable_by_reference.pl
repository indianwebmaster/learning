#!/usr/bin/perl

print "==============================================\n";
sub test_scalar {
	my $var_ref = $_[0];
	# Use the ${$var_ref} syntax to get to the scalar variable.
	# It is longer, but more clear that it is a reference, as
	# any change you make here, will also be affected outside the function
	print "Inside function test_scalar, var = ${$var_ref}\n";
	${$var_ref} .= " - changed in test_scalar()";	
}

my $var = "TEST";
print "Before calling function test_scalar, var = $var\n";
test_scalar (\$var);
print "After calling function test_scalar, var = $var\n";

print "==============================================\n";
sub test_list {
	my $var_ref = $_[0];
	my @this_makes_a_copy = @{$var_ref};	# Dont do this, if you want to change the list in this sub
	print "Inside function test_list, var = @{$var_ref}\n";
	push @{$var_ref}, "changed in test_list()";	
}

my @list_var = ("one","two");
print "Before calling function test_list, list_var = @list_var\n";
test_list (\@list_var);
print "After calling function test_list, list_var = @list_var\n";


print "==============================================\n";
sub print_hash {
	my %hash = %{$_[0]};
	foreach my $key (keys %hash) {
		print ("$key => $hash{$key}\n");
	}
}
sub test_hash {
	my $var_ref = $_[0];
	my %this_makes_a_copy = %{$var_ref};	# Dont do this, if you want to change the hash in this sub
	print "Inside function test_hash, var\n";
	print_hash($var_ref);
	${$var_ref}{"test_hash"} = "CHANGED IN test_hash()";
}

my %hash_var = (
	"one" => "NUMBER ONE",
	"two" => "NUMBER TWO"
	);
print "Before calling function test_hash, hash_var =\n";
print_hash (\%hash_var);
test_hash (\%hash_var);
print "After calling function test_hash, hash_var =\n";
print_hash (\%hash_var);
print "==============================================\n";
