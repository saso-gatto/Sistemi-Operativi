#!/usr/bin/perl

my $param1 = shift || die "miss value";
my $param2 = shift || die "miss value2";
print ("Parametri in input: $param1 \n");
print ("Parametri in input: $param2 \n");

my @finale;

open($fh,"<","$param1");
push @finale,(<$fh>);

open ($fh,"<","$param2");
push @finale,(<$fh>);

open ($fh,">","mergeFile.txt");
print $fh (@finale);

close $fh;