document.addEventListener('DOMContentLoaded', () => {
    const regButton = document.getElementById('registerButton');
    const regForm = document.getElementById('registerForm');
    const regMessage = document.getElementById('registerMessage');

    const loginForm = document.getElementById('loginForm');
    const loginMessage = document.getElementById('loginMessage');

    regForm.addEventListener('input', () => {
        const inputs = Array.from(regForm.getElementsByTagName('input'));
        const isAnyInputEmpty = inputs.some(input => input.value === '');
        regButton.disabled = isAnyInputEmpty;
    });

    regForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(regForm);
        const response = await fetch('/register', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const result = await response.text();
        regMessage.textContent = result === 'register' ? 'Registration successful.' : 'Username or password already exist.';
    });

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(loginForm);
        const response = await fetch('/login', {
            method: 'POST',
            body: JSON.stringify(Object.fromEntries(formData)),
            headers: {
                'Content-Type': 'application/json'
            }
        });

        const result = await response.text();
        loginMessage.textContent = result === 'login' ? 'Login successful.' : 'Invalid username or password.';
    });
});
