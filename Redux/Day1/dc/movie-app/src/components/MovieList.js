import React from 'react';
import { connect } from 'react-redux';
import { selectMovie } from '../actions';

const MovieList = ({ movies, selectMovie }) => {
  const renderList = () => {
    return movies.map(movie => (
      <div key={movie.title}>
        <h2>{movie.title}</h2>
        <button onClick={() => selectMovie(movie)}>Show Details</button>
      </div>
    ));
  };

  return <div>{renderList()}</div>;
};

const mapStateToProps = state => {
  return { movies: state.movies };
};

export default connect(mapStateToProps, { selectMovie })(MovieList);
