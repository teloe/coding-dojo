var express = require("express");
var path = require("path");
var bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({extended: true}));

// static content
app.use(express.static(path.join(__dirname, 'static')));

// setting up ejs and views folder
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// tell express app to listen on port 8000
var server = app.listen(8000, function(){
	console.log("listening on port 8000");
});

require('./routes/index.js')(app, server);