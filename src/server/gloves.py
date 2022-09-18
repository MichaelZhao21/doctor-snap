from fastai.vision.all import *
import cv2
from makemodel import *
import dill
import numpy as np

model = train_model()

def cut_img(img, crop):
    color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(color_coverted)
    cropped_im = pil_im.crop(tuple(crop))
    cv_im = np.array(cropped_im)
    cv_im = cv_im[:, :, ::-1].copy()
    return cv_im

def is_gloved(im):
    im_small = cv2.resize(im, (120, 120))
    im_blur = cv2.GaussianBlur(im_small, (3, 3), 0)
    glove_check, _, p = model.predict(im_blur)
    if p[0] > 0.3:
        return True
    return False
