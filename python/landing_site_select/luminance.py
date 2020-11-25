import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('sample.jpg')
img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img,(512,512))
img_ = img.copy()
print(img.shape)
height = img.shape[0]
width = img.shape[1]

mu = np.mean(img)
sigma = np.var(img)
print(mu,sigma)
#plt.imshow(img,cmap='gray')
#plt.show()

F = 16
print(height)
img_suihei = np.zeros((height,width))
img_heitan = np.zeros((height,width))
heitan_list = []
Vthm = 0.2
for h in range(F//2,height-(F//2),1):
    for w in range(F//2,width-(F//2),1):
        #print(h,w)
        roi = img[(h-F//2):(h+F//2),(w-F//2):(w+F//2)]
        mu_ = np.mean(roi)
        #print("mu_",mu_)
        sigma_ = np.var(roi)

        roi_mu = (mu_-mu)/np.sqrt(sigma)
        roi_s = np.sqrt(sigma_)/np.sqrt(sigma)
        #print(roi_mu)
        #print(roi_s)
        img_suihei[h,w] = np.abs(roi_mu) #水平度
        img_heitan[h,w] = roi_s #平坦度

        #if np.abs(roi_mu)<=Vthm: # 水平度が一定の閾値を満たす領域
        heitan_list.append(np.abs(roi_s))

heitan_list.sort()
heitan_thr = heitan_list[300]
print("========",heitan_thr) # 平坦度が高い順


fig = plt.figure()
ax = fig.add_subplot(111)
im = ax.imshow(img_suihei,cmap='jet')
fig.colorbar(im)
fig.savefig('img_suihei.png')
plt.imshow(img_heitan,cmap='jet')
plt.show()

c = 0.55
heitan_list = []
img_suihei_binary = np.zeros((height,width))
img_heitan_binary = np.zeros((height,width))

Vthm = np.mean(img_suihei)
Vths = c*np.mean(img_heitan)
for h in range(F//2,height-(F//2),1):
    for w in range(F//2,width-(F//2),1):
        heitan_roi = img_heitan[(h-F//2):(h+F//2),(w-F//2):(w+F//2)]
        suihei_roi = img_suihei[(h-F//2):(h+F//2),(w-F//2):(w+F//2)]
        #Vthm = np.sum(roi)/F
        # 閾値設定は高いほど輝度分散が高いので、低く設定するほうが安全です
        #Vthm = 0.2 #水平度
        #Vthm = np.mean(suihei_roi)
        #Vths = c*img_heitan[h,w]/F
        #Vths = 0.2 #平坦度
        #Vths = c * np.mean(heitan_roi)
        if img_heitan[h,w] <= Vths:
            #plt.imshow(roi)
            #plt.show()

        #if np.abs(img_suihei[h,w]) < Vthm:
            img_heitan_binary[h,w] = 1
            #plt.imshow(img[(h-F//2):(h+F//2),(w-F//2):(w+F//2)],cmap='gray')
            #plt.show()
        else:
            img_heitan_binary[h,w] = 0
        if np.abs(img_suihei[h,w]) < Vthm:
            img_suihei_binary[h,w] = 1
        else:
            img_suihei_binary[h,w] = 0
        

        

img_[(img_suihei_binary==1) & (img_heitan_binary==1)] = 255



plt.imshow(img_suihei_binary*255,cmap='gray')
plt.show()

plt.imshow(img_heitan_binary*255,cmap='gray')
plt.show()

plt.imshow(img_,cmap='gray')
plt.show()

