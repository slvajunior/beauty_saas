// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Agendamentos from './pages/Agendamentos';
import Clientes from './pages/Clientes';
import Servicos from './pages/Servicos';
import Saloes from './pages/Saloes';
import Login from './pages/Login'; // Importando a página de login
import './styles/App.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/agendamentos" element={<Agendamentos />} />
        <Route path="/clientes" element={<Clientes />} />
        <Route path="/servicos" element={<Servicos />} />
        <Route path="/saloes" element={<Saloes />} />
        <Route path="/login" element={<Login />} /> {/* Rota de Login */}
      </Routes>
    </Router>
  );
}

export default App;
