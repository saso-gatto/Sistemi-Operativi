#!usr/bin/perl

$parametro = shift || die "nessun parametro inserito";
$user = shift || die "nessun utente inserito";


if ($parametro!~/-c/ & $parametro!~/-m/){
    die "Parametro inserito errato";
}

@top = qx(top -n1 -b);
%usoUtente;
for my $riga (@top){
    $utente;
    $valore;
    if ($riga=~/^\d+ (\D+)(?:\d+\s+){5}\w+ (\d+,\d+) (\d+,\d+)/){
        if ($parametro=~/-c/){
            $usoUtente{$1}+={$2};
        }
        elsif ($parametro=~/-m/){
            $usoUtente{$1}+={$3};
        }
    }
}
$valoreUtente=$usoUtente{$utente};
$utenteMaggiore=0;
while (($k,$v)= each %usoUtente){
    if ($v>$valoreUtente){
        $utenteMaggiore=$k;
    }
}
if ($utenteMaggiore!=0){
    print "utente $user CPU: $valoreUtente";
    pirnt "utenet $utenteMaggiore CPI: $usoUtente{$utenteMaggiore}";
}