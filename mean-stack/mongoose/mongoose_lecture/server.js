// LOADING MODULES
const express = require('express');
			bodyParser = require('body-parser');
			mongoose = require('mongoose');
			path = require('path');


// CREATE EXPRESS APP
const app = express();

// SETTING UP EXPRESS
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname, 'static')));

// CONNECTING TO MONGODB
mongoose.connect('mongodb://localhost/mongoose_pizzas');

// DEFINE A MONGOOSE SCHEMA
let Schema = mongoose.Schema;
var pizzaSchema = mongoose.Schema({
	name: {type: String, minlength: 4, presence: true},
	cheese: String,
	toppings: String
});

var chefSchema = mongoose.Schema({
	name: {type: String, presence: true},
	pizzas: [{type: Schema.types.ObjectId, ref: "Pizza"}]
})

// REGISTER SCHEMAS INTO MODELS
mongoose.model("Pizza", pizzaSchema);
mongoose.model("Chef", chefSchema);
let Pizza = mongoose.model("Pizza");
let Chef = mongoose.model("Chef");

// ROUTING
app.get('/', (req, res)=>{
	Chef.find({}, (err, chefs)=>{
		if(err){
			console.log("Something went wrong");
			res.json(err);
		} else {
			console.log("Got all chefs");
			res.render('index', {allChefs: chefs, errors:{}})
		}
	})
})

app.post('/chefs', (req, res)=>{
	let newChef = new Chef(req.body);
	newChef.save((err)=>{
		if(err){
			console.log("Something went wrong");
			res.json(err);
		} else {
			console.log("Made a new chef");
			res.redirect('/');
		}
	})
})

// SERVER LISTENING
app.listen(8000, ()=>{
	console.log("Running on port 8000");
})

