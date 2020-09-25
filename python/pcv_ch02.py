
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.ndimage import filters
import harris

im1 = np.array(Image.open('data/sf_view1.jpg'))
im2 = np.array(Image.open('data/sf_view2.jpg'))

# 比較する画像の表示
plt.figure()
plt.subplot(1,2,1)
plt.imshow(im1)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(im2)
plt.axis('off')
plt.show()

def imresize(im,sz):
    """    Resize an image array using PIL. """
    pil_im = Image.fromarray(np.uint8(im))
    
    return np.array(pil_im.resize(sz))

# 比較する際は白黒写真にする
im1 = np.array(Image.open("data/sf_view1.jpg").convert("L"))
im2 = np.array(Image.open("data/sf_view2.jpg").convert("L"))
print(im1.shape)
print(im2.shape)

# イメージのリサイズを行う
# Python 3.xでは除算の結果をintにする場合、'//'を使う
im1 = imresize(im1,(im1.shape[1]//2,im1.shape[0]//2))
im2 = imresize(im2,(im2.shape[1]//2,im2.shape[0]//2))
print(im1.shape)
print(im2.shape)
# ２枚の画像のHarrisコーナー点の算出を行い、一致する点を線で結ぶ
wid = 5
harrisim = harris.compute_harris_response(im1,5) 
filtered_coords1 = harris.get_harris_points(harrisim,wid+1) 
print("filtered_coords1:",filtered_coords1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)
print("d1 :",d1)
harrisim = harris.compute_harris_response(im2,5) 
filtered_coords2 = harris.get_harris_points(harrisim,wid+1) 
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

print('starting matching')
matches = harris.match_twosided(d1,d2)

plt.figure(figsize=(15,15))
plt.gray() 
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches) 
plt.show()
"""
# 画像の読み込み
im = np.array(Image.open('data/empire.jpg').convert('L'))
# Harris検出器による画像の処理
harrisim = harris.compute_harris_response(im)
print(harrisim.shape)

# min_dist=6, threshold=0.1でHarrisコーナー点を抽出する
filtered_coords = harris.get_harris_points(harrisim, min_dist=6, threshold=0.1)

# 画像上にHarrisコーナー点をプロットする
harris.plot_harris_points(im, filtered_coords)
"""