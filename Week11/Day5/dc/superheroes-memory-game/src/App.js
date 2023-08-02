import React, { useState } from 'react';
import './App.css';
import { superheroesData } from './superheroesData';
import Card from './Components/Card';

import Navbar from './Components/Navbar';

function App() {
  const [superheroes, setSuperheroes] = useState(superheroesData.superheroes);
  const [score, setScore] = useState(0);
  const [topScore, setTopScore] = useState(0);
  const [clickedIds, setClickedIds] = useState([]);

  const shuffleCards = () => {
    const shuffledSuperheroes = [...superheroes];
    for (let i = shuffledSuperheroes.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffledSuperheroes[i], shuffledSuperheroes[j]] = [
        shuffledSuperheroes[j],
        shuffledSuperheroes[i],
      ];
    }
    setSuperheroes(shuffledSuperheroes);
  };

  const handleClick = (superhero) => {
    if (clickedIds.includes(superhero.id)) {
      // Clicked on the same card twice, reset score and clickedIds
      setScore(0);
      setClickedIds([]);
    } else {
      // Clicked on a new card, update score and clickedIds
      setScore(score + 1);
      setClickedIds([...clickedIds, superhero.id]);
      if (score + 1 > topScore) {
        setTopScore(score + 1);
      }
    }
    shuffleCards();
  };

  return (
    <div className="App">
      <Navbar score={score} topScore={topScore} />
      <div className="card-container">
        {superheroes.map((superhero) => (
          <Card key={superhero.id} superhero={superhero} onClick={handleClick} />
        ))}
      </div>
    </div>
  );
}

export default App;
