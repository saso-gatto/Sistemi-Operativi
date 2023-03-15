#!/usr/bin/perl

$formati=shift || die "Manca il formato dei file da filtrare";
$path = shift or $path='./';

die "Troppi parametri in input" if $#ARGV>=0;

$formati=~s/--formats=//;
$formati=~tr/,/|/;

print("Formati: $formati \n");
print("Path: $path \n");

@comando = qx(du -ka  "$path");
print("@comando \n");

#Filtro l'output richiesto
%sommaEstensioni;
for (@comando){
    chomp;
    if (m/(\d+).+($formati)/){ #$2 indica l'estensione, $1 il peso del file
        $sommaEstensioni{$2}+=$1;
    }
}

foreach (sort { ($sommaEstensioni{$b} <=> $sommaEstensioni{a}) || ($a cmp $b)} keys %sommaEstensioni){
        $somma += $sommaEstensioni{$_};
        print "Estensione: $_ $sommaEstensioni{$_}Kb \n";
}