#!usr/bin/perl

@comando = qx(ps -elf);
@pid;

for my $value (@comando){
    if ($value =~/\d \w \D+(\d+) .+(chrome)/){
        push (@pid, $1);
    }
}

$somma=0;
for my $v (@pid){
    open($fh,"<","/proc/$v/status");
    @testo = <$fh>;
    for my $riga (@testo){
        if ($riga=~/^VmRSS:.+(\d+)/){
            $somma+=$1;
        }
        close ($fh);
    }
}

print "La somma totale è $somma kb! \n";
