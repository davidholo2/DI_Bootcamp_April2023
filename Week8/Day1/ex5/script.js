var element = document.getElementById("myElement");

// Event listener for click event
element.addEventListener("click", function() {
    element.style.left = "50px"; // Change position x
});

// Event listener for mouseover event
element.addEventListener("mouseover", function() {
    element.style.top = "50px"; // Change position y
});

// Event listener for mouseout event
element.addEventListener("mouseout", function() {
    element.style.backgroundColor = "blue"; // Change color
});

// Event listener for double click event
element.addEventListener("dblclick", function() {
    element.style.fontSize = "24px"; // Change font size
});
