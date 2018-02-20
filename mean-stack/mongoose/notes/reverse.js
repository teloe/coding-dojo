function reverse(a) {
    var i = 0;
    var j = a.length - 1;
    while (i < j) {
        var x = a[i];
        a[i] = a[j];
        a[j] = x;
        i++;
        j--;
    }
    console.log(a);
}

reverse([1,5,7]);
