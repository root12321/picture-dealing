import cv2
import glob as gb
import numpy as np
img_path = gb.glob("D:\Converted\*.jpg")
for i in img_path:
    img = cv2.imread(i)
    img=img[100:250,250:600]
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lower = np.array([90,65,90])
    upper = np.array([100,90,120])
    mask = cv2.inRange(img, lower, upper)
    output1 = cv2.bitwise_and(img, img, mask=mask)
    #frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('img',frame)
    # cv2.waitKey(0)
    ret1, th1 = cv2.threshold(frame, 110, 255, cv2.THRESH_BINARY)
    cv2.imshow('img',th1)
    cv2.waitKey(1)


