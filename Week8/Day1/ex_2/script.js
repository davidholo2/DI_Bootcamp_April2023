
setTimeout(function() {
    alert("Hello World");
}, 2000);

setTimeout(function() {
    var container = document.getElementById("container");
    var newParagraph = document.createElement("p");
    newParagraph.textContent = "Hello World";
    container.appendChild(newParagraph);
}, 2000);
