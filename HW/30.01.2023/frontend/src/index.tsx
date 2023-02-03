import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { store } from './app/store';
import HomePage from './pages/HomePage';
import ToDo from './pages/ToDo';

import reportWebVitals from './reportWebVitals';

import './index.css';


const container = document.getElementById('root')!;
const root = createRoot(container);

root.render(
  <React.StrictMode>
    <Provider store={store}>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage />}></Route>
                <Route path="/todo" element={<ToDo />}></Route>
                {/*<Route path="/register" element={<RegisterPage />}></Route>*/}
                {/*<Route path="/http" element={<HttpPage />}></Route>*/}
                {/*<Route path="/todos" element={<TodoList />}></Route>*/}
                {/*<Route path="/todos/:id" element={<TodoDetail />}></Route>*/}
                {/*<Route path="/tasks" element={<TaskListPage />}></Route>*/}
                {/*<Route path="/tasks/:id" element={<TaskPage />}></Route>*/}
            </Routes>
        </BrowserRouter>
    </Provider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
