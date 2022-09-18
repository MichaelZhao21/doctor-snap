const express = require('express');
const path = require('path');
const app = express();

app.use(express.static('downloads'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/sketch.js', (req, res) => {
    res.sendFile(__dirname + '/sketch-gloves.js');
});

app.listen(3000, () => console.log('Server started on port 3000!'));
