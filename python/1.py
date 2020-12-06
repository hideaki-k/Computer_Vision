from PIL import Image
import os
import imtools
from pylab import *
import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

im = array(Image.open('DSC02687.ARW.jpg').convert('L'))

ax3.hist(im.flatten(),128)

ax1.imshow(Image.fromarray(im),cmap="gray")

#im2,cdf = imtools.histeq(im)
im2 = imtools.compute_average(im)
ax4.hist(im2.flatten(),128)
ax2.imshow(Image.fromarray(im2),cmap="gray")
plt.show()

#




"""
im = array(Image.open('test.jpg').convert('L'))
print(im.shape,im.dtype)
im2 = 255-im
pil_im = Image.fromarray(im2)
pil_im.show()
im3 = (100.0/255) * im + 100 #100~200の値に収める
im4 = 255.0 * (im/255.0)**2 # 2乗する
print(im4)
pil_im = Image.fromarray(uint8(im4))
pil_im.show()
"""
"""
im = array(Image.open('test.jpg').convert('L'))
figure()
gray()
contour(im, origin = 'image')
axis('equal')
axis('off')
figure()
hist(im.flatten(),128)
show()
"""
"""
filelist = ['foo.jpg','bar.bmp','zot.png']

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + '.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('cannot convert',infile)
"""
"""
filelist = imtools.get_imlist('.')
print(filelist)
pil_im = Image.open('test.jpg').convert('L')
#pil_im.thumbnail((128,128))
box = [100,100,400,500]
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region,box)
pil_im.show()
"""
