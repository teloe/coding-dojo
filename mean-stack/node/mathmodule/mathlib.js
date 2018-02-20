module.exports = function (){
	return {
		add: function(num1, num2){
			return a + b;
		},
		multiply: function(num1, num2){
			return a * b;
		},
		square: function(num){
			return a * a;
		},
		random: function(num1, num2){
			return Math.floor(Math.random() * 35) + 1;
		}
	}
};