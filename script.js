const menuparser = require("./menu_parser.js")

const path = require("path");

const express = require("express");
const app = express();

app.get('/', (req, res) => {
    menuparser.ParseMenu()
    res.sendFile(path.join(__dirname, "index.html"))
})

app.listen(8080);