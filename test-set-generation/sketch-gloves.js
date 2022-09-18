let img;
let loading;
let aggRectList = [];
let aggIndex = [];
let rectList = null;
let done = false;
let button;
let startX;
let startY;
let adj;
let notAdj = true;

let curr = 0,
    total = 102;

function setup() {
    createCanvas(windowWidth, windowHeight);
}

function draw() {
    background(249, 239, 252);
    if (curr === 102) {
    // if (curr === 6) {
        // We are DONE!!!!
        done = true;
        textSize(50);
        text('YOU ARE DONE!!!!', 10, 50);

        // Draw button to download file
        button = createButton('Download data');
        button.position(10, 70);
        button.mousePressed(downloadData);
        return;
    }
    textSize(32);
    text(`Image ${curr + 1}/${total}`, 10, 50);
    if (!img && !loading) {
        loading = true;
        try {
            fetch(`${curr}.jpg`).then((res) => {
                if (res.ok) {
                    loadImage(`${curr}.jpg`, (i) => {
                        loading = false;
                        img = i;
                        notAdj = true;
                    });
                } else {
                    loading = false;
                    img = null;
                    curr++;
                }
            });
        } catch (e) {
            loading = false;
            img = null;
            curr++;
        }
    }
    if (img && notAdj) {
        adj = 1;
        adj = grow(img.height, adj);
        adj = shrink(img.height, adj);
        img.resize(img.width * adj, img.height * adj);
        notAdj = false;
    }
    if (img) {
        image(img, 10, 80);
    }
    fill('rgba(249, 192, 107, 0.2)');
    let w = mouseX - startX;
    let h = mouseY - startY;
    if (w > h) {
        h = w;
    } else {
        w = h;
    }
    if (startX) rect(startX, startY, w, h);
    fill('rgba(0, 0, 0, 1)');
}

function grow(x, acc) {
    if (x * acc < windowHeight * 0.75) {
        return grow(x, acc * 1.2);
    }
    return acc;
}

function shrink(x, acc) {
    if (x * acc > windowHeight * 0.95) {
        return shrink(x, acc / 1.2);
    }
    return acc;
}

function downloadData() {
    const data = aggIndex.map((ind, i) => ({
        id: ind,
        crop: aggRectList[i],
    }));
    createStringDict(data).saveJSON('bounds-data');
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
}

function keyPressed() {
    if (done) return;
    if (key === 'Escape') {
        startX = null;
        startY = null;
    }
}

function mouseClicked() {
    if (done) return;

    if (startX) {
        // complete rectangle
        rectList = [
            (startX - 10) / adj,
            (startY - 80) / adj,
            (mouseX - 10) / adj,
            (mouseY - 80) / adj,
        ];

        // move to next pic
        aggRectList.push(rectList);
        aggIndex.push(curr);
        rectList = null;
        rectDisplayList = null;
        curr++;
        
        img = null;
        startX = null;
        startY = null;
    } else {
        // Start rectangle
        startX = mouseX;
        startY = mouseY;
    }
}
