document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("myForm");
    console.log(form);
  
    var fnameInput = document.getElementById("fname");
    var lnameInput = document.getElementById("lname");
    console.log(fnameInput);
    console.log(lnameInput);
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
  
      var fnameValue = fnameInput.value;
      var lnameValue = lnameInput.value;
  
      if (fnameValue.trim() !== "" && lnameValue.trim() !== "") {
        var ul = document.querySelector(".usersAnswer");
        var fnameLi = document.createElement("li");
        var lnameLi = document.createElement("li");
  
        fnameLi.textContent = "First name: " + fnameValue;
        lnameLi.textContent = "Last name: " + lnameValue;
  
        ul.appendChild(fnameLi);
        ul.appendChild(lnameLi);
      }
    });
  });
  