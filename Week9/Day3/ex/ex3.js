async function fetchStarWarsData() {
    try {
      const response = await fetch("https://www.swapi.tech/api/starships/9/");
  
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      const data = await response.json();
      console.log(data.result);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }
  
  fetchStarWarsData();
  