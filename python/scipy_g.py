from PIL import Image
import os
import imtools
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
# scipy.ndimageのimport
from scipy.ndimage import filters

im = np.array(Image.open('data/empire.jpg').convert('L'))
# ガウシアンフィルタ
"""
im2 = filters.gaussian_filter(im,5)
plt.figure(figsize=(8,8))
plt.gray()
plt.subplot(1,2,1)
plt.imshow(im)
plt.axis('off')
plt.title('original')
plt.subplot(1,2,2)
plt.imshow(im2)
plt.axis('off')
plt.title('gaussian')
plt.show()
"""
im = np.array(Image.open('data/empire.jpg').convert('L'))

# Sobel微分係数フィルタ
imx = np.zeros(im.shape)
filters.sobel(im, 1, imx)

imy = np.zeros(im.shape)
filters.sobel(im, 0, imy)

magnitude = np.sqrt(imx**2 + imy**2)

imlist = [im, imx, imy, magnitude]
tlist = ['original', 'sobel filter x', 'sobel filter y', 'gradient']
plt.figure(figsize=(15,10))
plt.gray()
for i, im, title in zip(range(4),imlist, tlist):
    plt.subplot(1,4,i+1)
    print(i)
    plt.imshow(im)
    plt.axis('off')
    plt.title(title)
plt.show()
