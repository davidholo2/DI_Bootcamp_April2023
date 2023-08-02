import React, { Component } from 'react';
import data from './data.json';

class Example3 extends Component {
  render() {
    return (
      <div>
        <h2>Experiences</h2>
        <div>
          {data.Experiences.map(experience => (
            <div key={experience.id}>
              <h3>{experience.title}</h3>
              <p>Years of experience: {experience.years}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
}

export default Example3;
