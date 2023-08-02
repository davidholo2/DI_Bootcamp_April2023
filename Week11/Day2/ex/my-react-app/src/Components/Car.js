
import React from 'react';

const Car = ({ carInfo, color }) => {
  return (
    <div>
      <h2>This car is {color} {carInfo.model}</h2>
    </div>
  );
};

export default Car;
