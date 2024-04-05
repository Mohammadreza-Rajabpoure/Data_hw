from src.denoising import Denoising
from src.remove_backgroung import Remove_bg
from src.sharpening import Sharpen
import os
import cv2

path = os.path.relpath('data/noisy_cat.jpeg')

def main():
     image = cv2.imread(path)

     denoised_img = Denoising(image)

     bg_removed_img = Remove_bg(denoised_img)

     sharpen_img = Sharpen(bg_removed_img)

     return sharpen_img,bg_removed_img,denoised_img

if __name__=="__main__":
     main()