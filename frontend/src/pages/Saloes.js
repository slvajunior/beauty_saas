// src/pages/Saloes.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Saloes = () => {
  const [saloes, setSaloes] = useState([]);

  // Função para pegar a lista de salões da API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/saloes/saloes/')
      .then(response => {
        setSaloes(response.data);
      })
      .catch(error => console.error('Erro ao buscar salões:', error));
  }, []);

  return (
    <div>
      <h1>Gestão de Salões</h1>
      <h2>Salões Cadastrados</h2>
      <ul>
        {saloes.map(salao => (
          <li key={salao.id}>{salao.nome} - {salao.endereco}</li>
        ))}
      </ul>
    </div>
  );
};

export default Saloes;
