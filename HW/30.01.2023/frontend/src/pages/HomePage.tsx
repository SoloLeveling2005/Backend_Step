import React from 'react';
import { Link } from 'react-router-dom';
// import logo from './logo.svg';
// import { Counter } from './features/counter/Counter';
import './../App.css';

function HomePage() {
  return (
    <div className="App">
        <header className="header d-flex justify-content-center py-3">
            <ul className="nav nav-pills">
                <li className="nav-item"><a href="#" className="nav-link active" aria-current="page">Home</a></li>
                {/*<li className="nav-item"><a href="#" className="nav-link">ToDo</a></li>*/}
                {/* eslint-disable-next-line react/jsx-no-undef */}
                <Link to={`/todo`}>
                    <li className="nav-item"><a href="#" className="nav-link">ToDo</a></li>
                </Link>
            </ul>
        </header>
        <div className="container">
        </div>
        <div className={'content'}>
            <h1>Очень информативный контент</h1>
        </div>
    </div>

  );
}

export default HomePage;
