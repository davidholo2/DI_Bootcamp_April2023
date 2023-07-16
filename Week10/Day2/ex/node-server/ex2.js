const http = require('http');

const user = {
  firstname: 'John',
  lastname: 'Doe'
};

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');
  
  // Convert the user object to JSON
  const jsonUser = JSON.stringify(user);

  // Send the JSON response
  res.end(jsonUser);
});

server.listen(8080, () => {
  console.log('Server running at http://localhost:8080/');
});
