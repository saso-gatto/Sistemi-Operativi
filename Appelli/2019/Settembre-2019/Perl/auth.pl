#!usr/bin/perl

if ($#ARGV==1){
    $ip=shift or die "$!";
    $nomeFile= shift or die "$!";
    $caso=0;
}
elsif ($#ARGV==2){
    $user=shift or die "$!";
    $username=shift or die "$!";
    $nomeFile= shift or die "$!";
    $caso=1;
}
else{
    print("Parametri non validi \n");
}
open ($fh,"<","$nomeFile");
@file=<$fh>;
close $fh;


%tentativi;
@date;
open ($fh,">","log.out");
for my $riga (@file){
    if ($riga=~/Failed password for invalid user/){
        if ($riga=~/.+from\s+((?:\d{1,3}\.){3}\d{1,3})/ and $caso==0){
            $tentativi{$1}+=1;
        }
        if ($caso==1 and $riga=~/(\w+\s+\d{1,2}\s(?:\d{2}:){2}\d{2}).+user\s($username)/){
            $tentativi{$username}+=1;
            push @date, $1;
        }
    }
}
if ($caso==0){
    foreach (sort {($tentativi{b} <=> $tentativi{a})} keys %tentativi){
        print $fh ("$_ -- $tentativi{$_} \n");
        print("sono qui");
    }
}
elsif ($caso==1){
    print $fh ("$username -- $tentativi{$username} \n");
    print $fh (@date);
}

close $fh;