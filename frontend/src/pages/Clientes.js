import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Button, TextField, Grid } from '@mui/material';
import { useNavigate } from 'react-router-dom'; // Importando o hook useNavigate

const Clientes = () => {
  const [clientes, setClientes] = useState([]);
  const [nome, setNome] = useState('');
  const [telefone, setTelefone] = useState('');
  const [email, setEmail] = useState('');
  const [editando, setEditando] = useState(null); // Controla se estamos editando um cliente

  const navigate = useNavigate(); // Inicializando o hook useNavigate

  // Função para pegar a lista de clientes da API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/clientes/clientes/')
      .then(response => {
        setClientes(response.data);
      })
      .catch(error => console.error('Erro ao buscar clientes:', error));
  }, []);

  // Função para adicionar um cliente
  const handleAddCliente = () => {
    axios.post('http://127.0.0.1:8000/clientes/clientes/', {
      nome,
      telefone,
      email,
    })
      .then(response => {
        setClientes([...clientes, response.data]);
        resetForm();
      })
      .catch(error => console.error('Erro ao adicionar cliente:', error));
  };

  // Função para editar um cliente
  const handleEditCliente = () => {
    axios.put(`http://127.0.0.1:8000/clientes/clientes/${editando.id}/`, {
      nome,
      telefone,
      email,
    })
      .then(response => {
        setClientes(clientes.map(cliente =>
          cliente.id === editando.id ? response.data : cliente
        ));
        resetForm();
      })
      .catch(error => console.error('Erro ao editar cliente:', error));
  };

  // Função para limpar o formulário e voltar ao estado inicial
  const resetForm = () => {
    setNome('');
    setTelefone('');
    setEmail('');
    setEditando(null);
  };

  // Função para preencher o formulário com os dados do cliente para editar
  const handleEditarClick = (cliente) => {
    setNome(cliente.nome);
    setTelefone(cliente.telefone);
    setEmail(cliente.email);
    setEditando(cliente);
  };

  // Função para deletar um cliente
  const handleDeleteCliente = (id) => {
    axios.delete(`http://127.0.0.1:8000/clientes/clientes/${id}/`)
      .then(() => {
        setClientes(clientes.filter(cliente => cliente.id !== id));
      })
      .catch(error => console.error('Erro ao deletar cliente:', error));
  };

  // Função para retornar ao Dashboard (inicial)
  const handleReturnToDashboard = () => {
    navigate('/'); // Redireciona para a página inicial
  };

  return (
    <div>
      <h1>{editando ? 'Editar Cliente' : 'Gestão de Clientes'}</h1>
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
            label="Telefone"
            value={telefone}
            onChange={(e) => setTelefone(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            label="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={editando ? handleEditCliente : handleAddCliente}
          >
            {editando ? 'Salvar Alterações' : 'Adicionar Cliente'}
          </Button>
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="outlined"
            color="secondary"
            onClick={handleReturnToDashboard}
          >
            Voltar para Dashboard
          </Button>
        </Grid>
      </Grid>

      <h2>Clientes Cadastrados</h2>
      <ul>
        {clientes.map(cliente => (
          <li key={cliente.id}>
            {cliente.nome} - {cliente.telefone}
            <Button
              variant="contained"
              color="secondary"
              onClick={() => handleEditarClick(cliente)}
            >
              Editar
            </Button>
            <Button
              variant="contained"
              color="error"
              onClick={() => handleDeleteCliente(cliente.id)}
            >
              Deletar
            </Button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Clientes;
