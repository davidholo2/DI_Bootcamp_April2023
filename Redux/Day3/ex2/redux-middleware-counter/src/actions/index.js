// src/actions/index.js
export const AGE_UP = 'AGE_UP';
export const AGE_DOWN = 'AGE_DOWN';

export const ageUp = () => {
  return {
    type: AGE_UP,
  };
};

export const ageDown = () => {
  return {
    type: AGE_DOWN,
  };
};
