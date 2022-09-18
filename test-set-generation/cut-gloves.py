import json
import shutil
import os
from PIL import Image

# Clear output directory
if os.path.exists('cropped'):
    shutil.rmtree('cropped')
os.mkdir('cropped')

with open('bounds-data.json') as f:
    data = json.load(f)

# Loop through the list of data
for image_data in data:
    # Extract ID and crops for current image
    id = image_data['id']
    crop = image_data['crop']

    # Open image
    im = Image.open(f'downloads/{id}.jpg')

    # Loop through crops
    if (crop[0] < crop[2] and crop[1] < crop[3]):
        cropped_im = im.crop(tuple(crop))
        cropped_im.save(f'cropped/y-{id}.jpg')
    
    print(f'Completed image {id}!')
