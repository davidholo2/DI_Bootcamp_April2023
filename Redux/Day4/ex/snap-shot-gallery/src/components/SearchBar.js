import React, { useState } from 'react';
import { useHistory } from 'react-router-dom'; // Correct import for useHistory

const SearchBar = () => {
  const [query, setQuery] = useState('');
  const history = useHistory(); // Correctly using useHistory

  const handleSubmit = (e) => {
    e.preventDefault();
    history.push(`/search/${query}`);
  };

  return (
    <div className="search-bar">
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Search for images..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>
    </div>
  );
};

export default SearchBar;
