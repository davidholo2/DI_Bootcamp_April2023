const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');

const port = 3000;

// Use body-parser middleware to parse form data
app.use(bodyParser.urlencoded({ extended: false }));

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Route to send the name of one hobby
app.get('/aboutMe/:hobby', (req, res) => {
  const hobby = req.params.hobby;

  // Check if the hobby is a string
  if (typeof hobby !== 'string') {
    res.sendStatus(404);
  } else {
    res.send(`My hobby is ${hobby}`);
  }
});

// Route to display an HTML file with a picture
app.get('/pic', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'picture.html'));
});

// Route to display an HTML form
app.get('/form', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'form.html'));
});

// Route to handle form submission and display the data
app.post('/formData', (req, res) => {
  const email = req.body.email;
  const message = req.body.message;

  res.send(`${email} sent you a message: "${message}"`);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
