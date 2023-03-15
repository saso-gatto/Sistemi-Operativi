#!usr/bin/perl

$parametro = shift or die "$!";
$utente = shift or die "$!";

if ($#ARGV>=0){
    die "parametri errati";
}

@list = qx(top -n1 -b);

%hash;
for my $riga (@list){
    chomp($riga);
    if ($riga=~/\d+\s+(\w+).+(\d+\.\d+)\s+(\d+\.\d+)/){
        $user=$1;
        $cpu=$2;
        $mem=$3;

        if ($parametro=~/-c/){
            $hash{$user}+=$cpu;
        }
        if ($parametro=~/-m/){
            $hash{$user}+=$mem;
        }
    }
}
$valoreUtente=$hash{$utente};
$valoreMax=0;
$utenteMax;

foreach $k (keys %hash){   
    if ($hash{$k}>$valoreUtente){
        $valoreMax=$hash{$k};
        $utenteMax=$k;
    }
}

open ($fh,">","stat.log") or die "Impossibile creare il file";
if ($parametro=~/-c/){
    print $fh ("utente $utente CPU: $hash{$utente} \n");
    if ($valoreMax!=0){
            print $fh ("Max uso CPU: $utenteMax  $valoreMax \n");
    }
}
elsif ($parametro=~/-m/){
    print $fh ("utente $utente MEM: $hash{$utente} \n");
    if ($valoreMax!=0){
        print $fh ("Max uso MEM: $utenteMax  $valoreMax \n");
    }
}
close $fh;