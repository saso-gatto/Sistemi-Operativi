#!/usr/bin/perl

#Esercizio 1
#Creare uno script che presi 2 interi in input ne mostri la somma, la differenza, il prodotto e il quoziente
#Rimodellare lo stesso programma facendo però uso delle subroutine. 
#Creare quindi una subroutine che prende come parametri 2 variabili per ogni operazione matematica da eseguire
#Creare uno script che presi in input una sequenza di numeri positivi terminati da tappo "-1", li inserisca in un array 
#e successivamente ne calcoli la somma*/


# $param = shift @ARGV;
# print "Param: $param\n";
# if ($a eq "param1") {...}

$a = <STDIN>; 
$b = <STDIN>; 

# elimina il fine stringa se questo è presente \n --> inserendo una var in input è presente
chomp $a;
chomp $b;

@numbers;
$num = <STDIN>;
chomp $num;
while ($num != -1){ 
    push (@numbers, $num);
    $num = <STDIN>;
}

sub sommaArray {
    $sommaTot = 0;
    foreach $n (@numbers){
        $sommaTot+=$n;
    }
    print("Somma degli elementi: $sommaTot\n");
}




somma();
differenza($a,$b);
prodotto();
quoziente();
sommaArray();

print("$sol\n");

sub somma{
#    $a = shift;
#    $b = shift @_;
#    print ("A: $a\n");
    # ricevi gli argomenti totali passati
#    $n = scalar(@_);

    $somma = $a + $b;
    print ("somma $a + $b = $somma \n");
}

sub differenza{
    $c = shift;
    $d = shift;
    $differenza = $c-$d; 
    print("differenza: c - d = $differenza\n"); 
}

sub prodotto{

    $num1 = shift;
    $num2 = shift;
    $prodotto = $a*$b;
    print("Prodotto tra $a e $b = $prodotto \n");  
}

sub quoziente{
    if($b==0){
        print("Errore nella divisione\n");
    }
    else{
        $quoziente= $a/$b;
        print("Quoziente  a / b = $quoziente\n") ;
    }
}