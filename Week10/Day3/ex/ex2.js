const fs = require('fs');

fs.writeFile('example.txt', 'Buy milk', (err) => {
  if (err) {
    console.error('Error creating or writing to the file:', err.message);
  } else {
    console.log('File created and text written successfully.');

    fs.appendFile('example.txt', '\nBuy orange juice', (err) => {
      if (err) {
        console.error('Error appending to the file:', err.message);
      } else {
        console.log('Text appended successfully.');
        
        fs.unlink('example.txt', (err) => {
          if (err) {
            console.error('Error deleting the file:', err.message);
          } else {
            console.log('File deleted successfully.');
          }
        });
      }
    });
  }
});
