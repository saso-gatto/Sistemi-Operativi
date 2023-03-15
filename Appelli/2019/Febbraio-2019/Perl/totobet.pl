#!usr/bin/perl

$fileScommesse = shift or die "$!";
$fileRisultati = shift or die "$!";
open ($fh,"<","./$fileScommesse") or die "File non trovato \n";
@scommesse= <$fh>;

open ($fh, "<", "./$fileRisultati");
@risultati= <$fh>;

close ($fh);
open ($fh,">","risultato.out");
$moltiplicatore=1.0;
$vittoria=1;            #SE 1 VINCE, 0 PERDE

for my $riga(@scommesse){
    chomp($riga);
    $possibileVincita=0;
    if ($riga=~/(#Schedina \d+#)/){
        print $fh ("$1 \n");
    }
    if ($riga=~/(\w+-\w+)\s+(\w)\s+(\d.\d)/){
        $partita=$1;
        $risultato=$2;
        $moltiplicatore*=$3;
        print("moltiplicatore: $moltiplicatore \n");
        for my $rigaRisultati(@risultati){
            chomp($rigaRisultati);
            if ($rigaRisultati=~/$partita\s+(\d)-(\d)/){
                if ($risultato==1 and $1>$2){
                    print $fh ("$riga --> OK ");
                }
                elsif ($risultato==1 and $2>=$1){
                    print $fh ("$riga --> NO ");
                    $vittoria=0;
                }
                if ($risultato=="X" and $1==$2){
                    print $fh ("$riga --> OK ");
                }
                elsif ($risultato=="X" and  ($2>$1 or $1>$2)){
                    print $fh ("$riga --> NO");
                    $vittoria=0;
                }
                if ($risultato==2 and $2>$1){
                    print $fh ("$riga --> OK");
                }
                elsif ($risultato==2 and $1>=$2){
                    print $fh ("$riga --> NO");
                    $vittoria=0;
                }
            }
        }
    }
    if ($riga=~/^#Importo Scommesso\s+(\d+)/){
        print $fh ("#Moltiplicatore: $moltiplicatore \n");
        $possibileVincita=$moltiplicatore*$1;
        print $fh ("#Possibile Vincita: $possibileVincita \n");
        if ($vittoria==1){
            print $fh ("#Vincita: SI \n");
        }
        elsif ($vittoria==0){
            print $fh ("#Vincita: NO \n");
        }
        $vittoria=1;            #SE 1 VINCE, 0 PERDE
        $moltiplicatore=1;
        $possibileVincita=0;
    }
    #if ($riga=~/\s+/){
        print $fh "\n";
   # }
}

$num1=1.7;
$num2=3.2;
print($num1*$num2);
close $fh;
print "Funziona! \n";