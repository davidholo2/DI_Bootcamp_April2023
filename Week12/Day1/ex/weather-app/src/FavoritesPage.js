import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import './FavoritesPage.css'; // Import the CSS file

const FavoritesPage = () => {
  const [favorites, setFavorites] = useState([]);
  const [city, setCity] = useState('');

  const addToFavorites = () => {
    if (city.trim() !== '') {
      setFavorites([...favorites, city]);
      setCity('');
    }
  };

  return (
    <div className="favorites-container">
      <h2>Favorites Page</h2>
      <TextField
        label="Enter City"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <Button variant="contained" onClick={addToFavorites}>
        Add to Favorites
      </Button>
      <ul>
        {favorites.map((favCity, index) => (
          <li key={index}>{favCity}</li>
        ))}
      </ul>
    </div>
  );
};

export default FavoritesPage;
