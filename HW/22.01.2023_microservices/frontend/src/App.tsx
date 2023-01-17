
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,useSearchParams,
} from 'react-router-dom';
import axios from 'axios';
import img_test from './images/test.jpg';
import React, { useEffect, useState } from 'react';
import { render } from '@testing-library/react';
// import { CheckBook } from './components/CheckBook.js';
import { useParams } from "react-router-dom"
import { Template } from 'webpack';


var baseURL = 'http://127.0.0.1:8000/api/get_book';
axios.defaults.baseURL = "http://127.0.0.1:8000/api";
function App() {
  


  const [appState, setAppState] = useState();


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
      
      

            <Router>



                <Routes>
                  <Route path="/" element={
                  <div>
                  <header>
                  <div className="content">
                    <h1 className='title_page'>MyBook</h1>
                    <button className="log_in">Войти</button>
                  </div>
                  </header>
                  <main>
                    <div className="content">
                      <br />
                      
                      {posts.map((item,index) =>
                        <Link to={"/book/"+item[0]} className='linkToBook'>
                          <div className="card_book" id={item[0]} key={item[0]}>
                            {/* {item[]} */}
                            {/* <img src={require(item[index][6]).default} /> */}
                            {/* {require(item[index][6])} */}
                            <img src={"./"+item[6]} alt="" />
                            <h4 className="title">{item[1]}</h4>
                            <h5 className="description">{item[2]}</h5>

                            <h5 className="date_add">Дата публикации: {item[4]} г.</h5>
                            {/* <br /> */}
                            <h5 className="price">Цена: {item[3]}</h5>
                            <button>Добавить в библиотеку</button>
                          </div>
                        </Link>
                      )}
                    </div>
                  </main>
                  </div>
                  
                  
                  } />
                  <Route path="/book/:id" element={<CheckBook />} />

                </Routes>
          </Router>
    </section>
  
  );
}
function CheckBook() {




  
  const { id } = useParams()
  console.log(id)
  let URL = baseURL+"/"+id
  const [appState, setAppState] = useState();
  const [post, setPost] = useState({data:[]});
    React.useEffect(() => {
      axios.get(URL).then((response) => {
        setPost(response.data);
        console.log(response.data)
      });
    }, []);
    
    if (!post) return null;
    
    let post_one = post.data
    console.log('post_one',post_one);
  return (  
    <div>
      <header>
        <div className="content">
          <Link to="/" className=''><h1 className=''>MyBook</h1></Link>
          <button className="log_in">Войти</button>
        </div>
      </header>
      <main>
      
        
        {post_one.map((data) => (
          <div className="content info">
            <img src={"../"+data[6]} alt="" />
            <div className='content'>
              <h1>{data[1]}</h1>
              <h4>{data[2]}</h4>
              <h4 className="date_add">Дата публикации: {data[4]} г.</h4>
              <h4 className="price">Цена: {data[3]}</h4>
              <button>Добавить в библиотеку</button>
            </div>
          </div> 
        ))}
       
      </main>
    </div>
    
  )
}

export default App;
