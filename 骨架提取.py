from skimage import morphology,draw
import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("D:\\tensflow\\1.png")
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',emptyImage3)
cv2.waitKey(0)
ret, th2 = cv2.threshold(emptyImage3, 60, 255,cv2.THRESH_BINARY)
th3=th2/255
cv2.imshow('img',th3[2:th3.shape[0],0:th3.shape[1]])
cv2.waitKey(0)
cv2.destroyAllWindows()
skeleton =morphology.skeletonize(th3[2:th3.shape[0],0:th3.shape[1]])
skeleton=skeleton*255
skeleton= np.array(skeleton, dtype=np.uint8)
cv2.imshow('img',skeleton)
cv2.waitKey(0)
cv2.destroyAllWindows()





