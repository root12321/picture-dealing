import cv2
import numpy as np
img = cv2.imread("D:\\tensflow\\1.png")
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',emptyImage3)
cv2.waitKey(0)
#th2 = cv2.adaptiveThreshold(emptyImage3,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,0)
def Cvpointgray(img):
    y=[]
    for i in range(1,img.shape[1]):
        x=[]
        for j in range(1,img.shape[0]):
            x.append(img[j,i])
            #print(x)
        a=x.index(max(x))
        y.append(a)

    return y
z=Cvpointgray(emptyImage3)
print(z)
# cv2.imshow('img',Cvpointgray(emptyImage3))
# cv2.waitKey(0)






