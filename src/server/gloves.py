from fastai.vision.all import *

model = load_learner('model.pkl')

def cut_img(img, crop):
    cropped_im = img.crop(tuple(crop))
    return cropped_im

def is_gloved(img):
    glove_check, _, _ = model.predict(img)
    return glove_check
