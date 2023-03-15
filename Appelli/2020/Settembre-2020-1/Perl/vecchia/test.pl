#!usr/bin/perl
%test;
$test{"a"}+=100;

$var="a";
$test{$var}+=10;

print("$test{$var} \n!")
