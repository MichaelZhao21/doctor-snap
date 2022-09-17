# Project for HackSMU 2022

Currently a WIP :)

## Downloading Images

Change to the `test-set-generation` directory. Run `yarn install` to install the necessary packages. Add URLs to the `input-urls.txt` file and then run `node download-images.js` to download, and they will appear in the `test-set-generation/downloads` folder.

## Creating Bounding Boxes on Images

Once the images are downloaded, run `node create-bounding.js`. This will open up a browser where you can interactively create bounding boxes. Do this by clicking once to start a selection and a second time with the bottom right corner of the selection. If you wish to cancel a selection, simply hit the Escape key. Once all selections have been made on an image, you can press Enter to go to the next image.

## Cropping the Images using Manually Created Bounding Boxes

// TODO: Python
