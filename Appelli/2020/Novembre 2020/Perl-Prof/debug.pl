#!/usr/bin/perl

$dev = shift or die "Device name is required \n";
die "Too many parameters in input \n" if $#ARGV>=0;

$ip = ifconfig ($dev);
print "Il tuo indirizzo ip locale è $ip \n";

%arp_map= arp();
#foreach (keys %arp_map){
#    print "key: $_ --> value: $arp_map{$_}";
#}
netstat();

for (sort{$arp_map{$b} <=> $arp{a}} keys %arp_map){
    print "IP: $_ \t #cpmmessopmo_ $arp_map{$_}\n";
}


sub ifconfig{
    $device = shift;
    $ifconfig = qx{ifconfig $device};
    #cercare in $ifconfig la stringa inet IP
    $ifconfig =~ m/inet\s((?:\d{1,3}\.){3}\d{1,3})/;
    return $1;
}

sub arp {
    %arp_map;
    @arp = qx {arp n};
    for (@arp){
        m/inet\s((?:\d{1,3}\.){3}\d{1,3})/; #è equivalente a $_ =~ m/inet\s((?:\d{1,3}\.){3}\d{1,3})/;
        chomp $1;
        next if ($l eq "");
        $arp_map{$1}=0;
    }
    return %arp_map;
}

sub netstat{
    @netstat = qx{netstat - tupan};

    for (@netstat){ #Abbiamo l'output di netstat, l'obiettivo è quello di ricavare da netstat l'iplocale e l'ipremoto
        chomp;
        @splittedline = split (" ", $_);
        @ip_locale= split(":", $splittedline[3]);
        @ip_remoto= split(":", $splittedline[4]);
        print "$splittedline[0] \n";

        next if ($ip_locale[0] eq " ");

    }
}

#espressione regolare per matchare un indirizzo ip:
# inet\s+(\d{1,3}\.\d{1,3}.\d{1,3}\.\d{1,3})
# inet\s((?:\d{1,3}\.){3}\d{1,3})/;