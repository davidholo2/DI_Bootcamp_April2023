import React, { Component } from 'react';
import data from './data.json';

class Example1 extends Component {
  render() {
    return (
      <div>
        <h2>Social Media</h2>
        <ul>
          {data.SocialMedias.map((media, index) => (
            <li key={index}>
              <a href={media.link} target="_blank" rel="noopener noreferrer">
                {media.name}
              </a>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default Example1;
