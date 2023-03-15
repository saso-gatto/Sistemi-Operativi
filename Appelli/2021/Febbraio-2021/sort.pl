#!/usr/bin/perl

open($fh,"<","numeri.txt");
%numeri;
for my $riga (<$fh>){
    $numeri{$riga}+=1;
}

foreach (sort {$a <=> $b}  keys %numeri){
    print "Key: $_ ";
    print "value: $numeri{$_} \n";
}
close $fh;