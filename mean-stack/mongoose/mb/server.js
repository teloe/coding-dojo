const express = require('express');
			path = require('path');
			bodyParser = require('body-parser');
			mongoose = require('mongoose');
			app = express();


// CONNECT TO OUR DB
mongoose.connect('mongodb://localhost/super_awesome_message_b');
app.use(bodyParser.urlencoded({extended: false}));

// ESTABLISH OUR SCHEMAS
var Schema = mongoose.Schema;

var messageSchema = new Schema({
	name: String,
	message: String,
	_comments: []
})

var commentSchema = new Schema({
	name: String,
	comment: String,
	_message: String
})

var Message = mongoose.model('Message', messageSchema);
var Comment = mongoose.model('Comment', commentSchema);


app.set(express.static(path.join(__dirname, './static')));

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, './views'));


// ROUTING RULES
app.get('/', function(req, res){
	Message.find({}, function(err, output){
		if(err){
			console.log("Broken");
		} else {
			console.log(output);
			res.render('index', {messages: output});
		}
	})
})

app.post('/message/new', function(req, res){
	var new_message = new Message({name: req.body.name, mesage: req.body.mesage});
	new_message.save(function(err, output){
		if(err){
			console.log("The server messed up and it's Tom's fault!");
		} else {
			res.redirect('/');
			// res.render('index');
		}
	})
})

const server = app.listen(8000, ()=>{
	console.log("Listening on port 8000");
})