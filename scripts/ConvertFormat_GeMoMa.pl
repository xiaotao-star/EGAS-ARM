#!/usr/bin/perl
use strict;
use warnings;

my $in=shift or die "in\n";
my $fix=shift;
my %gff;
open (F,"$in");
while (<F>){
    chomp;
    my @a=split(/\s+/,$_);
    next if /^#/;
    ($a[3],$a[4])=sort{$a<=>$b} ($a[3],$a[4]);
    if ($a[2] eq "CDS"){
	$a[8]=~/Parent=([^\;]+)/ or die "$_\n";
	my $id=$1;
	$id=~s/\:/_/g;
	$gff{$a[0]}{$id}{gff}{$a[3]}{end}=$a[4];
	$gff{$a[0]}{$id}{gff}{$a[3]}{coord}=$a[7];
	$gff{$a[0]}{$id}{pos}{$a[3]}++;
	$gff{$a[0]}{$id}{pos}{$a[4]}++;
	$gff{$a[0]}{$id}{strand}=$a[6];
    }
}
close F;
open (O1,">$in.train");
open (O2,">${in}_pro.gff");
for my $k1 (sort keys %gff){
    #print O2 "\n";
    for my $k2 (sort keys %{$gff{$k1}}){
	print O2 "\n";
	my @pos=sort{$a<=>$b} keys %{$gff{$k1}{$k2}{pos}};
	my $strand=$gff{$k1}{$k2}{strand};
	print O1 "$k1\tGeMoMa\tgene\t$pos[0]\t$pos[-1]\t.\t$strand\t.\tID=$k2\n";
	print O1 "$k1\tGeMoMa\tmRNA\t$pos[0]\t$pos[-1]\t.\t$strand\t.\tID=$k2.t1;Parent=$k2\n";
	my @k3=sort{$a<=>$b} keys %{$gff{$k1}{$k2}{gff}};
	@k3=sort{$b<=>$a} @k3 if ($strand eq "-");
	for (my $i=0;$i<@k3;$i++){
	    my $j=$i+1;
	    my ($cdss,$cdse,$coord)=($k3[$i],$gff{$k1}{$k2}{gff}{$k3[$i]}{end},$gff{$k1}{$k2}{gff}{$k3[$i]}{coord});
	    print O1 "$k1\tGeMoMa\texon\t$cdss\t$cdse\t.\t$strand\t.\tID=$k2.t1.exon$j;Parent=$k2.t1\n";
	    print O1 "$k1\tGeMoMa\tCDS\t$cdss\t$cdse\t.\t$strand\t$coord\tID=cds.$k2.t1;Parent=$k2.t1\n";
	    $k2=~/^(\S+)\_R\d+/ or die "$k2\n";
	    print O2 "$k1\t$fix\tnucleotide_to_protein_match\t$cdss\t$cdse\t.\t$strand\t.\tID=match.$k2;Target=$1\n";
	}
    }
}
close O1;
close O2;
