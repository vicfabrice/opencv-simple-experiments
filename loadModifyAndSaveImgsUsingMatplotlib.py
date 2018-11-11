# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:14:00 2018

@author: VicFabrice
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt



#Im not checking if I really have an image called image in the same folder as my program 
#because emmm i'll do it later

#Load image,the 2nd parameter is a flag, 1 is for color image, 0 is for greyscale, -1 = unchanged including alpha channel
#1 is default flag 
img = cv2.imread('image.jpg', 0)


#show image in gray scale using matplotlib
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')

#dont know why it doesnt open a new window to display my image
plt.show()


