import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      response: null,
    };
  }

  async postData() {
    const url = 'https://webhook.site/79243ea2-269a-40c3-a60f-199a8d9466c6'; // Replace with your webhook URL
    const data = {
      key1: 'myusername',
      email: 'mymail@gmail.com',
      name: 'Isaac',
      lastname: 'Doe',
      age: 27,
    };

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    };

    try {
      const response = await fetch(url, options);
      const responseData = await response.json();
      this.setState({ response: responseData });
      console.log(responseData);
    } catch (error) {
      console.error('Error:', error);
    }
  }

  render() {
    return (
      <div className="container mt-4">
        <button className="btn btn-primary" onClick={() => this.postData()}>
          Post Data
        </button>
        {this.state.response && (
          <pre>{JSON.stringify(this.state.response, null, 2)}</pre>
        )}
      </div>
    );
  }
}

export default App;
