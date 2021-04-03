#!/usr/bin/perl

my @num_array = ( 3, 2, 1, 10, 20, 5, 6, 9 );
print "num_array = @num_array\n";

my @alpha_sort_array = sort @num_array;
print "alpha_sort_array = @alpha_sort_array\n";

my @numeric_sort_array = sort {$a<=>$b} @num_array;
print "numeric_sort_array = @numeric_sort_array\n";


my %num_hash = (
	3 => "three",
	2 => "two",
	1 => 'one',
	10 => 'ten',
	20 => 'twenty',
	5 => 'five'
);
my @hash_keys = keys %num_hash;
print "hash_keys = @hash_keys\n";

my @alpha_sort_hash_keys = sort keys %num_hash;
print "alpha_sort_hash_keys = @alpha_sort_hash_keys\n";

my @numeric_sort_hash_keys = sort {$a<=>$b} keys %num_hash;
print "numeric_sort_hash_keys = @numeric_sort_hash_keys\n";
