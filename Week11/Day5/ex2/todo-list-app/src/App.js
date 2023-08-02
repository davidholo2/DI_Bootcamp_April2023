import React, { useState } from 'react';
import './App.css';
import Todo from './Todo';

function App() {
  const [todos, setTodos] = useState([]);
  const [inputText, setInputText] = useState('');

  const addTodo = () => {
    if (inputText.trim() !== '') {
      const newTodo = {
        id: Date.now(),
        text: inputText,
        completed: false,
      };
      setTodos([...todos, newTodo]);
      setInputText('');
    }
  };

  const toggleTodo = (id) => {
    const updatedTodos = todos.map((todo) =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    );
    setTodos(updatedTodos);
  };

  const deleteTodo = (id) => {
    const updatedTodos = todos.filter((todo) => todo.id !== id);
    setTodos(updatedTodos);
  };

  return (
    <div className="App">
      <h1>Todo List</h1>
      <div>
        <input
          type="text"
          placeholder="Enter your task..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <button onClick={addTodo}>Add</button>
      </div>
      <div className="todo-list">
        {todos.map((todo) => (
          <Todo
            key={todo.id}
            todo={todo}
            toggleTodo={toggleTodo}
            deleteTodo={deleteTodo}
          />
        ))}
      </div>
    </div>
  );
}

export default App;
