'''
Created on May 18, 2017

@author: neilagupta
'''

import numpy as np
import cv2

img = cv2.imread('Neil.png', 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('Neil.jpg', img)