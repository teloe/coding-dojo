function Ninja(name) {
			this.name = name;
			this.health = 100;
			var speed = 3;
			var strength = 3;

			this.showStats = function() {
				console.log("Name: " + this.name + ", Health: " + this.health + ", Speed: " + speed + ", Strength: " + strength);
				return this;
			}
		}

		Ninja.prototype.sayName = function() {
			console.log("My name is " + this.name);
			return this;
		}

		Ninja.prototype.drinkSake = function(){
			this.health += 10;
			return this;
		}

		Ninja.prototype.punch = function(){
			this.health -= 5;
			console.log("Goemon was punched by Bill Gates and lost 5 health!")
			return this;
		}

		Ninja.prototype.kick = function(){
			this.health -= 15;
			console.log("Bill Gates was kicked by Goemon and lost 15 Health!")
			return this;
		}
		

		// var ninja1 = new Ninja("Goemon");
		// ninja1.sayName();
		// ninja1.showStats();

		var blue_ninja = new Ninja("Goemon");
		var red_ninja = new Ninja("Bill Gates");
		red_ninja.punch(blue_ninja);
		// -> "Goemon was punched by Bill Gates and lost 5 Health!"

		blue_ninja.kick(red_ninja);
		// -> "Bill Gates was kicked by Goemon and lost 15 Health!"


