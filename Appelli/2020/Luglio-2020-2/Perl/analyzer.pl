#!usr/bin/perl

$path = shift || die "parametro mancante";
%ipUtente;
%tentativi;
open ($fh, "<",$path) or die "$!";
while(<$fh>){
    chomp;
    if(m/Invalid user (\w+) from (\d+\.\d+\.\d+\.\d+) port (\d+)/i){
        $ipUtente{"$2:$3"}=$1;
        $tentativi{$1}+=1;
    }
}
close $fh;

open ($fh,">","es.out") or die "$!";
foreach(sort {($tentativi{$b} <=> $tentativi{$a}) || ($a cmp $b)  }  keys %tentativi){
    print $fh "$_   $tentativi{$_}  \n";

    foreach my $k (keys %ipUtente){
        if ($_ eq $ipUtente{$k}){
            print $fh "$k \n";
  
        }
    }
    print $fh ("\n");
}
close $fh;