function makeJuice(size) {
    const ingredients = [];
  
    function addIngredients(ingredient1, ingredient2, ingredient3) {
      ingredients.push(ingredient1, ingredient2, ingredient3);
    }
  
    function displayJuice() {
      const sentence = `The client wants a ${size} juice, containing ${ingredients.join(", ")}`;
      document.getElementById("output").textContent = sentence;
    }
  
    addIngredients("apple", "orange", "carrot");
    addIngredients("strawberry", "banana", "spinach");
    displayJuice();
  }
  
  makeJuice("large");


  function makeJuice() {
    const size = document.getElementById("size").value;
    const ingredient1 = document.getElementById("ingredient1").value;
    const ingredient2 = document.getElementById("ingredient2").value;
    const ingredient3 = document.getElementById("ingredient3").value;
  
    const sentence = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}`;
    document.getElementById("output").textContent = sentence;
  }
  
  