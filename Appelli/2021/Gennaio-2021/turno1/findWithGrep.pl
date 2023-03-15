#!/usr/bin/perl

if ($#ARGV==2){
    $path=shift or die "$!";
    $intd = shift or die "$!";
    $stringa = shift or die "$!";
}
else{
    die "Parametri errati";
}

@list = qx {ls -l -R $path};
print ("@list");
$sommaTotale=0;
%files;
for my $riga (@list){
    chomp ($riga);

    if ($riga=~/^-(?:-|r|w|x){9}\s+\d+\s+(?:\w+|\d+)\s+(?:\w+|\d+)\s+(\d+).+:\d{2}\s+(.+\..+)/){
        if ($2=~/$stringa/ and $intd>$1){
            $sommaTotale+=$1;
            $files{$2}=$1;
        }
    }
}
open ($fh,">","results.out") or die ("Impossibile creare il file");

foreach (sort { ($files{$b} <=> $files{$a}) || ($a cmp $b)  }  keys %files){
    print $fh ("$_   $files{$_} \n");
}
print $fh ("Spazio totale occupato: $sommaTotale");
close $fh;