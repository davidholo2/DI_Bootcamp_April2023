import React from 'react';

const Todo = ({ todo, toggleTodo, deleteTodo }) => {
  return (
    <div className={`todo ${todo.completed ? 'completed' : ''}`}>
      <span onClick={() => toggleTodo(todo.id)}>{todo.text}</span>
      <button onClick={() => deleteTodo(todo.id)}>Delete</button>
    </div>
  );
};

export default Todo;
