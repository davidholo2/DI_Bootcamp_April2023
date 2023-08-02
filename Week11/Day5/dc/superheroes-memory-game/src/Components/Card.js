import React from 'react';
import './Card.css';

const Card = ({ superhero, onClick }) => {
  return (
    <div className="card" onClick={() => onClick(superhero)}>
      <img src={superhero.image} alt={superhero.name} />
      <div className="overlay">
        <h3>{superhero.name}</h3>
        <p>{superhero.occupation}</p>
      </div>
    </div>
  );
};

export default Card;
