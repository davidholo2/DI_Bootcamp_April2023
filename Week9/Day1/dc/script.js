function handleSubmit(event) {
    event.preventDefault();
  
    const name = document.getElementById('name').value;
    const lastName = document.getElementById('last-name').value;
  
    const jsonString = `{"name": "${name}", "lastName": "${lastName}"}`;
  
    const outputDiv = document.getElementById('output');
    outputDiv.textContent = jsonString;
  }
  