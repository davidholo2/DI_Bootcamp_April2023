import React from 'react';
import './Navbar.css';

const Navbar = ({ score, topScore }) => {
  return (
    <div className="navbar">
      <div className="score">
        Score: <span>{score}</span>
      </div>
      <div className="top-score">
        Top Score: <span>{topScore}</span>
      </div>
    </div>
  );
};

export default Navbar;
