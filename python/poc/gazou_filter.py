import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import numpy.matlib as mlb
import scipy.signal as ss
import cis
import cv2

G = cv2.imread('cyclist-394274_640.jpg',0)
h,w = G.shape
fftsize = max(h,w)
plt.imshow(np.uint8(hp)+np.mean(G),cmap='gray')
x1 = np.uint8((np.float16(G)+float(np.float16(hp))/(float(np.max(G))+float(np.max(hp))))*255)
plt.imshow(x1,cmap='gray')
plt.show()