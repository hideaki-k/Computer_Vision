import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.ndimage import filters


# SIFT特徴量計算のためのモジュール
import sift

# 対象の画像ファイルのパス
imname = 'data/empire.jpg'
# SIFT特徴量のファイルパス
siftname = 'data/empire.sift'
# 画像の読み込み
im1 = np.array(Image.open(imname).convert('L'))
# SIFT特徴量を計算して、SIFTファイルを出力する
sift.process_image(imname, 'dammy.sift')
# SIFT特徴量の読み込み
l1, d1 = sift.read_features_from_file(siftname)


# SIFT特徴点の描画
plt.figure(figsize=(10,10))
plt.gray()
sift.plot_features(im1, l1, circle=True)
plt.show()