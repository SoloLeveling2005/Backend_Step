
// import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  // useRouteMatch,
} from 'react-router-dom';
import axios from 'axios';
import img_test from './images/test.jpg';
import React, { useEffect, useState } from 'react';
import { useParams } from '@reach/router';
// import { CheckBook } from './components/CheckBook.js';



function CheckBook() {
  let { IdBook } = useParams();
  const baseURL = 'http://127.0.0.1:8000/api/get_book/';
  console.log(IdBook)
  // const [appState, setAppState] = useState();
  const [post, setPost] = useState({data:[]});
  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setPost(response.data);
      console.log(response.data)
    });
  }, []);
  
  if (!post) return null;
  
  let posts = post.data
  console.log(posts[0]);

  return (
    <section className="app">
      <header>
        <div className="content">
          <h1>MyBook</h1>
          <button className="log_in">Войти</button>
        </div>
      </header>
      
    </section>
  
  );
}

export default CheckBook;
