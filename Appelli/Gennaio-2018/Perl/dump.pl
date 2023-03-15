#!usr/bin/perl
$path = shift or die "$!";
$S = shift or die "$!";
$F = shift or die "$!";
if ($#ARGV>=0 or $S>=$F){
    die "Parametri errati";
}

open ($fh,"<","$path") or die "$!";
%udp;
$totaleUDP;
%other;
$totaleOth;
for my $riga (<$fh>){
    chomp($riga);
    if ($riga=~/^(\d{2})/){

        if ($1>=$S and $1<=$F){
            if ($riga=~/((?:\d+:){2}\d+\.\d+)\s+\w+\s+((?:\d+\.){1,3}\d{1,3}(?:\.\d+)*)\s+>\s+((?:\d+\.){1,3}\d{1,3}(?:\.\d+)*):\s+(\w+)/)
            {   
                if ($4 eq "UDP"){
                    $udp{$1}="$2 > $3";
                    $totaleUDP+=1;
                }
                else {
                    $other{$1}="$2 > $3";
                    $totaleOth+=1;
                }
            }
        }
    }
}
close $fh or die "$!";
open ($fh,">", "udp.log") or die "$!";
foreach  (sort  { ($a cmp $b)} keys %udp){
    print $fh "$_ --> $udp{$_} \n";
}
print $fh ("Totale: $totaleUDP \n");
close $fh or die "$!";

open ($fh,">", "other.log") or die "$!";
foreach  (sort  { ($a cmp $b)} keys %other){
    print $fh "$_ --> $other{$_} \n";
}
print $fh ("Totale: $totaleOth \n");
close $fh or die "$!";