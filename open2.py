import cv2
import numpy as np
import matplotlib.pyplot as plt
def hist_plot(img):

#sayıyı tutmak icin bir bos liste olusturdum
    count = []

#göruntu yogunlugunu tutmak ıcın bos lıste

    r = []
    for k in range(0, 256):
        r.append(k)
        count1 = 0

#pikseli gecmek ıcın dongu olusturdum
        for i in range(m):
            for j in range(n):
                if img[i, j] == k:
                    count1 += 1
        count.append(count1)

    return (r, count)


img = cv2.imread('hand.png', 0)

#goruntunun boyutu
m, n = img.shape
r1, count1 = hist_plot(img)

#histogramı cızmek ıcın
plt.stem(r1, count1)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('esas görüntünün histogramı')

#gerılmeyı elde etmek ıcın donusum
constant = (255 - 0) / (img.max() - img.min())
img_stretch = img * constant
r, count = hist_plot(img_stretch)

# histogramı çizmek
plt.stem(r, count)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('gerilmiş görüntünün histogramı')

