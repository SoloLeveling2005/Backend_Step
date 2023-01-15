import React from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from 'react-router-dom';
import axios from 'axios';
import img_test from './images/test.jpg';


function App() {
  axios.defaults.baseURL = "http://127.0.0.1:8000/api";

  let in_library = "";

  let state = {
        shop: [
            {id: 35, name: 'jumper', color: 'red', price: 20},
            {id: 42, name: 'shirt', color: 'blue', price: 15},
            {id: 56, name: 'pants', color: 'green', price: 25},
            {id: 71, name: 'socks', color: 'black', price: 5},
            {id: 72, name: 'socks', color: 'white', price: 5},
        ]
    }

  return (
    <section className="app">
      <header>
        <div className="content">
          <h1>MyBook</h1>
          <button className="log_in">Войти</button>
        </div>
      </header>
      <main>
        <div className="content">
          <div className="card_book" id=''>
            <img src={img_test} alt="" />
            <h4 className="title">Подсознание может все</h4>
            <h5 className="description">Книга «Подсознание может всё!» раскрывает глубины человеческого сознания и повествует о неисчерпаемых ресурсах нашего мозга.</h5>

            <h5 className="date_add">Дата публикации: 1997 г.</h5>
            {/* <br /> */}
            <h5 className="price">Цена: 548 р.</h5>
            <button>Добавить в библиотеку</button>
          </div>
          {/* {state.shop.map((item, key) =>
            <div>{item.id}</div>
          )} */}
        </div>
      </main>

        {/*     <Router> */}
        {/*     <header> */}
        {/*       <nav> */}
        {/*         <ul> */}
        {/*           <li> */}
        {/*             <Link to="/">Главная</Link> */}
        {/*           </li> */}
        {/*           <li> */}
        {/*             <Link to="/about">Контакты</Link> */}
        {/*           </li> */}
        {/*           <li> */}
        {/*             <Link to="/users">Пользователи</Link> */}
        {/*           </li> */}
        {/*         </ul> */}
        {/*       </nav> */}
        {/*     </header> */}

        {/*     <main> */}
        {/*        */}{/* <Switch> рендерит первый <Route>, совпавший с URL */}
        {/*         <Routes> */}
        {/*           <Route path="/about" element={<h1>about</h1>} /> */}
        {/*           <Route path="/users" element={<h1>users</h1>} /> */}
        {/*           <Route path="/" element={<h1>home</h1>} /> */}
        {/*         </Routes> */}
        {/*     </main> */}
        {/*   </Router> */}
    </section>
  
  );
}

export default App;
