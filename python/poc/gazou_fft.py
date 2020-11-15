import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import numpy.matlib as mlb
import scipy.signal as ss
import cis
import cv2

G = cv2.imread('building-1081868_640.jpg',0)
plt.imshow(G,cmap='gray')
plt.show()

plt.plot(G[250,:]) # height250のピクセルの横方向輝度値
plt.show()

plt.plot(np.log(np.abs(sfft.fft(G[250,:]))))
plt.show()

h,w = 64,64
x = np.array([np.arange(0,1,1/h)]).T
G = mlb.repmat(np.uint8(100*(np.sin(2*np.pi*5*x)+1)),1,w)
plt.subplot(311);plt.plot(x,G[:,0])
plt.subplot(312);plt.stem(np.abs(sfft.fft(G[:,0])))
S = sfft.fft(G,axis=0)
plt.show()
S2 = sfft.fft(S,axis=1)
#cis.stem3(np.abs(S2))