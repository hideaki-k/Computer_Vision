import cv2
import numpy as np

img1 = cv2.imread('test.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
akaze = cv2.AKAZE_create()
kp1 = akaze.detect(gray1)
img1_akaze = cv2.drawKeypoints(gray1, kp1, None, flags=4)
cv2.imshow("image", img1_akaze)
cv2.waitKey(0)
cv2.destroyAllWindows()