// src/ParentComponent.js

import React from 'react';
import Card from './Card';

const ParentComponent = () => {
  return (
    <div className="parent">
      <Card icon="💼" label="Total Orders" number={256} />
      <Card icon="🛒" label="Items Sold" number={1243} />
      <Card icon="💰" label="Revenue" number={58900} />
    </div>
  );
};

export default ParentComponent;
