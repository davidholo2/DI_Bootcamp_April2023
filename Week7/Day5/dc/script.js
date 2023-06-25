function bottlesOfBeer() {
    var bottles = parseInt(prompt("Enter the number of bottles to start the song:"));
  
    for (var i = bottles; i > 0; i--) {
      console.log(`${i} ${bottleText(i)} of beer on the wall`);
      console.log(`${i} ${bottleText(i)} of beer`);
      console.log(`Take ${takeText(i)} down, pass ${passText(i)} around`);
      console.log(`${nextBottleText(i)} ${bottleText(nextBottle(i))} of beer on the wall`);
      console.log();
    }
  
    console.log(`${noBottleText()} of beer on the wall`);
  
    function bottleText(count) {
      if (count === 1) {
        return "bottle";
      } else {
        return "bottles";
      }
    }
  
    function takeText(count) {
      if (count === 1) {
        return "it";
      } else {
        return count;
      }
    }
  
    function passText(count) {
      if (count === 1) {
        return "it";
      } else {
        return "them";
      }
    }
  
    function nextBottle(count) {
      if (count === 1) {
        return "no";
      } else {
        return count - 1;
      }
    }
  
    function nextBottleText(count) {
      if (count === 2) {
        return "1";
      } else {
        return nextBottle(count);
      }
    }
  
    function noBottleText() {
      return "No more bottles";
    }
  }
  
  bottlesOfBeer();
  