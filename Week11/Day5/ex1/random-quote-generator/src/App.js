import React, { Component } from 'react';
import './App.css';
import quotesData from './quotesData';



class QuoteGenerator extends Component {
  constructor(props) {
    super(props);
    this.state = {
      quoteIndex: this.getRandomIndex(),
      bgColor: this.getRandomColor(),
      textColor: this.getRandomColor(),
    };
  }

  getRandomIndex = () => Math.floor(Math.random() * quotesData.length);

  getRandomColor = () => '#' + Math.floor(Math.random() * 16777215).toString(16);

  generateRandomQuote = () => {
    let newIndex;
    do {
      newIndex = this.getRandomIndex();
    } while (newIndex === this.state.quoteIndex);

    this.setState({
      quoteIndex: newIndex,
      bgColor: this.getRandomColor(),
      textColor: this.getRandomColor(),
    });
  };

  render() {
    const { quoteIndex, bgColor, textColor } = this.state;
    const { quote, author } = quotesData[quoteIndex];

    const quoteStyle = {
      color: textColor,
    };

    const boxStyle = {
      backgroundColor: bgColor,
    };

    return (
      <div className="quote-box" style={boxStyle}>
        <h1 className="quote" style={quoteStyle}>
          {quote}
        </h1>
        <p className="author">{author}</p>
        <button className="new-quote-btn" style={quoteStyle} onClick={this.generateRandomQuote}>
          New Quote
        </button>
      </div>
    );
  }
}

export default QuoteGenerator;