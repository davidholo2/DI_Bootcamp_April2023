// src/middleware/index.js
const logAction = store => next => action => {
    console.log('Dispatching action:', JSON.stringify(action));
    return next(action);
  };
  
  export default logAction;
  