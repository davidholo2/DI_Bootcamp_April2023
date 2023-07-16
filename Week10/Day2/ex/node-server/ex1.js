const http = require('http');

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/html');

  // First line of HTML
  res.write('<h1>This is my first attempt</h1>');

  // Second line of HTML
  res.write('<h2>This is my second attempt</h2>');

  // Third line of HTML
  res.write('<p>This is my third attempt</p>');

  // End the response
  res.end();
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});
