import cv2
from fastai.vision.all import *
import dill

def process_img(name):
    im = cv2.imread(f'data/{name}.jpg')
    im_small = cv2.resize(im, (120, 120))
    im_blur = cv2.GaussianBlur(im_small, (3, 3), 0)
    im_final = None
    cv2.fastNlMeansDenoising(im_blur, im_final)
    cv2.imwrite(f'ready/{name}.jpg', im_blur)
    print(f'Processed {name}.jpg')

def train_model():
    path = 'ready'
    dls = ImageDataLoaders.from_name_func(
        path, get_image_files(path), valid_pct=0.2, seed=42,
        label_func=lambda x: x[0] == 'y', item_tfms=Resize(224))

    learn = vision_learner(dls, resnet34, metrics=error_rate)
    # learn.fit_one_cycle(1, lr_max=slice(1e-4, 1e-3))
    learn.fine_tune(1)
    return learn

def has_glove(x): return x[0] == 'y'

def get_model():
    return load_learner('model.pkl')

if __name__ == '__main__':

    for i in range(1, 111):
        process_img(f'n-{i}')
    for i in range(1, 102):
        process_img(f'y-{i}')

    learn = train_model()

    learn.export('model.pkl', pickle_module=dill)

