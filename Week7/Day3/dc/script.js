var sentence = prompt("Enter a sentence:");
var wordNot = sentence.indexOf("not");
var wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
  var result = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
} else {
  var result = sentence;
}

console.log(result);
