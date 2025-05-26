# 🗓️ API de Reservas

## 📌 Descrição

Esta API é responsável pela criação e listagem de reservas de salas para turmas específicas. Ela valida a existência da turma antes de permitir a reserva e armazena os dados localmente utilizando SQLite. A aplicação foi desenvolvida com Flask e estruturada no padrão MVC, além de estar totalmente conteinerizada via Docker para facilitar a integração em um ambiente de microsserviços.

---

## 🚀 Como Executar com Docker

### Pré-requisitos

- Docker e Docker Compose instalados.
-  Ter a API de turma ativa.

### Passos

1. Clone o repositório:
   ```bash
   git clone https://github.com/genari05/Reserva-de-sala.git

   https://github.com/genari05/Flask.git

---
🌐 Ecossistema de Microsserviços
A **API de Reservas** faz parte de um sistema baseado em microsserviços. Atualmente, ela se integra ao seguinte serviço externo:

🔗 Serviço de Turmas
- **Descrição**: Responsável por fornecer dados das turmas existentes.

- **Integração**: A API de Reservas faz uma requisição GET para validar se a turma informada na reserva existe.

 - **Endpoint consultado:**
  ```
      GET http://localhost:5000/turmas/<turma_id>
```

- Se a turma for válida, a reserva é criada; caso contrário, a requisição retorna erro **400**.

📬 Endpoints
POST **/reserva/**
Cria uma nova reserva.

Corpo esperado (JSON):
  ```
    {
  "turma_id": 1,
  "sala": "B203",
  "data": "2025-06-10",
  "hora_inicio": "08:00",
  "hora_fim": "10:00"
}

```
**Resposta:**
```
{
  "mensagem": "Reserva criada com sucesso"
}
```

GET **/Reserva**
Lista todas as reservas:
Corpo esperado(JSON):
  ```
    {
  "turma_id": 1,
  "sala": "B201",
  "data": "2025-06-10",
  "hora_inicio": "08:00",
  "hora_fim": "10:00"
}

    {
  "turma_id": 2,
  "sala": "B202",
  "data": "2025-06-10",
  "hora_inicio": "08:00",
  "hora_fim": "10:00"
}

    {
  "turma_id": 3,
  "sala": "B203",
  "data": "2025-06-10",
  "hora_inicio": "08:00",
  "hora_fim": "10:00"
}

```

GET **/reserva/validar_turma/<turma_id>**
Verifica se uma turma existe (via serviço externo).

Resposta:

```
{
  "valida": true
}
```

🛠️ Tecnologias Utilizadas
- Python 3.12

- Flask

- SQLite

- Docker / Docker Compose

- Padrão MVC

  🏗️ Arquitetura
A aplicação segue a **arquitetura MVC (Model-View-Controller)**.

Estrutura de Diretórios

```
.
├── client/
|   └── client.py  
├── model/
|   └── reserva_model.py       
├── controller/
|   └── reserva_router.py
├── instance/      
│       └── app.py
├── docker/      
│       └── Dockerfile
│       └── docker-compose.yml
│       └── .dockerignore
│       └── .gitignore                 
├── app.py
├── config.py
├── database.py
├── requirements.txt    
└── README.md                      
```

