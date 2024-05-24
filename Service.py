from PIL import Image
import pytesseract
import numpy as np


def recognize_words_by_photo(image):
    arrayImage = np.array(Image.open(image))
    return pytesseract.image_to_string(arrayImage)
