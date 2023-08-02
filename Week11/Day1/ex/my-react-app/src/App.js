import React from 'react';
import './Exercise.css';

const style_header = {
  color: "white",
  backgroundColor: "DodgerBlue",
  padding: "10px",
  fontFamily: "Arial"
};

class Exercise extends React.Component {
  render() {
    return (
      <div>
        <h1 style={style_header}>Styled Header</h1>
        <p className="para">This is a styled paragraph.</p>

      </div>
    );
  }
}

export default Exercise;
