#!/usr/bin/perl

# Esercizio 2
# Creare uno script che modelli il funzionamento di una rubrica telefonica
# Ad ogni persona, identificata tramite nome e cognome, è attribuito un unico numero di telefonica
# Stampare in output per ogni persona il proprio numero di telefono e la lista univoca delle persone in rubrica

%hash_rubrica=("Salvatore-Gatto"=>"1234",
               "Davide-Ragona"=>"2345",
               "Caterina-Gerace"=>"3456", 
               "Debora-Ippolito"=>"4567",
               "Giorgio-Guagliardi"=>"5678");

@chiave = keys %hash_rubrica;
@values = values %hash_rubrica;

foreach $k (@chiave){
    print("chiave: $k --> valore: $hash_rubrica{$k} \n");
}

for (@chiave){
    print "Chiaveeeeee:  $_ --> valore: $hash_rubrica{$_} \n";
}