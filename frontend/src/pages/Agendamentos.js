import React, { useState, useEffect } from "react";
import axios from "axios";
import { Button, TextField, Grid, MenuItem } from "@mui/material";
import { useNavigate } from "react-router-dom";

const Agendamentos = () => {
  const [agendamentos, setAgendamentos] = useState([]);
  const [clientes, setClientes] = useState([]); // Lista de clientes
  const [clienteId, setClienteId] = useState(""); // Cliente selecionado
  const [servico, setServico] = useState("");
  const [dataHora, setDataHora] = useState("");
  const [confirmado, setConfirmado] = useState(false);
  const [erro, setErro] = useState(null);
  const [token] = useState(localStorage.getItem("token")); // Token armazenado no localStorage

  const navigate = useNavigate();

  // Função para carregar os clientes
  const fetchClientes = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/api/clientes/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setClientes(response.data);
    } catch (error) {
      console.error("Erro ao carregar clientes:", error);
      setErro("Erro ao carregar clientes.");
    }
  };

  // Função para carregar os agendamentos
  const fetchAgendamentos = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api/api/agendamentos/", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setAgendamentos(response.data);
    } catch (error) {
      console.error("Erro ao carregar agendamentos:", error);
      setErro("Erro ao carregar agendamentos.");
    }
  };

  // Carregar dados ao montar o componente
  useEffect(() => {
    fetchClientes();
    fetchAgendamentos();
  }, []);

  // Adicionar um novo agendamento
  const handleAddAgendamento = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/api/agendamentos/",
        {
          cliente: clienteId, // Cliente selecionado pelo ID
          servico,
          data_hora: dataHora,
          confirmado,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      setAgendamentos([...agendamentos, response.data]);
      resetForm();
    } catch (error) {
      console.error("Erro ao adicionar agendamento:", error);
      setErro("Erro ao adicionar agendamento.");
    }
  };

  // Limpar o formulário
  const resetForm = () => {
    setClienteId("");
    setServico("");
    setDataHora("");
    setConfirmado(false);
  };

  // Voltar para a dashboard
  const handleReturnToDashboard = () => {
    navigate("/"); // Redireciona para a página inicial
  };

  return (
    <div>
      <h1>Criar Agendamento</h1>

      <Grid container spacing={2}>
        {/* Seleção de Cliente */}
        <Grid item xs={12} sm={6}>
          <TextField
            select
            label="Cliente"
            value={clienteId}
            onChange={(e) => setClienteId(e.target.value)}
            fullWidth
            error={!clientes.length && !!erro}
            helperText={!clientes.length ? "Nenhum cliente disponível." : ""}
          >
            {clientes.map((cliente) => (
              <MenuItem key={cliente.id} value={cliente.id}>
                {cliente.nome} {/* Verifica o campo 'nome' na resposta */}
              </MenuItem>
            ))}
          </TextField>
        </Grid>

        {/* Serviço */}
        <Grid item xs={12} sm={6}>
          <TextField
            label="Serviço"
            value={servico}
            onChange={(e) => setServico(e.target.value)}
            fullWidth
          />
        </Grid>

        {/* Data e Hora */}
        <Grid item xs={12} sm={6}>
          <TextField
            label="Data e Hora"
            type="datetime-local"
            value={dataHora}
            onChange={(e) => setDataHora(e.target.value)}
            fullWidth
            InputLabelProps={{
              shrink: true,
            }}
          />
        </Grid>

        {/* Confirmado */}
        <Grid item xs={12} sm={6}>
          <label>
            <input
              type="checkbox"
              checked={confirmado}
              onChange={(e) => setConfirmado(e.target.checked)}
            />
            Confirmado
          </label>
        </Grid>

        {/* Botão Adicionar */}
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleAddAgendamento}
          >
            Adicionar Agendamento
          </Button>
        </Grid>

        {/* Botão Voltar */}
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

      {/* Exibição de erros */}
      {erro && <p style={{ color: "red" }}>{erro}</p>}

      <h2>Agendamentos Cadastrados</h2>
      <ul>
        {agendamentos.map((agendamento) => (
          <li key={agendamento.id}>
            {agendamento.servico} - {agendamento.data_hora} - Confirmado:{" "}
            {agendamento.confirmado ? "Sim" : "Não"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Agendamentos;
