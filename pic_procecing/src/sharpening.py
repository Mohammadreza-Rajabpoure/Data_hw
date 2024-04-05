'''
in this function we used a filter matrix(kernel),to sharpen the image,
the filter matix substract a blurred version of the image
finaly we apply the filter matrix to the image using filter2D() function
then the function returnes a sharpend image.'''

import cv2
import numpy as np

def Sharpen(image):

    kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])

    sharpend_img = cv2.filter2D( image, -1, kernel)

    cv2.imwrite('sharpend_iamge.png' , sharpend_img)

    return sharpend_img