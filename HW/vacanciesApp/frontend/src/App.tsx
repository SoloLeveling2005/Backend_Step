import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Route, Routes} from 'react-router';
import VacanciesList from "./pages/VacanciesList";
import Vacancy from "./pages/Vacancy";

function App() {
  return (
      <Routes>
        <Route path="/" element={<VacanciesList />} />
        <Route path="/vacancy/:id" element={<Vacancy />} />
      </Routes>
  );
}

export default App;
