#!/usr/bin/perl
$i=0;
$i=0;
$j=0;
while($ARGV[$j]){
  if($ARGV[$j]=~/.*[.]fig/){
    $i++;
    $_=$ARGV[$j];
    s/[.]fig//;
    $files[$i]=$_;
    print "$i $files[$i]\n";
  }
  $j++;
}
$maxj=$i;
for($j=1;$j<=$maxj;$j++){
    $x=-C "$files[$j].fig";
    if(-e "$files[$j].eps"){$x1=-C "$files[$j].eps";}else{$x1=$x+1;}
    if($x1>$x){
	system "fig2dev -L pstex $files[$j].fig >$files[$j].pstex",;
	print "$j opening $files[$j].fig\n";
	open(IN,"fig2dev -L pstex_t -p $files[$j].pstex $files[$j].fig |")||die "No file pstex_t ? $!";
	open(OUT,'>',$files[$j].'.tex');
	print OUT "\\documentclass{article}\n";
	print OUT "\\usepackage{graphicx,color}\n";
	print OUT "\\begin{document}\n";
	print OUT "\\thispagestyle{empty}\n";
	while(<IN>){s/\\epsfig{file=/\\includegraphics{/g; print OUT $_;}
	print OUT "\\end{document}\n";
	close OUT;
	close IN;
	system 'latex',$files[$j].'.tex'; 
	system 'dvips -E -o '.$files[$j].'.eps '.$files[$j].'.dvi';
    }
}
$i=0;
$j=0;
while($ARGV[$j]){
  if($ARGV[$j]=~/.*[.]mp/){
    $i++;
    $_=$ARGV[$j];
    s/[.]mp//;
    $files[$i]=$_;
    print "$i $files[$i]\n";
  }
  $j++;
}
$maxi=$i;
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
	print OUT "\\textwidth=\\paperwidth\n";
	print OUT "\\textheight=\\paperheight\n";
	print OUT "\\begin{document}\n";
	print OUT "\\thispagestyle{empty}\n";
	print OUT "\\includegraphics{$files[$i].1}\n";
	print OUT "\\end{document}\n";
	close OUT;
	system 'latex',"$files[$i].tex";
	system 'dvips -E -o '.$files[$i].'.eps '.$files[$i].'.dvi';
    }
}

