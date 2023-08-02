# mini project 11
# Install the following:
'''
!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install Pillow==9.0.0
'''

from google.colab import files

uploaded = files.upload()

import pytesseract
from PIL import Image
extractedInformation = pytesseract.image_to_string(Image.open('D:\Coding\Python programmming\summer_school\image.png'))
print(extractedInformation)