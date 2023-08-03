import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

const Counter = () => {
  const count = useSelector((state) => state.count);
  const dispatch = useDispatch();

  const increment = () => {
    dispatch({ type: 'INCREMENT' });
  };

  const decrement = () => {
    dispatch({ type: 'DECREMENT' });
  };

  const incrementIfOdd = () => {
    if (count % 2 !== 0) {
      increment();
    }
  };

  const incrementWithDelay = () => {
    setTimeout(() => {
      increment();
    }, 1000);
  };

  return (
    <div>
      <h1>Counter App</h1>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
      <button onClick={incrementIfOdd}>Increment If Odd</button>
      <button onClick={incrementWithDelay}>Increment With Delay</button>
    </div>
  );
};

export default Counter;
