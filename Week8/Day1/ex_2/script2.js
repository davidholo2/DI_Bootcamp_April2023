function myMove() {
    var container = document.getElementById("container");
    var animate = document.getElementById("animate");

    var containerWidth = container.offsetWidth;
    var animateWidth = animate.offsetWidth;

    var position = 0;
    var interval = setInterval(frame, 1);

    function frame() {
        if (position >= containerWidth - animateWidth) {
            clearInterval(interval);
        } else {
            position++;
            animate.style.left = position + "px";
        }
    }
}
