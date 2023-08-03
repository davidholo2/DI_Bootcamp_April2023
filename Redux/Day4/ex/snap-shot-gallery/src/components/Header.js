// src/components/Header.js
import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/category/mountain">Mountain</Link></li>
          <li><Link to="/category/beaches">Beaches</Link></li>
          <li><Link to="/category/birds">Birds</Link></li>
          <li><Link to="/category/food">Food</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
