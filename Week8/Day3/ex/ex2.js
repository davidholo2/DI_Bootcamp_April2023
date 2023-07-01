const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th", "st", "nd", "rd"];

colors.forEach((color, index) => {
  const suffixIndex = (index + 1) % 10;
  const suffix = ordinal[suffixIndex] || ordinal[0];
  console.log(`${index + 1}${suffix} choice is ${color}.`);
});
