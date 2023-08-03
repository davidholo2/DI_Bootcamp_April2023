import React from 'react';
import { connect } from 'react-redux';

const MovieDetails = ({ selectedMovie }) => {
  if (!selectedMovie) {
    return <div>Select a movie to see details</div>;
  }

  return (
    <div>
      <h2>{selectedMovie.title}</h2>
      <p>Release Date: {selectedMovie.releaseDate}</p>
      <p>Rating: {selectedMovie.rating}</p>
    </div>
  );
};

const mapStateToProps = state => {
  return { selectedMovie: state.selectedMovie };
};

export default connect(mapStateToProps)(MovieDetails);
