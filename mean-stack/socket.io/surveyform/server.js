var express = require("express");
var path = require("path");
var bodyParser = require("body-parser");

// create the express app
var app = express();

app.use(bodyParser.urlencoded());

// static content
app.use(express.static(path.join(__dirname, "./static")));

// setting up ejs and views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// tell express app to listen to port 3000
var server = app.listen(3000, function(){
	console.log("listening on port 3000");
})

// have /routes/index.js handle all of the routing
var route = require('/routes/index.js')(app.server);