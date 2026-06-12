const menuparser = require("./menu_parser.js")
menuparser.ParseMenu()

const path = require("path");

const express = require("express");
const app = express();

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"))
})

app.listen(8080);