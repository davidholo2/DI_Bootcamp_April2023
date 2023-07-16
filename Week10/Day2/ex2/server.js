const express = require('express');
const app = express();
const path = require('path');

const user = {
  firstname: 'John',
  lastname: 'Doe'
};

// Serve static files from the public directory
app.use(express.static(path.join(__dirname, 'public')));

app.get('/users', (req, res) => {
  res.json(user);
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
