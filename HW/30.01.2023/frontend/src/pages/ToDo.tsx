import React from 'react';
// import logo from './logo.svg';
// import { Counter } from './features/counter/Counter';
import './../App.css';

function ToDo() {
  return (
    <div className="App">
        <form action={''} method={'POST'}>
            <div className="mb-3">
                <label htmlFor="exampleInputTitle" className="form-label">Введите название задачи</label>
                <input type="text" className="form-control" id="exampleInputTitle" aria-describedby="emailHelp"/>
            </div>
            <button type="submit" className="btn btn-primary w-100">Добавить</button>
        </form>
    </div>

  );
}

export default ToDo;
