
var h1Element = document.querySelector("h1");
console.log(h1Element);

var articleElement = document.querySelector("article");
var paragraphs = articleElement.querySelectorAll("p");
var lastParagraph = paragraphs[paragraphs.length - 1];
articleElement.removeChild(lastParagraph);

var h2Element = document.querySelector("#h2-chocolate");
h2Element.addEventListener("click", function() {
    h2Element.style.backgroundColor = "red";
});

var h3Element = document.querySelector("#h3-history");
h3Element.addEventListener("click", function() {
    h3Element.style.display = "none";
});

var boldButton = document.querySelector("#bold-button");
var allParagraphs = document.querySelectorAll("p");
boldButton.addEventListener("click", function() {
    allParagraphs.forEach(function(paragraph) {
        paragraph.style.fontWeight = "bold";
    });
});

h1Element.addEventListener("mouseover", function() {
    var randomSize = Math.floor(Math.random() * 101);
    h1Element.style.fontSize = randomSize + "px";
});


var secondParagraph = document.querySelectorAll("p")[1];
secondParagraph.addEventListener("mouseover", function() {
    secondParagraph.style.opacity = "0";
});
