// src/reducers/transactionReducer.js

const initialState = {
    currentIndex: -1,
    list: JSON.parse(localStorage.getItem('transactions')) || [],
  };
  
  const transactionReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'INSERT':
        return {
          ...state,
          list: [...state.list, action.payload],
        };
  
      case 'UPDATE':
        state.list[state.currentIndex] = action.payload;
        return { ...state };
  
      case 'UPDATE-INDEX':
        return {
          ...state,
          currentIndex: action.payload,
        };
  
      case 'DELETE':
        state.list.splice(action.payload, 1);
        return { ...state };
  
      default:
        return state;
    }
  };
  
  export default transactionReducer;
  