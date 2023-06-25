var element = document.getElementById("myElement");


element.addEventListener("click", function() {
    element.style.left = "50px"; 
});

element.addEventListener("mouseover", function() {
    element.style.top = "50px"; 
});

element.addEventListener("mouseout", function() {
    element.style.backgroundColor = "blue"; 
});

element.addEventListener("dblclick", function() {
    element.style.fontSize = "24px";
});
