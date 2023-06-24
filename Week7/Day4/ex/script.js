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


  //ex3
  function changeEnough(itemPrice, amountOfChange) {
    const [quarters, dimes, nickels, pennies] = amountOfChange;
    const totalChange = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01);
  
    return totalChange >= itemPrice;
  }
  
  console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
  console.log(changeEnough(14.11, [2, 100, 0, 0])); // false
  console.log(changeEnough(0.75, [0, 0, 20, 5])); // true

  
  //ex4
  function hotelCost() {
    let numberOfNights;
    while (true) {
      numberOfNights = prompt("Enter the number of nights you would like to stay in the hotel:");
      if (numberOfNights === null) {
        return null; // User canceled
      }
      numberOfNights = Number(numberOfNights);
      if (!isNaN(numberOfNights) && numberOfNights > 0) {
        break;
      }
    }
    return numberOfNights * 140;
  }
  
  function planeRideCost() {
    let destination;
    while (true) {
      destination = prompt("Enter your destination:");
      if (destination === null) {
        return null; // User canceled
      }
      destination = destination.toLowerCase();
      if (destination === "london") {
        return 183;
      } else if (destination === "paris") {
        return 220;
      } else {
        return 300;
      }
    }
  }
  
  function rentalCarCost() {
    let numberOfDays;
    while (true) {
      numberOfDays = prompt("Enter the number of days you would like to rent the car:");
      if (numberOfDays === null) {
        return null; // User canceled
      }
      numberOfDays = Number(numberOfDays);
      if (!isNaN(numberOfDays) && numberOfDays > 0) {
        break;
      }
    }
    let cost = numberOfDays * 40;
    if (numberOfDays > 10) {
      cost *= 0.95; // Apply 5% discount
    }
    return cost;
  }
  
  function totalVacationCost() {
    const hotelCost = hotelCost();
    const planeRideCost = planeRideCost();
    const rentalCarCost = rentalCarCost();
  
    if (hotelCost === null || planeRideCost === null || rentalCarCost === null) {
      return null; // User canceled
    }
  
    const totalCost = hotelCost + planeRideCost + rentalCarCost;
    console.log("The car cost: $" + rentalCarCost + ", the hotel cost: $" + hotelCost + ", the plane tickets cost: $" + planeRideCost);
    return totalCost;
  }
  
  totalVacationCost();

  

  //ex5
const divElement = document.getElementById('container');
console.log(divElement);
const secondListItem = document.querySelector('.list:nth-child(1) li:nth-child(2)');
secondListItem.textContent = 'Richard';
const secondUl = document.querySelector('.list:nth-child(2)');
const secondLiItem = secondUl.querySelector('li:nth-child(2)');
secondUl.removeChild(secondLiItem);
const listItems = document.querySelectorAll('.list li:first-child');
listItems.forEach((item) => {
  item.textContent = 'Your Name';
});

const ulElements = document.querySelectorAll('ul');
ulElements.forEach((ul) => {
  ul.classList.add('student_list');
});

const firstUl = document.querySelector('.list:first-child');
firstUl.classList.add('university', 'attendance');
divElement.style.backgroundColor = 'lightblue';
divElement.style.padding = '10px';
const danLiItem = firstUl.querySelector('li:last-child');
danLiItem.style.display = 'none';
const richardLiItem = secondListItem;
richardLiItem.style.border = '1px solid black';
document.body.style.fontSize = '16px';
const users = Array.from(document.querySelectorAll('.list li')).map(li => li.textContent);
if (divElement.style.backgroundColor === 'lightblue') {
  alert(`Hello ${users.join(' and ')}`);
}


//ex6
const navBarElement = document.getElementById('navBar');
navBarElement.setAttribute('id', 'socialNetworkNavigation');
const newListElement = document.createElement('li');
const logoutText = document.createTextNode('Logout');
newListElement.appendChild(logoutText);
const ulElement = navBarElement.querySelector('ul');
ulElement.appendChild(newListElement);
const firstLi = ulElement.firstElementChild;
const lastLi = ulElement.lastElementChild;
console.log(firstLi.textContent);
console.log(lastLi.textContent);


//ex7
const allBooks = [
    {
      title: 'Harry Potter',
      author: 'J.K. Rowling',
      image: 'https://example.com/harry_potter.jpg',
      alreadyRead: true
    },
    {
      title: 'The Great Gatsby',
      author: 'F. Scott Fitzgerald',
      image: 'https://example.com/great_gatsby.jpg',
      alreadyRead: false
    }
  ];

  const listBooksSection = document.querySelector('.listBooks');
  allBooks.forEach((book) => {
    const bookDiv = document.createElement('div');
    const bookImage = document.createElement('img');
    bookImage.src = book.image;
    bookImage.style.width = '100px';
    bookDiv.appendChild(bookImage);
    const bookDetails = document.createElement('p');
    bookDetails.textContent = `${book.title} written by ${book.author}`;
    if (book.alreadyRead) {
      bookDetails.style.color = 'red';
    }
  
    bookDiv.appendChild(bookDetails);
    listBooksSection.appendChild(bookDiv);
  });
  

  
  