from gloves import cut_img
from PIL import Image

with Image.open('glove.jpg') as im:
    ci = cut_img(im, (10, 10, 100, 100))
    ci.save('glove-cut.jpg')