import React from 'react';
// import logo from './logo.svg';
// import { Counter } from './features/counter/Counter';
import './App.css';

function App() {
  const [todo, setTodo] = React.useState({})

  let data = function() {
    fetch('https://jsonplaceholder.typicode.com/posts')
    .then(response => response.json())
    .then(json => setTodo(json))
  }
  // console.log(typeof JSON.stringify(data))
  // console.log(JSON.stringify(data))
  React.useEffect(() => {
    data()
  }, [])
  return (
    <div>
        {JSON.stringify(todo)}

    </div>
  );
}

export default App;
