import cv2
from fingerprint_enhancer import *

image1 = cv2.imread("./BTL_HTTM/Database/Train/DB4_B_2004/101_1.tif",cv2.IMREAD_GRAYSCALE) # vân tay trong database
image = cv2.imread("./BTL_HTTM/z3723177660338_853a74371d544eac0a3f1611ea13eea31.jpg",cv2.IMREAD_GRAYSCALE) # vân tay chụp ảnh

size=400

# Xử lí vân tay chụp

image = cv2.resize(image, (size, size))
cv2.namedWindow("image")
cv2.resizeWindow('image', size, size)

clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(64,64))

image = clahe.apply(image)

(thresh, blackAndWhiteImage) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

for i in range(blackAndWhiteImage.shape[0]):
    for j in range(blackAndWhiteImage.shape[1]):
        if blackAndWhiteImage[i, j] ==0:
            image[i, j] = 255

image = enhance_Fingerprint(image)

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        image[i,j]=255-image[i,j]

cv2.imshow('image',image)


# Xử lí vân tay trong database

image1 = cv2.resize(image1, (size, size))
cv2.namedWindow("image1")
cv2.resizeWindow('image1', size, size)

image1 = enhance_Fingerprint(image1)

for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        image1[i,j]=255-image1[i,j]

cv2.imshow('image1',image1)

cv2.waitKey(0)
cv2.destroyAllWindows()