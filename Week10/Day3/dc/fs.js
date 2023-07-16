const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'RightLeft.txt');

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err.message);
  } else {
    let position = 0;
    let stepsToMinusOne = -1;

    for (let symbol of data) {
      if (symbol === '>') {
        position++;
      } else if (symbol === '<') {
        position--;
        if (stepsToMinusOne === -1 && position === -1) {
          stepsToMinusOne = position;
        }
      }
    }

    console.log(`Final position: ${position} steps to the right.`);
    console.log(`Steps to reach position -1: ${Math.abs(stepsToMinusOne)} steps.`);
  }
});
