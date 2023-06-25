import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Route, Routes} from 'react-router';
import VacanciesList from "./pages/VacanciesList";
import Vacancy from "./pages/Vacancy";
import VacancyCreate from "./pages/VacancyCreate";

function App() {
  return (
      <Routes>
        <Route path="/" element={<VacanciesList />} />
        <Route path="/vacancy/:id" element={<Vacancy />} />
        <Route path="/create" element={<VacancyCreate />} />
      </Routes>
  );
}

export default App;
