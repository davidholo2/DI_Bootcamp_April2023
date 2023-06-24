// Define an array of planets
const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

// Get the section element
const listPlanetsSection = document.querySelector('.listPlanets');

// Create divs for each planet
planets.forEach((planet, index) => {
  // Create a div for the planet
  const planetDiv = document.createElement('div');
  planetDiv.classList.add('planet', `planet-${index}`);

  // Set a different background color for each planet
  const backgroundColors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white'];
  planetDiv.style.backgroundColor = backgroundColors[index % backgroundColors.length];

  // Create a span for the planet name
  const planetName = document.createElement('span');
  planetName.textContent = planet;

  planetDiv.appendChild(planetName);

  // Append the planet div to the section
  listPlanetsSection.appendChild(planetDiv);

  // Create moons for each planet
  const moons = generateMoons();
  moons.forEach((moon, moonIndex) => {
    // Create a div for the moon
    const moonDiv = document.createElement('div');
    moonDiv.classList.add('moon', `moon-${index}-${moonIndex}`);

    // Set a different position for each moon
    const angle = (moonIndex / moons.length) * 360;
    const distance = 50 + (moonIndex * 20);
    moonDiv.style.transform = `rotate(${angle}deg) translate(${distance}px)`;

    // Append the moon div to the planet div
    planetDiv.appendChild(moonDiv);
  });
});

// Function to generate random number of moons
function generateMoons() {
  const minMoons = 0;
  const maxMoons = 4;
  const numberOfMoons = Math.floor(Math.random() * (maxMoons - minMoons + 1)) + minMoons;

  return Array.from({ length: numberOfMoons });
}
