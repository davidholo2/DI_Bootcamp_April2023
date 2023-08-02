import React from 'react';
import posts from './posts.json';

function PostList() {
  return (
    <div>
      <h2>Posts List</h2>
      <ul>
        {posts.map(post => (
          <li key={post.id}>
            <h3>{post.title}</h3>
            <p>{post.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostList;
