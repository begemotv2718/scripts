#!/usr/bin/env python
from PIL import Image
import sys
import os.path

im = Image.open(sys.argv[1])
scale = float(sys.argv[2])
size = im.size
newsize = map (lambda x: int(x*scale/100.0), size)
print newsize
newimage = im.resize(newsize, Image.ANTIALIAS)
file, ext = os.path.splitext(sys.argv[1])
newimage.save(file+"-scaled"+ext)
