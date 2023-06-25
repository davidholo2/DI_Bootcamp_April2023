var allBoldItems;

function getBoldItems() {
  var paragraph = document.querySelector("p");
  allBoldItems = paragraph.querySelectorAll("strong");
}

function highlight() {
  for (var i = 0; i < allBoldItems.length; i++) {
    allBoldItems[i].style.color = "blue";
  }
}

function returnItemsToDefault() {
  for (var i = 0; i < allBoldItems.length; i++) {
    allBoldItems[i].style.color = "black";
  }
}

document.addEventListener("DOMContentLoaded", function() {
  getBoldItems();

  var paragraph = document.querySelector("p");
  paragraph.addEventListener("mouseover", highlight);
  paragraph.addEventListener("mouseout", returnItemsToDefault);
});
