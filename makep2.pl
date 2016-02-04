#!/usr/bin/perl
open(IN,'ls *.fig|');
$i=0;
while(<IN>){
    $i++;
    s/[.]fig//;
    chop;
    $files[$i]=$_;
    print "$i $files[$i]\n";
}
$maxi=$i;
close(IN);
for($i=1;$i<=$maxi;$i++){
    $x=-C "$files[$i].fig";
    if(-e "$files[$i].eps"){$x1=-C "$files[$i].eps";}else{$x1=$x+1;}
    if($x1>$x){
	system "fig2dev -L pstex $files[$i].fig >$files[$i].pstex",;
	print "$i opening $files[$i].fig\n";
	open(IN,"fig2dev -L pstex_t -p $files[$i].pstex $files[$i].fig |")||die "No file pstex_t ? $!";
	open(OUT,'>',$files[$i].'.tex');
	print OUT "\\documentclass{article}\n";
	print OUT "\\usepackage{graphicx,color}\n";
	print OUT "\\begin{document}\n";
	print OUT "\\thispagestyle{empty}\n";
	while(<IN>){print OUT $_;}
	print OUT "\\end{document}\n";
	close OUT;
	close IN;
	system 'latex',$files[$i].'.tex'; 
	system 'dvips -E -o '.$files[$i].'.eps '.$files[$i].'.dvi';
    } 
}
open(IN,'ls *.mp|');
$i=0;
while(<IN>){
    $i++;
    s/[.]mp//;
    chop;
    $files[$i]=$_;
    print "$i $files[$i]\n";
}
$maxi=$i;
close(IN);
for($i=1;($i<=$maxi)&&($i>0);$i++){
    $xmp=-C "$files[$i].mp";
    if(-e "$files[$i].eps"){$xeps=-C "$files[$i].eps";}else{$xeps=$xmp;}
    $xdat=$xeps;
    foreach(`ls $files[$i]*.dat`){
	chop;
	$tmp=-C $_;
	if($tmp<$xdat){$xdat=$tmp;}
    }
    if(($xeps>$xdat)||($xeps>=$xmp)){
	print "Processing mpost file...\n";
	system 'mpost',"$files[$i].mp";
	open(OUT,'>',$files[$i].'.tex');
	print OUT "\\documentclass[12pt]{article}\n";
	print OUT "\\usepackage{graphicx,color}\n";
	print OUT "\\begin{document}\n";
	print OUT "\\thispagestyle{empty}\n";
	print OUT "\\includegraphics{$files[$i].1}\n";
	print OUT "\\end{document}\n";
	close OUT;
	system 'latex',"$files[$i].tex";
	system 'dvips -E -o '.$files[$i].'.eps '.$files[$i].'.dvi';
    }
}

