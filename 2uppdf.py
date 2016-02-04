#!/usr/bin/env python
from PIL import Image
import sys
import os.path


im1 = Image.open(sys.argv[1])
dpi1 = im1.info.get('dpi',(300,300))
size1 = im1.size
bbox = im1.size

im2 = None
if len(sys.argv)>2:
  im2 = Image.open(sys.argv[2])
  dpi2 = im2.info.get('dpi',(300,300))
  size2 = im2.size
  bbox = (max(im1.size[0],im2.size[0]),
          im1.size[1]+im2.size[1])


imout = Image.new('L',bbox)
imout.paste(im1,(0,0))
if im2:
  imout.paste(im2,(0, im1.size[1]))



file, ext = os.path.splitext(sys.argv[1])
imout.save(file+"-out"+".pdf")
