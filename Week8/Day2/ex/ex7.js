(function(userName) {
    const userInfoDiv = document.getElementById("user-info");
  
    // Create a span for the user's name
    const userNameSpan = document.createElement("span");
    userNameSpan.textContent = userName;
  
    // Create an image for the user's profile picture
    const profileImage = document.createElement("img");
    profileImage.src = "profile-picture.jpg";
    profileImage.alt = "Profile Picture";
  
    // Append the user's name and profile picture to the user info div
    userInfoDiv.appendChild(userNameSpan);
    userInfoDiv.appendChild(profileImage);
  })("John");
  