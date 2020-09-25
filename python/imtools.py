import os
from pylab import *
from PIL import Image
from numpy import *

" pathに指定されたディレクトリの全てのjpgファイル名のリストを返す"
def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def histeq(im, nbr_bins=256):
    """グレースケール画像のヒストグラム平たん化"""
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # 累積分布関数
    cdf = 255 * cdf / cdf[-1] # 正規化

    # cdf を線形補完し新しいピクセル値とする
    im2 = interp(im.flatten(),bins[:-1],cdf)

    return im2.reshape(im.shape),cdf

def compute_average(imlist):
    """ 画像別の平均を求める """
    # 最初の画像を開き,浮動小数点の配列に変換する
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname+"...skipped")

    averageim /= len(imlist)
    # 平均をuint8　に変換する
    return array(averageim, 'uint8')

