import cv2


inMat = cv2.imread("hand.png")
def OpenCV_Access_RGBValue(inMat):

#dosya boyutlarını belirledim
    h = inMat.shape[0]
    w = inMat.shape[1]


    for y in range(0, h):
        for x in range(0, w):

#pikselin sınırlarını belirliyoruz
            b = inMat[y, x, 0]
            g = inMat[y, x, 0]
            r = inMat[y, x, 0]

#görüntünün negatifini bulmak için değerleri 255'den çıkarıyoruz
            b = 255 - b
            g = 255 - g
            r = 255 - r

            inMat[y, x, 0] = b
            inMat[y, x, 1] = g
            inMat[y, x, 2] = r


    return inMat

OpenCV_Access_RGBValue(inMat)

# display
cv2.namedWindow("tersi", 0)
cv2.imwrite("out.png", inMat)
cv2.imshow("tersi", inMat)
cv2.waitKey(0)
