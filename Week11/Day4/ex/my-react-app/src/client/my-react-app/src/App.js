import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = {
    message: '',
  };

  componentDidMount() {
    this.fetchMessage();
  }

  fetchMessage = async () => {
    try {
      const response = await fetch('/api/hello');
      const data = await response.text();
      this.setState({ message: data });
    } catch (error) {
      console.error('Error fetching message:', error);
    }
  };

  handleSubmit = async (event) => {
    event.preventDefault();
    const inputValue = event.target.input.value;

    try {
      const response = await fetch('/api/world', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: inputValue }),
      });
      const data = await response.text();
      console.log('Response from server:', data);
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  render() {
    return (
      <div className="App">
        <h1>{this.state.message}</h1>
        <form onSubmit={this.handleSubmit}>
          <input type="text" name="input" placeholder="Type something" />
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default App;
