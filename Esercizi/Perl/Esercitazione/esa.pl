#!/usr/bin/perl

my $value;
if ($#ARGV>=0){
    $value=shift;
}
else{
    print "Inserisci un numero: ";
    $value=<STDIN>;
    print "Inserito \n";
}
print "Value is: $value \n";
if ($value =~ /^[0-9A-F]+$/){
    print "Il numero inserito è esadecimale! \n";
}
else{
    print "Il numero inserito non è esadecimale! \n";
}