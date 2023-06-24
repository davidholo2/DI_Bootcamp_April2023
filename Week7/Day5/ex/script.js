// Step 1: Create the playTheGame() function
function playTheGame() {
    // Step 2: Ask the user if they want to play
    var playGame = confirm("Would you like to play the game?");
  
    if (playGame) {
      // Step 3: Ask the user to enter a number between 0 and 10
      var userNumber = prompt("Enter a number between 0 and 10:");
  
      // Step 4: Check the validity of the user's number
      if (isNaN(userNumber)) {
        alert("Sorry, not a number. Goodbye.");
      } else if (userNumber < 0 || userNumber > 10) {
        alert("Sorry, it's not a good number. Goodbye.");
      } else {
        // Step 5: Generate a random number for the computer
        var computerNumber = Math.round(Math.random() * 10);
  
        // Step 6: Call the compareNumbers() function
        compareNumbers(userNumber, computerNumber);
      }
    } else {
      alert("No problem, goodbye.");
    }
  }
  
  // Step 7: Create the compareNumbers() function
  function compareNumbers(userNumber, computerNumber) {
    // Step 8: Compare the user's number with the computer's number
    if (userNumber == computerNumber) {
      alert("WINNER");
      return;
    } else if (userNumber > computerNumber) {
      alert("Your number is bigger than the computer's. Guess again.");
    } else {
      alert("Your number is smaller than the computer's. Guess again.");
    }
  
    // Step 9: Prompt the user for a new number if they haven't guessed correctly
    var newNumber = prompt("Enter a new number:");
    compareNumbers(newNumber, computerNumber);
  }
  
  // Step 10: Link the JavaScript file to the HTML
  // Open the index.html file and add the following line just before the closing </body> tag:
  // <script src="script.js"></script>
  