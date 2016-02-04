#!/usr/bin/env python
from PIL import Image
import sys
import os.path
from os import system,remove,rename


im = Image.open(sys.argv[1])
newimage = im.copy()
newimage = newimage.convert('L')
newimage = newimage.point(lambda x: 0 if x<1 else 255, '1')
file, ext = os.path.splitext(sys.argv[1])
newimage.save(file+".pbm")
system("cjb2 %s.pbm %s-bw.djvu" % (file,file))
remove(file+".pbm")
im=im.point(lambda x: x if x>0 else 255,'L')
hist=im.histogram()
hist=hist[0:254]
if(all([v == 0 for v in hist])):
    rename(file+"-bw.djvu",file+".djvu")
else:
    im.save(file+'.pgm')
    system("c44 -slice 74+13+10 %s.pgm %s-gray.djvu" %(file,file))
    remove(file+".pgm")
    system("djvuextract %s-gray.djvu BG44=%s.iww44" %(file,file))
    remove(file+"-gray.djvu")
    size=newimage.size
    neww=int((size[0]+11)/12)
    newh=int((size[1]+11)/12)
    black = Image.new('L',(neww,newh))
    black.save("bg.pgm")
    system("c44 -slice 140 bg.pgm bg.djvu")
    system("djvuextract bg.djvu BG44=bg.iww44")
    system("djvumake %s.djvu FG44=bg.iww44 BG44=%s.iww44 Sjbz=%s-bw.djvu" %(file,file,file))
    remove(file+"-bw.djvu")
    remove(file+".iww44")


