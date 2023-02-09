import React from 'react';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { store } from './store/store';
import HomePage from './pages/HomePage';
import ToDo from './pages/ToDo';
import { CookiesProvider } from 'react-cookie';
import './index.css';


const container = document.getElementById('root')!;
const root = createRoot(container);

root.render(
    <CookiesProvider>
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
    </CookiesProvider>
);
