import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import ImageGrid from './components/ImageGrid';
import SearchBar from './components/SearchBar';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Header />
        <Switch>
          <Route path="/" exact component={SearchBar} />
          <Route path="/search/:query" component={ImageGrid} />
          <Route path="/category/:category" component={ImageGrid} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
