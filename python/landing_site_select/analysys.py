import cv2

img = cv2.imread('imgsh_20081102T071400_wm8_fp_l_101.jpg')
print(img.size)
print(img.shape)
color = img[300,300,:]
print(color)