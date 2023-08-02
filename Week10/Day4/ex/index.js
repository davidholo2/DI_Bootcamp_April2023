const express = require('express');
const bodyParser = require('body-parser');
const bcrypt = require('bcrypt');
const knex = require('knex')({
  client: 'pg',
  connection: {
    host: '127.0.0.1',
    user: 'your_username',
    password: 'your_password',
    database: 'your_database',
  },
});

const app = express();
app.use(bodyParser.json());

app.post('/register', async (req, res) => {
  const { firstName, lastName, email, username, password } = req.body;
  try {
    const hashedPassword = await bcrypt.hash(password, 10);

    await knex('register').insert({
      first_name: firstName,
      last_name: lastName,
      email,
      username,
      password: hashedPassword,
    });

    res.json({ message: 'Registration successful' });
  } catch (error) {
    if (error.code === '23505') {
      res.status(400).json({ message: 'Email already exists' });
    } else {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  }
});

app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  try {
    const user = await knex('register').where({ username }).first();

    if (!user) {
      res.status(404).json({ message: 'User not found' });
    } else {
      const passwordMatch = await bcrypt.compare(password, user.password);

      if (passwordMatch) {
        res.json({ message: 'Login successful' });
      } else {
        res.status(401).json({ message: 'Incorrect password' });
      }
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
