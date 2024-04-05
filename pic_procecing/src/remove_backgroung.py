'''
for removig the background of the image we used the rembg model
'''
import rembg
import cv2

def Remove_bg(image):

    removed_bg = rembg.remove(image)

    cv2.imwrite('bg_removed.png', removed_bg)

    return removed_bg