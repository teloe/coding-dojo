// loading required modules
const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const session = require("express-session");
const path = require('path');

// configuring the app variable (middleware)
app.set('view engine', 'ejs')
app.use(bodyParser.urlencoded());
app.use(session({secret:"ThisIsASecret"}));
app.use(express.static(path.join(__dirname, 'static')));

// routing
app.get('/', function (req, res) {
	res.render("index");
})
app.post('/teams', function (req, res) {
	console.log(req.body);
	var fav_team = req.body;
	req.session.favTeamName = req.body.name;
	res.redirect('/result');
})
app.get('/result', function (req, res) {
	console.log(req.session);
	res.render("result", {teamName: req.session.favTeamName});
})

// activating the server
app.listen(8000, function () {
	console.log("Running on port 8000");
});