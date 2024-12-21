// src/pages/Dashboard.js
import React from 'react';

function Dashboard() {
  return (
    <div className="dashboard-container">
      <h1>Dashboard</h1>
      <p>Bem-vindo ao painel administrativo! Aqui você pode ver um resumo das operações.</p>
      <div className="nav-buttons">
        <a href="/agendamentos" className="nav-button">Agendamentos</a>
        <a href="/clientes" className="nav-button">Clientes</a>
        <a href="/servicos" className="nav-button">Serviços</a>
        <a href="/saloes" className="nav-button">Salões</a>
      </div>
    </div>
  );
}

export default Dashboard;
