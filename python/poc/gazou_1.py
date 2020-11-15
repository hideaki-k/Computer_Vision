import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack as sfft
import numpy.matlib as mlb
import scipy.signal as ss
import cis
import cv2


C = cv2.imread("paprika-966290_640.jpg")
C = cv2.cvtColor(C, cv2.COLOR_BGR2GRAY)
plt.imshow(C,cmap='gray')
plt.show()
BW = np.zeros((640,480))
BW[np.logical_and(np.logical_and(np.logical_and(C[:,:,0]>150,c[:,:,0]<240),np.logical_abd(np.logical_and(C[:,:,1]>80,c[:,:,1]<220)),C[:,:,2]<40)]=1

R=C.copy()
R[BW==0]=0
plt.imshow(R)
plt.show()
"""
Ired = cv2.imread('redpepper.jpg')
h,w,b = Ired.shape
I = cv2.imread('paprika-966290_640.jpg')
plt.imshow(cv2.cvtColor(I,cv2.COLOR_BGR2RGB))

#plt.show()
Iyellow = I[155:155+h,390:390+w]
Imixed=Iyellow/2+Ired/2
Imixed = Imixed.astype(np.uint8)
plt.imshow(cv2.cvtColor(Imixed,cv2.COLOR_BGR2RGB))

#plt.show()
"""
"""
A = np.zeros((3,4,3),np.int8)
B1 = np.arange(12).reshape(3,4)
B2 = B1 + 100
B3 = B2 + 100
print(B1)
print(B2)
A[:,:,0] = B1
A[:,:,1] = B2
A[:,:,2] = B3
print(A)
print("=================")
print(A[:,2])
"""