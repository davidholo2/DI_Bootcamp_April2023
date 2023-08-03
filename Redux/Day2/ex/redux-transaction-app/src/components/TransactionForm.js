// src/components/TransactionForm.js

import React, { useState } from 'react';
import { connect } from 'react-redux';
import { insertTransaction, updateTransaction, updateIndex } from '../actions/transactionActions';

const TransactionForm = ({ currentIndex, insertTransaction, updateTransaction, updateIndex }) => {
  const [state, setState] = useState({
    accountNumber: '',
    FSC: '',
    name: '',
    amount: '',
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setState((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (currentIndex === -1) {
      insertTransaction(state);
    } else {
      updateTransaction(state);
      updateIndex(-1);
    }
    setState({
      accountNumber: '',
      FSC: '',
      name: '',
      amount: '',
    });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" name="accountNumber" value={state.accountNumber} onChange={handleInputChange} placeholder="Account Number" />
        <input type="text" name="FSC" value={state.FSC} onChange={handleInputChange} placeholder="FSC" />
        <input type="text" name="name" value={state.name} onChange={handleInputChange} placeholder="Name" />
        <input type="text" name="amount" value={state.amount} onChange={handleInputChange} placeholder="Amount" />
        <button type="submit">{currentIndex === -1 ? 'Add' : 'Update'}</button>
      </form>
    </div>
  );
};

const mapStateToProps = (state) => ({
  currentIndex: state.currentIndex,
});

const mapDispatchToProps = {
  insertTransaction,
  updateTransaction,
  updateIndex,
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionForm);
