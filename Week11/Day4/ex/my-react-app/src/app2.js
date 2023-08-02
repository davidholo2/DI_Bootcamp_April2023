import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import PostList from './PostList'; // Import the PostList component

function App() {
  return (
    <div className="container mt-4">
      <PostList /> {/* Render the PostList component */}
    </div>
  );
}

export default App;
