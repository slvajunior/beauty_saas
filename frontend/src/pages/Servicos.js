// src/pages/Servicos.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, TextField, Grid } from '@mui/material';

const Servicos = () => {
  const [servicos, setServicos] = useState([]);
  const [nome, setNome] = useState('');
  const [descricao, setDescricao] = useState('');
  const [preco, setPreco] = useState('');

  // Função para pegar a lista de serviços da API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/servicos/servicos/')
      .then(response => {
        setServicos(response.data);
      })
      .catch(error => console.error('Erro ao buscar serviços:', error));
  }, []);

  const handleAddServico = () => {
    axios.post('http://127.0.0.1:8000/servicos/servicos/', {
      nome,
      descricao,
      preco,
    })
      .then(response => {
        setServicos([...servicos, response.data]);
      })
      .catch(error => console.error('Erro ao adicionar serviço:', error));
  };

  return (
    <div>
      <h1>Gestão de Serviços</h1>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <TextField
            label="Nome"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            label="Descrição"
            value={descricao}
            onChange={(e) => setDescricao(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            label="Preço"
            value={preco}
            onChange={(e) => setPreco(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleAddServico}
          >
            Adicionar Serviço
          </Button>
        </Grid>
      </Grid>

      <h2>Serviços Cadastrados</h2>
      <ul>
        {servicos.map(servico => (
          <li key={servico.id}>{servico.nome} - {servico.preco}</li>
        ))}
      </ul>
    </div>
  );
};

export default Servicos;
