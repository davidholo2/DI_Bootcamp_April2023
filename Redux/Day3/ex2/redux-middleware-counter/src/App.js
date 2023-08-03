// src/App.js
import React from 'react';
import { connect } from 'react-redux';
import { ageUp, ageDown } from './actions';

function App({ age, onAgeUp, onAgeDown }) {
  return (
    <div>
      <h1>Age: {age}</h1>
      <button onClick={onAgeUp}>Age Up</button>
      <button onClick={onAgeDown}>Age Down</button>
    </div>
  );
}

const mapStateToProps = state => {
  return {
    age: state.age,
  };
};

const mapDispatchToProps = dispatch => {
  return {
    onAgeUp: () => dispatch(ageUp()),
    onAgeDown: () => dispatch(ageDown()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(App);
