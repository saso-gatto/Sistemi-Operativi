#!/usr/bin/perl

#Esercizio 1
#Creare uno script che presi 2 interi in input ne mostri la somma, la differenza, il prodotto e il quoziente
#Rimodellare lo stesso programma facendo però uso delle subroutine. 
#Creare quindi una subroutine che prende come parametri 2 variabili per ogni operazione matematica da eseguire
#Creare uno script che presi in input una sequenza di numeri positivi terminati da tappo "-1", li inserisca in un array 
#e successivamente ne calcoli la somma*/
$a = <STDIN>; 
$b = <STDIN>; 
$somma=$a+$b;
$sottrazione= $a-$b;
$prodotto= $a*$b;

print("Somma  a + b = $somma\n");
print("Sottrazione  a - b = $sottrazione\n");
print("Prodotto  a * b = $prodotto\n");

if($b==0){
    print("Errore nella divisione\n");
}
else{
    $quoziente= $a/$b;
    print("Quoziente  a / b = $quoziente\n") ;
}