(function(numberOfChildren, partnerName, geographicLocation, jobTitle) {
    const sentence = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;
    document.getElementById("output").textContent = sentence;
  })(2, "John", "New York", "Software Engineer");
  