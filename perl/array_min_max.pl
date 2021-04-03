#!/usr/bin/perl
use List::Util qw( min max );

my @num_array = ( 3, 5, 6, 7, 1, 2, 10, 4, 20, 3, 8 );
print "num_array = @num_array\n";

my $max_val = max @num_array;
my $min_val = min @num_array;
print "min = $min_val     max = $max_val\n";
