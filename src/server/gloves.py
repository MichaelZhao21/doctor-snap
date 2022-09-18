from fastai.vision.all import *
import cv2
import dill

model = load_learner('model.pkl')

def cut_img(img, crop):
    cropped_im = img.crop(tuple(crop))
    return cropped_im

def is_gloved(im):
    im_small = cv2.resize(im, (120, 120))
    im_blur = cv2.GaussianBlur(im_small, (3, 3), 0)
    glove_check, _, _ = model.predict(im_blur)
    return glove_check
