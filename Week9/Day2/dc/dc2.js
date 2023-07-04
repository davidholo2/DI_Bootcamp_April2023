const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;
  
  // Function 1: toJs
  function toJs() {
    return new Promise((resolve, reject) => {
      try {
        const morseJS = JSON.parse(morse);
        if (Object.keys(morseJS).length === 0) {
          reject("The morse JavaScript object is empty.");
        } else {
          resolve(morseJS);
        }
      } catch (error) {
        reject("Error parsing the morse JSON string.");
      }
    });
  }
  
  // Function 2: toMorse
  function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
      const userInput = prompt("Enter a word or a sentence:");
      if (!userInput) {
        reject("User input is empty.");
      } else {
        const morseTranslation = [];
        for (const char of userInput.toLowerCase()) {
          if (morseJS[char]) {
            morseTranslation.push(morseJS[char]);
          } else {
            reject(`Character "${char}" doesn't exist in the morse JavaScript object.`);
          }
        }
        resolve(morseTranslation);
      }
    });
  }
  
  // Function 3: joinWords
  function joinWords(morseTranslation) {
    const joinedMorse = morseTranslation.join(" ");
    console.log(joinedMorse); 
  }
  
  // Chain the three functions
  toJs()
    .then(morseJS => toMorse(morseJS))
    .then(morseTranslation => joinWords(morseTranslation))
    .catch(error => console.log(error));
  