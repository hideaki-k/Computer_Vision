import cv2
import numpy as np
from matplotlib import pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 25, 20

#grayscaleで読み込み
img = cv2.imread('test.jpg',0)

#フーリエ変換
f = np.fft.fft2(img)
#画像中心を原点に変更
fshift = np.fft.fftshift(f)
#フーリエ変換結果は複素数なので絶対値にし、logにしている
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()