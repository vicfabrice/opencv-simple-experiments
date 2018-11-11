# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:14:00 2018

@author: VicFabrice
"""

import cv2



#Im not checking if I really have an image called image in the same folder as my program 
#because emmm i'll do it later

#Load image,the 2nd parameter is a flag, 1 is for color image, 0 is for greyscale, -1 = unchanged including alpha channel
#1 is default flag 
img = cv2.imread('image.jpg', 1)

#smaller pic
small = cv2.resize(img, (0,0), fx=0.2, fy=0.2)

#img is going GREY
imgray = cv2.cvtColor(small,cv2.COLOR_BGR2GRAY)

#saving my awesome work
cv2.imwrite('grayMe.png',imgray)

#show me the color me and then the grey me
#f you specify flag to be cv2.WINDOW_NORMAL, you can resize window
cv2.namedWindow('color image',cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('grey image',cv2.WINDOW_AUTOSIZE)

cv2.imshow('color image',small)
cv2.imshow('grey image',imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()

