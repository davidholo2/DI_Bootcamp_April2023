// Function to get the current date and time
const getCurrentDateTime = () => {
    const now = new Date();
    return now.toUTCString();
  };
  
  module.exports = getCurrentDateTime;
  