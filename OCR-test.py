import cv2
import numpy as mp
import pytesseract  

pytesseract.pytesseract.tsseract_cmd = r"file:///home/snow/Downloads/tesseract-master"

img = cv2.imread(5832296680521840942.jpg)

test = pytesseract.image_to_string(img)
print(text)

cv2.imshow("Img", img)
cv2.waiKey(0)