from gloves import *
import cv2
from makemodel import *

im = cv2.imread('glove.jpg')
cut_img(im, (0, 0, 1000, 1000))
a = is_gloved(im)
print(a)
