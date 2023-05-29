#!/usr/bin/env perl
use v5.14;
#标准规范 声明局部变量 关键字 my
use warnings;
use strict;

my $split_len=shift;
my $size = $split_len;
my $j=0;
my $i=0;
while(<>){
    chomp;
    my $id = $_ if(/>/);
    my $seq = <>;
    $j+=length($seq);
    if($j<=$size){
	open(O,">>Split-$i.fa");
	print O "$id\n$seq";
	close O;
    }else{
	$i++;$j=length($seq);
	open(O,">>Split-$i.fa");
	print O "$id\n$seq";close O;
    }
}
