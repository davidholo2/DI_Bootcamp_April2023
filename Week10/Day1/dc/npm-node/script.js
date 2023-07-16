// script.js for part2
//const http = require('http');
//const largeNumber = require('./main.js');

//const server = http.createServer((req, res) => {
  //console.log("I'm listening");

  //res.setHeader('Content-Type', 'text/html');

  //const sum = largeNumber + 5;

  //res.end(`<p>My Module is ${sum}</p><h1>Hi there at the frontend</h1>`);
//});

//server.listen(3000, () => {
  //console.log('Server running at http://localhost:3000/');
//});




const http = require('http');
const getCurrentDateTime = require('./main.js');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');
  const currentDateTime = getCurrentDateTime();
  res.end(`<p>${currentDateTime}</p>`);
});

server.listen(8080, () => {
  console.log('Server running at http://localhost:8080/');
});
