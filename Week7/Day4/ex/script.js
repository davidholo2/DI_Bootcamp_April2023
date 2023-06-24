function displayNumbersDivisible(divisor) {
    let sum = 0;
    
    for (let i = 0; i <= 500; i++) {
      if (i % divisor === 0) {
        console.log(i);
        sum += i;
      }
    }
    
    console.log("Sum:", sum);
  }

  displayNumbersDivisible(23);


  //ex2

  const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
  };
  
  const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
  };
  
  const shoppingList = ["banana", "orange", "apple"];
  
  function myBill() {
    let total = 0;
  
    for (let item of shoppingList) {
      if (item in stock && stock[item] > 0) {
        total += prices[item];
        stock[item] -= 1;
      }
    }
  
    return total;
  }
  
  const totalPrice = myBill();
  console.log("Total Price:", totalPrice);
  console.log("Updated Stock:", stock);
  
  