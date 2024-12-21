// src/pages/Login.js
import React, { useState } from 'react';
import { TextField, Button, Grid, Typography } from '@mui/material';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [username, setUsername] = useState('');  // Mudança para 'username' em vez de 'email'
  const [password, setPassword] = useState('');  // 'password' continua
  const [erro, setErro] = useState('');
  const navigate = useNavigate();

  // Função para lidar com o envio do formulário de login
  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/token/', {
        username,  // Usando 'username' ao invés de 'email'
        password,  // Continua usando 'password'
      });

      const { access } = response.data;  // Supondo que o backend retorne um 'access' token
      localStorage.setItem('token', access);  // Salva o token no localStorage
      navigate('/');  // Redireciona para a Dashboard ou página inicial
    } catch (error) {
      setErro('Credenciais inválidas. Tente novamente.');
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <Typography variant="h4" gutterBottom>Login</Typography>
      
      {erro && <p style={{ color: 'red' }}>{erro}</p>}
      
      <form onSubmit={handleLogin}>
        <Grid container spacing={2}>
          <Grid item xs={12}>
            <TextField
              label="Username"  // Mudança do label para 'Username'
              fullWidth
              value={username}  // Usando 'username'
              onChange={(e) => setUsername(e.target.value)}  // Atualizando o 'username'
              required
            />
          </Grid>
          <Grid item xs={12}>
            <TextField
              label="Password"  // 'Password' permanece
              type="password"
              fullWidth
              value={password}  // Usando 'password'
              onChange={(e) => setPassword(e.target.value)}  // Atualizando o 'password'
              required
            />
          </Grid>
          <Grid item xs={12}>
            <Button variant="contained" color="primary" type="submit" fullWidth>
              Entrar
            </Button>
          </Grid>
        </Grid>
      </form>
    </div>
  );
};

export default Login;
