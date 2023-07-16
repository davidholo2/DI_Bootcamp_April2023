fetch('/users')
  .then(response => response.json())
  .then(data => {
    console.log(data); // Log the response to the console
    document.getElementById('user-data').textContent = JSON.stringify(data);
  })
  .catch(error => console.error(error));
