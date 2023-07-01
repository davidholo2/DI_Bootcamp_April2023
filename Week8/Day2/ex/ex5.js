function convertToGramsDeclaration(weightInKg) {
    return weightInKg * 1000;
  }
  
  const convertToGramsExpression = function(weightInKg) {
    return weightInKg * 1000;
  };
  
  console.log(convertToGramsDeclaration(2));
  console.log(convertToGramsExpression(3));
  
  const convertToGramsArrow = weightInKg => weightInKg * 1000;
  
  console.log(convertToGramsArrow(4));
  
