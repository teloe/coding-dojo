// In place while loop
// function reverseA(a) {
// 	let i = 0;
// 	let j = a.length - 1;
// 	while(i < j) {
// 		let temp = a[i];
// 		a[i] = a[j];
// 		a[j] = temp;
// 		i++;
// 		j--;
// 	}
// 	console.log(a);
// }

// reverseA([1,2,3,4,5,6]);


// var reverseArr = (arr) => {
// 	var last = arr.length - 1;
// 	for (var i = 0; i < last; i++) {
// 		var x = arr[i];
// 		arr[i] = arr[last];
// 		arr[last] = x;
// 		last--;
// 	}
// 	console.log(arr);
// }

// reverseArr([1,2,3,4,5,6]);


let rArr = (arr) => {
	let newArr = [];
	for (var i = arr.length - 1; i >= 0; i--){
		newArr.push(arr[i]);
	}
	console.log(newArr);
}

rArr([1,2,3,4,5,6,7]);