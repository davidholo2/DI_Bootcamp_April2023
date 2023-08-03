import React from 'react';
import MovieList from './components/MovieList';
import MovieDetails from './components/MovieDetails';

const App = () => {
  return (
    <div>
      <h1>Movie List</h1>
      <MovieList />
      <h1>Movie Details</h1>
      <MovieDetails />
    </div>
  );
};

export default App;
