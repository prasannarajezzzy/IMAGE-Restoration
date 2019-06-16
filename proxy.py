
import cv2
import numpy as np
img = cv2.imread('img.jpg')
cv2.imshow("real image",img)
cv2.waitKey(0)

#load imge
markdam = cv2.imread('mask.jpg',0)
cv2.imshow('marked',markdam)
cv2.waitKey(0)


ret, thresh1 = cv2.threshold(markdam,254,255,cv2.THRESH_BINARY)
cv2.imshow('thresold',thresh1)
cv2.waitKey(0)

kernel  = np.ones((7,7),np.uint8)
mask = cv2.dilate(thresh1,kernel , iterations=1)

cv2.imshow('dillate',mask)
cv2.imwrite('broken2.png',mask)
cv2.waitKey(0)

restored = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)

cv2.imshow('restored',restored)

cv2.waitKey(0)
cv2.destroyAllWindows()







