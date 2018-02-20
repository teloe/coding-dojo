const _ = {
	map: function(arr, callback){
		for (let i = 0; i < arr.length; i++) {
			array[i] = callback(array[i]);
		}
	},
	reduce: function(arr, callback, memo){
		let el = 0;
		if (!memo){
			memo = array[0];
			el = 1;
		}
		for(let i = el; i < arr.length; i++){
			memo = callback(arr[i], memo);
		}
		return memo;
	},
	find: function(arr, callback) {
		for (let i = 0; i < arr.length; i++){
			if (callback(arr[i])){
				return arr[i];
			}
		}
	},
	filter: function(arr, callback){
		const tempArr = [];
		for (let i = 0; i < arr.length; i++){
			if (!callback(arr[i])){
				tempArr.push(arr[i]);
			}
		}
		return tempArr;
	},
}

const arr = [2,3,4];
_.map(array, function callback(x) { return x * 5; });
console.log(array);
console.log(_.reduce(array, function callback(x, memo) { return x + memo; }));
console.log(_.find(array, function callback(x) { return x === 15; }));
// note: we used named functions for clarity above, but we can also pass anonymous functions as the second parameter:
console.log(_.filter(array, function(x) { return x > 20; }));