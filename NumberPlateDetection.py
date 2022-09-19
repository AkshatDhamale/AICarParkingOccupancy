import cv2
from xml.dom import minidom
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread('images/Cars34.png')
file = minidom.parse('annotations/Cars34.xml')

xmin = int(file.getElementsByTagName('xmin')[0].firstChild.data)
ymin = int(file.getElementsByTagName('ymin')[0].firstChild.data)
xmax = int(file.getElementsByTagName('xmax')[0].firstChild.data)
ymax = int(file.getElementsByTagName('ymax')[0].firstChild.data)

start = (xmin,ymin)
end = (xmax,ymax)
cv2.rectangle(img,start,end,(0,0,255),thickness=3, lineType=cv2.LINE_8)
image = img[start[1]:end[1], start[0]:end[0]]
cv2.imshow('Original image',image)

gry = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
flt = cv2.adaptiveThreshold(gry,
                            100, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 15, 16)

text = pytesseract.image_to_string(image)
print(text)
cv2.waitKey(0)