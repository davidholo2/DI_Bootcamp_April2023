// src/components/Counter.js
import React from 'react';
import { connect } from 'react-redux';
import { increaseCount, decreaseCount } from '../actions';

class Counter extends React.Component {
  render() {
    const { count, increaseCount, decreaseCount } = this.props;

    return (
      <div>
        <h1>Counter App with Redux</h1>
        <p>Count: {count}</p>
        <button onClick={increaseCount}>+</button>
        <button onClick={decreaseCount}>-</button>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
    count: state.count,
  };
};

export default connect(mapStateToProps, { increaseCount, decreaseCount })(Counter);
