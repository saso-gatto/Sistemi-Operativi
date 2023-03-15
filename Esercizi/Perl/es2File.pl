#!/usr/bin/perl

#Apro in lettura il file password.txt presente nella cartella corrente e salvo il suo contenuto nell'array.
#Scrivo il path da input e lo prendo col comando shift
$path = shift || die "Parametro mancante";

open($fh,"<",$path);
@array =<$fh>;

for (@array){
    chomp;
    print "$_ \n";
}
close $fh;

open($fh,">","./nuovoFile.txt") || die "Errore";
for my $value (@array){
    chomp ($value);
    print $fh "$value";         #Print $fh + testo = mi scrive il valore sul file in output
}
close $fh;
