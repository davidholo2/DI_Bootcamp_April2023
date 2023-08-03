// src/App.js

import React from 'react';
import './App.css';
import TransactionForm from './components/TransactionForm';
import TransactionList from './components/TransactionList';

function App() {
  return (
    <div className="App">
      <h1>Redux Transaction App</h1>
      <TransactionForm />
      <TransactionList />
    </div>
  );
}

export default App;
