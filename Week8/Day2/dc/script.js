let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

// Function to display the fruits from the groceries object
const displayGroceries = () => {
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = ""; // Clear the previous content

  groceries.fruits.forEach((fruit) => {
    const fruitElement = document.createElement("p");
    fruitElement.textContent = fruit;
    outputDiv.appendChild(fruitElement);
  });
};

// Arrow function to clone groceries object and modify variables
const cloneGroceries = () => {
  let user = client; // Copying the value of client to user

  client = "Betty"; // Modifying the value of client

  let shopping = JSON.parse(JSON.stringify(groceries)); // Cloning the groceries object

  shopping.totalPrice = "35$"; // Modifying the totalPrice key in shopping object
  shopping.other.paid = false; // Modifying the paid key in shopping object

  console.log(user); // Output: John
  console.log(shopping); // Output: Modified shopping object
};
