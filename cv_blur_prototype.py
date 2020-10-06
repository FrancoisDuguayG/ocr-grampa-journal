try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# # Simple image to string
# print(pytesseract.image_to_string(Image.open('../tests/data/test.png')))
#
# # French text image to string
# print(pytesseract.image_to_string(Image.open('../tests/data/test-european.jpg')))


img = cv2.imread('final.jpg', 1)
#-----Reading the image-----------------------------------------------------
cv2.imshow("img",img)

#-----Converting image to LAB Color model-----------------------------------

#-----Converting image from LAB Color model to RGB model--------------------
final = cv2.GaussianBlur(img, (3, 3), 0)
# cv2.imshow('final', final)
cv2.imwrite('final_blur3x3.jpg', final)



# print(pytesseract.image_to_string(Image.open('../tests/data/Feb18_letterjpg.jpg')))