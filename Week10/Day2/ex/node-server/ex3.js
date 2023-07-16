const express = require('express');
const app = express();

const htmlLineOfCode = '<h1>This is html tag</h1>';

app.get('/', (req, res) => {
  res.send(htmlLineOfCode);
});

const port = 3000;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
