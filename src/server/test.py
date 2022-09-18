from gloves import is_gloved
import cv2
from makemodel import *

im = cv2.imread('glove.jpg')
a = is_gloved(im)
print(a)
