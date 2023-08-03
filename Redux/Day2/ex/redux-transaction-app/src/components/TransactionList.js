// src/components/TransactionList.js

import React from 'react';
import { connect } from 'react-redux';
import { updateIndex, deleteTransaction } from '../actions/transactionActions';

const TransactionList = ({ transactions, updateIndex, deleteTransaction }) => {
  const handleEdit = (index) => {
    updateIndex(index);
  };

  const handleDelete = (index) => {
    deleteTransaction(index);
  };

  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Account Number</th>
            <th>FSC</th>
            <th>Name</th>
            <th>Amount</th>
            <th>Edit</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction, index) => (
            <tr key={index}>
              <td>{transaction.accountNumber}</td>
              <td>{transaction.FSC}</td>
              <td>{transaction.name}</td>
              <td>{transaction.amount}</td>
              <td>
                <button onClick={() => handleEdit(index)}>Edit</button>
              </td>
              <td>
                <button onClick={() => handleDelete(index)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const mapStateToProps = (state) => ({
  transactions: state.list,
});

const mapDispatchToProps = {
  updateIndex,
  deleteTransaction,
};

export default connect(mapStateToProps, mapDispatchToProps)(TransactionList);
