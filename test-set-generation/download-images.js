const fs = require('fs-extra');
const fetch = require('node-fetch');

/**
 * Downloads a single image
 * @param {String} img Image URL
 * @param {Number} i Index of list
 */
async function downloadImage(img, i) {
    if (img === '') return;
    console.log(`Downloading ${i}: ${img}`);
    try {
        await fetch(img)
            .then((res) => res.body.pipe(fs.createWriteStream(`./downloads/image-${i}.png`)))
            .then(() => {
                console.log(`Downloaded ${i}`);
            });
    } catch (e) {
        console.error(e);
    }
}

function main() {
    // Remove downloads folder
    try {
        fs.rmSync('./downloads', { force: true, recursive: true });
    } catch (e) {
        console.log('Downloads folder does not exist!');
    }

    // Create downloads folder
    fs.mkdirSync('downloads');

    // Read in input and split by new lines
    const input = fs.readFileSync('./input-urls.txt').toString().split('\n');

    // For each URL in the input, run the download image function
    input.forEach((img, i) => downloadImage(img, i));
}

main();
