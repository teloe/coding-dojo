function zeroNegativity(arr) {
			for (let i = 0; i < arr.length; i++) {
				if (arr[i] < 0){
					return false;
				}
			}
			return true;
		}

		// 2
		function isEven(num) {
			if (num % 2 === 0) {
				return true;
			} else {
				return false;
			}
		}

		// 3
		function howManyEven(arr) {
			let sum = 0;
			for (let i =0; i < arr.length; i++) {
				if (isEven(arr[i])) {
					sum += 1;
				}
			}
			return sum;
		}

		// 4
		function createDummyArray(num) {
			const arr = [];
			for (let i = 0; i < num; i++) {
				arr.push(Math.floor(Math.random() * 10));
			}
			return arr;
		}

		// 5
		function randomChoice(arr) {
			let index = Math.floor(Math.random() * arr.length);
			return arr[index];
		}