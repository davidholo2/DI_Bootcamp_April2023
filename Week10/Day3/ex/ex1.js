const fs = require('fs');

// Read the text file
fs.readFile('example.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading the file:', err.message);
  } else {
    console.log('File content:');
    console.log(data);
  }
});
