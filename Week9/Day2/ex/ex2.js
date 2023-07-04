function delayedResolve() {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve("success");
      }, 4000);
    });
  }
  
  delayedResolve()
    .then(result => console.log(result))
    .catch(error => console.log(error));
  