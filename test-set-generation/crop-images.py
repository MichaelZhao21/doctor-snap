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
    crops = image_data['crops']

    # Open image
    im = Image.open(f'downloads/image-{id}.png')

    # Loop through crops
    for i, crop in enumerate(crops):
        cropped_im = im.crop(tuple(crop))
        cropped_im.save(f'cropped/image-{id}-{i}.png')
    
    print(f'Completed image {id}, cropped {len(crops)} images!')
