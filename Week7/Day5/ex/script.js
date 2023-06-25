
function playTheGame() {
    var playGame = confirm("Would you like to play the game?");
  
    if (playGame) {
      var userNumber = prompt("Enter a number between 0 and 10:");
  
      if (isNaN(userNumber)) {
        alert("Sorry, not a number. Goodbye.");
      } else if (userNumber < 0 || userNumber > 10) {
        alert("Sorry, it's not a good number. Goodbye.");
      } else {
        var computerNumber = Math.round(Math.random() * 10);
  
        compareNumbers(userNumber, computerNumber);
      }
    } else {
      alert("No problem, goodbye.");
    }
  }
  
  function compareNumbers(userNumber, computerNumber) {
    if (userNumber == computerNumber) {
      alert("WINNER");
      return;
    } else if (userNumber > computerNumber) {
      alert("Your number is bigger than the computer's. Guess again.");
    } else {
      alert("Your number is smaller than the computer's. Guess again.");
    }
  
    var newNumber = prompt("Enter a new number:");
    compareNumbers(newNumber, computerNumber);
  }
  