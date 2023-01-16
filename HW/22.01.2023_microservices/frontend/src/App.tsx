
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
import { useParams } from '@reach/router';
import { render } from '@testing-library/react';
// import { CheckBook } from './components/CheckBook.js';


interface WeatherCardProps {
  // id: number,
  // title: string,
  // description: string,
  // price:number,
  // data:number,
  // in_or_not:boolean,
  // url_img:string
}

const WeatherCard = (props:any) => {
  return (
    <div>
        {props}
    </div>
  )
}

function App() {
  


  const [appState, setAppState] = useState();
  axios.defaults.baseURL = "http://127.0.0.1:8000/api";
  // let state = {
  //   persons: []
  // }
  // async function getOneUser(id: number){
  //   const config = {
  //     url: `/get_book/${id}`,
  //     method: `GET`,
  //     timeout: 5000,

  //     data: {},
  //   };
  //   const response = await axios(config);
  //   // @ts-ignore
  //   console.log(response)
  // }
  const baseURL = 'http://127.0.0.1:8000/api/get_book';

      // useEffect(() => {
        
      //   axios.get(apiUrl).then((resp) => {
      //     const allBooks = resp.data;
      //     setAppState(allBooks);
      //     console.log(allBooks)
      //   });
      // }, [setAppState]);

      // const config = {
      //   url: `/get_book`,
      //   method: `GET`,
      //   timeout: 5000,
      //   data: {},
      // };
      // const response = await axios(config).then(res => {
      //   const persons = res.data;
      //   this.setState({ persons });
      // });

      
      // console.log(response)

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
      

            <Router>
            {/* <header>
              <nav>
                <ul>
                  <li>
                    <Link to="/">Главная</Link>
                  </li>
                  <li>
                    <Link to="/about">Контакты</Link>
                  </li>
                  <li>
                    <Link to="/users">Пользователи</Link>
                  </li>
                </ul>
              </nav>
            </header>      */}

            <main>
              {/* <Switch> рендерит первый <Route>, совпавший с URL */}
                <Routes>
                  <Route path="/" element={
                  
                  <main>
                    <div className="content">
                      {/* <div className="card_book" id=''> */}
                        {/* <img src={img_test} alt="" /> */}
                        {/* <h4 className="title">Подсознание может все</h4> */}
                        {/* <h5 className="description">Книга «Подсознание может всё!» раскрывает глубины человеческого сознания и повествует о неисчерпаемых ресурсах нашего мозга.</h5> */}
                        {/*  */}
                        {/* <h5 className="date_add">Дата публикации: 1997 г.</h5> */}
                        <br />
                        {/* <h5 className="price">Цена: 548 р.</h5> */}
                        {/* <button>Добавить в библиотеку</button> */}
                      {/* </div> */}
                      
                      {posts.map((item,index) =>
                        
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

                      )}
                    </div>
                  </main>
                  
                  
                  } />
                  <Route path="/book/:id" element={
                    <WeatherCard/>
                  }/>
                  
                  <Route path="/about" element={<h1>about</h1>} />
                </Routes>
            </main>
          </Router>
    </section>
  
  );
}
function CheckBook() {

  let { id } = useParams();
  // const baseURL = 'http://127.0.0.1:8000/api/get_book/';
  console.log(id)
  // // const [appState, setAppState] = useState();
  // const [post, setPost] = useState({data:[]});
  // React.useEffect(() => {
  //   axios.get(baseURL).then((response) => {
  //     setPost(response.data);
  //     console.log(response.data)
  //   });
  // }, []);
  
  // if (!post) return null;
  
  // let posts = post.data
  // console.log(posts[0]);

  return (
    <section className="app">
      
    </section>
  
  );
}

export default App;
