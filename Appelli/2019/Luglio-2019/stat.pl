#!usr/bin/perl

$directory=shift or die "$!";
$parametro="";
if ($#ARGV==0){
    $parametro=shift or die "$!";
}
elsif ($#ARGV>0){
    die "Parametri errati";
}
@stat = qx{stat $directory $parametro};
print (@stat);


