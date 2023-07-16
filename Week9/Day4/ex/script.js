const charData = {
    'Height': 'height',
    'Gender': 'gender',
    'Birth Year': 'birth_year',
  };
  
  const container = document.getElementById('container');
  const find_button = document.getElementById('find_button');
  find_button.addEventListener('click', find);
  
  // Fetching function
  async function fetchingFunc(url) {
    try {
      const request = await fetch(url);
      if (request.ok) {
        const result = await request.json();
        return result;
      } else {
        throw new Error('Network response was not ok');
      }
    } catch (err) {
      return false;
    }
  }
  
  async function find() {
    // Clear the container
    container.innerHTML = '';
  
    // Show loading animation
    const loadingDiv = document.createElement('div');
    loadingDiv.id = 'loadingDiv';
    const loadingAnimation = document.createElement('i');
    loadingAnimation.classList.add('fa-solid', 'fa-circle-notch', 'fa-spin', 'fa-5x');
    loadingDiv.appendChild(loadingAnimation);
    const loadingText = document.createElement('h1');
    loadingText.textContent = 'Loading...';
    loadingDiv.appendChild(loadingText);
    container.appendChild(loadingDiv);
  
    // Fetch data
    const charNum = Math.floor(Math.random() * 83 + 1);
    const result = await fetchingFunc(`https://www.swapi.tech/api/people/${charNum}`);
  
    if (result) {
      const data = result.result.properties;
      const planetResult = await fetchingFunc(data.homeworld);
  
      // Add name
      const h1 = document.createElement('h1');
      h1.textContent = data.name;
      container.removeChild(loadingDiv);
      container.appendChild(h1);
  
      // Add data
      Object.keys(charData).forEach((element) => {
        const h2 = document.createElement('h2');
        h2.textContent = `${element}: ${data[charData[element]]}`;
        container.appendChild(h2);
      });
  
      // Add homeworld
      const planetName = planetResult.result.properties.name;
      const h2 = document.createElement('h2');
      h2.textContent = `Homeworld: ${planetName}`;
      container.appendChild(h2);
    } else {
      // Display error message
      const h1 = document.createElement('h1');
      h1.textContent = 'Something goes wrong...';
      container.removeChild(loadingDiv);
      container.appendChild(h1);
    }
  }
  