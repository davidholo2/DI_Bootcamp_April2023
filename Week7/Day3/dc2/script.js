// Using one loop
var pattern = "";
for (var i = 1; i <= 6; i++) {
  pattern += "* ";
  console.log(pattern);
}


// Using two nested loops
for (var i = 1; i <= 6; i++) {
    var pattern = "";
    for (var j = 1; j <= i; j++) {
      pattern += "* ";
    }
    console.log(pattern);
  }
  