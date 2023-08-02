// ErrorBoundary.js
import React, { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      errorInfo: null,
    };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo,
    });
  }

  render() {
    if (this.state.errorInfo) {
      return (
        <details style={{ whiteSpace: 'pre-wrap' }}>
          <summary>Error</summary>
          <div>
            {this.state.error && this.state.error.toString()}
          </div>
          <br />
          <div>
            {this.state.errorInfo.componentStack}
          </div>
        </details>
      );
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
