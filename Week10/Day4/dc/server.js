const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use(express.static(__dirname));

app.post('/register', (req, res) => {
    const { firstName, lastName, email, regUsername, regPassword } = req.body;

    const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));

    if (users.some(user => user.username === regUsername || user.password === regPassword)) {
        res.send('error1');
    } else {
        users.push({ firstName, lastName, email, username: regUsername, password: regPassword });
        fs.writeFileSync('users.json', JSON.stringify(users, null, 4), 'utf8');
        res.send('register');
    }
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    const users = JSON.parse(fs.readFileSync('users.json', 'utf8'));

    const user = users.find(user => user.username === username && user.password === password);

    if (user) {
        res.send('login');
    } else {
        res.send('error2');
    }
});

app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});
