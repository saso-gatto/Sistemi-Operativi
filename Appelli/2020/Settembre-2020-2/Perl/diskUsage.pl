#!usr/bin/perl
$parametri = shift or die "Parametro non inserito";
if ($#ARGV==0){
    $path=shift or die "$!";
}
elsif ($#ARGV==-1){
    $path=".";
}
@list = qx {du -ka $path};

$parametri=~ s/--format=//g;
$parametri=~ s/,/|/;
print ("$parametri \n");
%files;
for my $riga (@list){
    chomp ($riga);
    if ($riga=~/(\d+)\s+.+\.($parametri)/){
        $files{$2}+=$1;
    }
}
$sommaTot=0;
open ($fh,">","du.out") or die "$!";
foreach (sort {($files{$b} <=> $files{$a}) || ($a cmp $b)} keys %files){
    print ("Estensione: $_     $files{$_}Kb \n");
    $sommaTot+=$files{$_};
}
print $fh ("Totale occupazione disco della cartella \n");
print $fh ("$path:   $sommaTot");
close $fh;
