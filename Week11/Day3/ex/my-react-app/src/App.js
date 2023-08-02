// App.js
import React, { Component } from 'react';
import BuggyCounter from './BuggyCounter';
import ErrorBoundary from './ErrorBoundary';
import Child from './Child';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      show: true,
    };
  }

  handleDeleteClick = () => {
    this.setState({ show: false });
  };

  render() {
    return (
      <div>
        <h1>Exercise 3:</h1>
        {this.state.show && <Child />}
        <button onClick={this.handleDeleteClick}>Delete</button>
      </div>
    );
  }
}

export default App;
