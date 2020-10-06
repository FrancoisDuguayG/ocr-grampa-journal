try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt



print(pytesseract.image_to_string(Image.open('heros.jpg')))