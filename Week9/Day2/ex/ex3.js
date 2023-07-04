const resolvedPromise = Promise.resolve(3);

resolvedPromise
  .then(result => console.log(result))
  .catch(error => console.log(error));


  
const rejectedPromise = Promise.reject("Boo!");

rejectedPromise
  .then(result => console.log(result))
  .catch(error => console.log(error));
