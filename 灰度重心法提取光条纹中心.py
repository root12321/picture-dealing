import cv2
import numpy as np
img = cv2.imread("D:\\tensflow\\1.png")
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',emptyImage3)
cv2.waitKey(0)
def Cvpointgray(img):
    x=[]
    x0=0;y0=0
    for i in range(img.shape[1]):
        for j in range(1,img.shape[0]):
            x0=x0+img[j,i]
            y0=y0+img[j,i]*j
        y=y0/x0
        y=round(y)
        x.append(y)
    return x
print(Cvpointgray(emptyImage3))











