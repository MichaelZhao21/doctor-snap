import cv2
from fastai.vision.all import *

def process_img(name):
    im = cv2.imread(f'data/{name}.jpg')
    im_small = cv2.resize(im, (120, 120))
    im_blur = cv2.GaussianBlur(im_small, (3, 3), 0)
    im_final = None
    cv2.fastNlMeansDenoising(im_blur, im_final)
    cv2.imwrite(f'ready/{name}.jpg', im_blur)
    print(f'Processed {name}.jpg')

for i in range(1, 111):
    process_img(f'n-{i}')
for i in range(1, 102):
    process_img(f'y-{i}')

path = 'ready'

def has_glove(x): return x[0] == 'y'

dls = ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2, seed=42,
    label_func=has_glove, item_tfms=Resize(224))

learn = vision_learner(dls, resnet34, metrics=error_rate)
learn.fit_one_cycle(2, lr_max=slice(1e-4, 1e-3))
learn.fine_tune(1)

learn.export('./model.pkl')
