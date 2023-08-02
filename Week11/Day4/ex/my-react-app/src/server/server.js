// server/server.js
const express = require('express');
const app = express();
const PORT = 5000;

app.get('/api/hello', (req, res) => {
  res.send('Hello From Express');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

const bodyParser = require('body-parser');
app.use(bodyParser.json());

app.post('/api/world', (req, res) => {
  const inputValue = req.body.input;
  console.log('Received POST request:', inputValue);
  const responseMessage = `I received your POST request. This is what you sent me: ${inputValue}`;
  res.send(responseMessage);
});