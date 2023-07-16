const userId = "1234";

fetch(`/${userId}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    document.getElementById('user-id').textContent = JSON.stringify(data);
  })
  .catch(error => console.error(error));
