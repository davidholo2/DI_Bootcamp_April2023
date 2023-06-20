const people = ["Greg", "Mary", "Devon", "James"];

// Remove "Greg" from the people array
people.splice(0, 1);

// Replace "James" with "Jason"
const jamesIndex = people.indexOf("James");
if (jamesIndex !== -1) {
  people[jamesIndex] = "Jason";
}

// Add your name to the end of the people array
people.push("david");

// Console.log Mary's index
const maryIndex = people.indexOf("Mary");
console.log("Mary's index:", maryIndex);

// Make a copy of the people array without "Mary" 
const peopleCopy = people.slice(1, 3);

// Check index of "Foo"
const fooIndex = people.indexOf("Foo");
console.log("Index of 'Foo':", fooIndex); // It returns -1 because "Foo" is not present in the array.

// Get the last element of the array
const last = people[people.length - 1];

console.log(people);
console.log(peopleCopy);
console.log("Last element:", last);

//loops
// Iterate through the people array and console.log each person
for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
  }
  
  // Iterate through the people array and exit the loop after console.log "Devon"
  for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
      break;
    }
  }

  
  //ex2
  const colors = ["blue", "red", "green", "yellow", "purple"];
  const suffixes = ["st", "nd", "rd", "th", "th"];
  
  for (let i = 0; i < colors.length; i++) {
    const suffixIndex = i > 2 ? 3 : i; // Determine the correct suffix index
    const choiceString = `My ${i + 1}${suffixes[suffixIndex]} choice is ${colors[i]}`;
    console.log(choiceString);
  }


//ex3
let number;
do {
  number = Number(prompt("Please enter a number:"));
} while (number < 10);

console.log("Number is now greater than or equal to 10.");

//ex4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
      firstFloor: 3,
      secondFloor: 4,
      thirdFloor: 9,
      fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
      sarah: [3, 990],
      dan: [4, 1000],
      david: [1, 500],
    },
  };
  
  // Console.log the number of floors in the building
  console.log("Number of floors:", building.numberOfFloors);
  
  // Console.log how many apartments are on the floors 1 and 3
  console.log("Apartments on the first floor:", building.numberOfAptByFloor.firstFloor);
  console.log("Apartments on the third floor:", building.numberOfAptByFloor.thirdFloor);
  
  // Console.log the name of the second tenant and the number of rooms he has in his apartment
  const secondTenant = building.nameOfTenants[1];
  const numberOfRooms = building.numberOfRoomsAndRent[secondTenant][0];
  console.log("Second tenant:", secondTenant);
  console.log("Number of rooms in his apartment:", numberOfRooms);
  
  // Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent.
  // If it is, then increase Dan’s rent to 1200.
  const sarahRent = building.numberOfRoomsAndRent.sarah[1];
  const davidRent = building.numberOfRoomsAndRent.david[1];
  const danRent = building.numberOfRoomsAndRent.dan[1];
  
  if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
  }
  
  console.log(building.numberOfRoomsAndRent);
  

//ex5
const family = {
    father: "John",
    mother: "Jane",
    son: "Alex",
    daughter: "Emily",
  };
  
  // Console.log the keys of the object
  console.log("Keys of the family object:");
  for (let key in family) {
    console.log(key);
  }
  
  // Console.log the values of the object
  console.log("Values of the family object:");
  for (let key in family) {
    console.log(family[key]);
  }
  
//ex6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  };
  
  let sentence = '';
  
  for (let key in details) {
    sentence += key + ' ' + details[key] + ' ';
  }
  
  console.log(sentence.trim());


  //ex7
  const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const secretSocietyName = names
  .map(name => name[0]) // Extract the first letter of each name
  .sort() // Sort the first letters in alphabetical order
  .join(''); // Concatenate the sorted letters into a single string

console.log(secretSocietyName);


