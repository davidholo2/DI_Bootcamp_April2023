function makeAllCaps(words) {
    return new Promise((resolve, reject) => {
      if (Array.isArray(words) && words.every(word => typeof word === "string")) {
        resolve(words.map(word => word.toUpperCase()));
      } else {
        reject("Input should be an array of strings.");
      }
    });
  }
  
  function sortWords(words) {
    return new Promise((resolve, reject) => {
      if (Array.isArray(words) && words.length > 4) {
        resolve(words.sort());
      } else {
        reject("Input array should have more than 4 words.");
      }
    });
  }
  
  
  makeAllCaps([1, "pear", "banana"])
    .then(arr => sortWords(arr))
    .then(result => console.log(result))
    .catch(error => console.log(error));
  
  makeAllCaps(["apple", "pear", "banana"])
    .then(arr => sortWords(arr))
    .then(result => console.log(result))
    .catch(error => console.log(error));
  
  makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
    .then(arr => sortWords(arr))
    .then(result => console.log(result))
    .catch(error => console.log(error));
  