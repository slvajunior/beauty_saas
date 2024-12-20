# Beauty SaaS

**Beauty SaaS** é uma plataforma de agendamentos e gerenciamento para salões de beleza e barbearias. O sistema permite que os proprietários de salões gerenciem seus agendamentos e clientes de maneira simples e eficiente, enquanto oferece uma aplicação móvel para os clientes agendarem seus atendimentos.

## Tecnologias Usadas

- **Backend**: Django, Django REST Framework
- **Banco de Dados**: MySQL
- **Hospedagem**: (Inserir detalhes da infraestrutura, como AWS, Heroku, etc.)
- **Outras ferramentas**: Docker, Nginx (se aplicável)

## Funcionalidades

### Para os Salões:
- Cadastro e gerenciamento de salões.
- Gerenciamento de agendamentos.
- Relacionamento com os clientes.
  
### Para os Clientes:
- Agendamento de atendimentos através de um aplicativo dedicado (em breve).

## Estrutura do Projeto

- **backend/**: Código do backend, utilizando Django e Django REST Framework.
  - **clientes/**: App para gerenciar os clientes dos salões.
  - **core/**: App para gerenciar funcionalidades principais do sistema (salões, agendamentos, etc.).
  - **beauty_saas_backend/**: Diretório principal do projeto Django.
- **frontend/**: (Se você decidir criar um frontend para o sistema no futuro)
- **docs/**: Documentação do projeto e instruções de uso.
  
## Instalação

### Pré-requisitos

- Python 3.x
- MySQL (ou outro banco de dados que você esteja utilizando)
- Django 4.x
- Django REST Framework
- Outros pacotes necessários (veja o `requirements.txt`)

### Passos para rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/beauty_saas.git
   cd beauty_saas
