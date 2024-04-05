'''
in this function we try to denoise the image with salt and peper noise
the best approach is to use medianBlur filter to denoise salt and peper noise 
first we seperate the red ,green and blue channel then we apply cv2.medianBlur()
for each channel and after that we merge the denoised channels
'''
import cv2

def Denoising(picture):

    b,g,r= cv2.split(picture)


    denoised_b = cv2.medianBlur(b, 3)
    denoised_g= cv2.medianBlur(g, 3)
    denoised_r = cv2.medianBlur(r, 3)
    
    final_image = cv2.merge([denoised_b, denoised_g, denoised_r])

    cv2.imwrite('denoised_image.png', final_image)

    return final_image