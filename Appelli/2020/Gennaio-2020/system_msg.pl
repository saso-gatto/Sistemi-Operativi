#!/usr/bin/perl

$tipo=0;

if ($#ARGV==2){
    $user = shift;# || die "Non è presente il valore";
    $options = shift; # || die "non è presente";
    $path = shift; # || die "manca";
}
elsif ($#ARGV==1) {
    $user = qx (whoami);
    chomp($user);
    $options = shift;
    $path = shift;
}
else {
    die "Numero di parametri non corretti. \n"
}

if ($options=~/^-t=/){ #Se l'inizio della stringa corrisponde con -t
    $options =~ s/-t=//;
    $tipo=1;
}
elsif ($options =~ /-hw/){
    $options= "memory|dma|usb|tty";
}
else{
    die "parametro options non corretto";
}



open($fh, "<", "$path") or die "Can’t open < input.txt: $!";
@fileLog = <$fh>;
close $fh;

@file;

for (@fileLog){
    #chomp;
    if (( m/(\d+\.\d+ \d+:\d+:\d+) ($user) ($options)/ ) and ($tipo==1)){
        push (@file,$_);
    }
    elsif (( m/(\d+\.\d+ \d+:\d+:\d+) ($user).+:.+($options)/) and ($tipo==0)){
        push (@file,$_);
    }
  #  print("$_ \n");
}
print ("@file \n");


print ("User: $user \n");
print ("Options: $options \n");
print ("Path: $path \n");

%dataValore;
foreach (@file){
    chomp;
    if(m/(\d+\.\d+ \d+\:\d+\:\d+)/){
        $dataValore{$1}="$_";
    }
}
#print ("Hash \n");
#while (($k,$v)= each %dataValore){
#    print "$k => $v \n";
#}


$nomefile= qx(date "+%Y-%m-%d");
print("NomeFile: $nomefile \n");
open ($fh,">","$nomefile.out") || die $!;
foreach (sort {$dataValore{$a}<=>$dataValore{$b}} keys %dataValore){
    print $fh "$dataValore{$_} \n";
}
close $fh;



# 12.23 14:29:35 francesco liblogging-stdlog: [origin software="rsyslogd" swVersion="8.24.0" x-pid="466" x-info="http://www.rsyslog.com"] rsyslogd was HUPed
# 12.23 15:38:09 francesco kernel: [4417.092128] wlp6s0: disconnect from AP dc:fb:02:e7:e0:2c for new auth to dc:fb:02:e7:e0:20