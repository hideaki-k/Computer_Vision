import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('sample.jpg')
img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
print(img.shape)
height = img.shape[0]
width = img.shape[1]

mu = np.mean(img)
sigma = np.var(img)
print(mu,sigma)
plt.imshow(img,cmap='gray')
plt.show()

F = 16
print(height)
img_suihei = np.zeros((height,width))
img_heitan = np.zeros((height,width))

for h in range(F//2,height-(F//2),1):
    for w in range(F//2,width-(F//2),1):
        #print(h,w)
        roi = img[h:h+F,w:w+F]
        mu_ = np.mean(roi)
        print("mu_",mu_)
        sigma_ = np.var(roi)

        roi_mu = (mu_-mu)/np.sqrt(sigma)
        roi_s = np.sqrt(sigma_)/np.sqrt(sigma)
        print(roi_mu)
        print(roi_s)
        img_suihei[h,w] = np.abs(roi_mu)
        img_heitan[h,w] = roi_s

print(img_suihei)
cm = plt.cm.get_cmap('RdYlBu')

fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(img_suihei,cmap='jet')
fig.colorbar(im)
fig.savefig('colorbar1.png')
plt.imshow(img_heitan,cmap='jet')
plt.show()