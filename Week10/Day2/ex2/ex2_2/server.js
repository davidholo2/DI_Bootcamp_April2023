const express = require('express');
const app = express();
const path = require('path');

app.get('/:id', (req, res) => {
  const idValue = req.params.id;
  res.json({ id: idValue });
});

const port = 3000;
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
