// Child.js
import React, { Component } from 'react';

class Child extends Component {
  componentWillUnmount() {
    console.log('Component is unmounting.');
  }

  render() {
    return <h2>Hello World!</h2>;
  }
}

export default Child;
