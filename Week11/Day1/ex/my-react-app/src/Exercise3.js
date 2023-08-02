import React from 'react';

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
        {/* Add other HTML tags as required */}
      </div>
    );
  }
}

export default Exercise;
