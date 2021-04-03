#!/usr/bin/perl

my %num_hash = (
	3 => "three",
	2 => "two",
	1 => 'one',
	10 => 'ten',
	20 => 'twenty',
	5 => 'five'
);
for my $hash_key (keys %num_hash) {
	print "hash_key($hash_key): value($num_hash{$hash_key})\n";
}
