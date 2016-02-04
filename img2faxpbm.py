#!/usr/bin/env python
from PIL import Image
import sys
import os.path

def otsu(hist):
  def safediv(x,y):
    if y == 0:
      return 0
    else:
      return float(x)/float(y)
  totalleft = reduce(lambda x,y: x+[x[-1]+y], hist, [0,])
  total = totalleft[-1]
  totalright = map (lambda x: total -x ,totalleft)

  weighted = [ i*hist[i] for i in range(len(hist))]
  sumweightedleft = reduce(lambda x,y: x+[x[-1]+y], weighted, [0,])
  sumweighted = sumweightedleft[-1]
  sumweightedright = map(lambda x: sumweighted -x, sumweightedleft)

  Wb = map(lambda x: float(x)/float(total), totalleft)
  Wf = map(lambda x: float(x)/float(total), totalright)
  Mb = [ safediv(sumweightedleft[i],totalleft[i]) for i in range(len(totalleft))]
  Mf = [ safediv(sumweightedright[i],totalright[i]) for i in range(len(totalright))]
  sigma2 = [ Wb[i]*Wf[i]*(Mb[i]-Mf[i])**2 for i in range(len(Wb))]
  return sigma2.index(max(sigma2))


im = Image.open(sys.argv[1])
dpi = im.info.get('dpi',(300,300))
outdpi = (204.1,195.6)
scale = (outdpi[0]/float(dpi[0]),outdpi[1]/float(dpi[1]))
size = im.size
newsize = (int(size[0]*scale[0]),int(size[1]*scale[1]))
newsize = (newsize[0]-newsize[0]%8, newsize[1]-newsize[1]%8)
newimage = im.resize(newsize, Image.ANTIALIAS)
newimage = newimage.convert('L')
threshold = otsu(newimage.histogram())
newimage = newimage.point(lambda x: 0 if x<threshold else 255, '1')
file, ext = os.path.splitext(sys.argv[1])
newimage.save(file+"-fax"+".pbm")
