# API RESTful de Gerenciamento de Usuários com Flask

## Descrição

Aplicação web simples desenvolvida com **Flask** que implementa uma **API RESTful** para gerenciamento de usuários. Permite realizar operações CRUD (Create, Read, Update, Delete) sobre um recurso de usuário.

Os dados são armazenados temporariamente em memória (lista de dicionários).

---

## Endpoints

| Método | Endpoint         | Descrição                     |
| ------ | ---------------- | ----------------------------- |
| POST   | /users           | Cria um novo usuário          |
| GET    | /users           | Lista todos os usuários       |
| GET    | /users/<id_user> | Retorna um usuário específico |
| PUT    | /users/<id_user> | Atualiza um usuário existente |
| DELETE | /users/<id_user> | Deleta um usuário pelo ID     |

---

## Exemplos de Requisição e Resposta

### Criar Usuário

**POST /users**

```json
{
  "nome": "Bianca Almeida",
  "email": "bianca@example.com"
}
```

**Resposta:**

```json
{
  "mensagem": "Usuario criado com sucesso!",
  "dados_usuario": {
    "id": 0,
    "nome": "Bianca Almeida",
    "email": "bianca@example.com"
  }
}
```

### Listar Usuários

**GET /users**

```json
{
  "usuarios": [
    { "id": 0, "nome": "Bianca Almeida", "email": "bianca@example.com" }
  ],
  "total_usuarios": 1
}
```

### Obter Usuário

**GET /users/0**
**Resposta:**

```json
{
  "mensagem": "Usuário encontrado com sucesso!",
  "dados_usuario": {
    "id": 0,
    "nome": "Bianca Almeida",
    "email": "bianca@example.com"
  }
}
```

### Atualizar Usuário

**PUT /users/0**

```json
{
  "nome": "Bianca A.",
  "email": "bianca.novo@example.com"
}
```

**Resposta:**

```json
{
  "mensagem": "Dados do usuário atualizados com sucesso!"
}
```

### Deletar Usuário

**DELETE /users/0**
**Resposta:**

```json
{
  "mensagem": "Usuário excluído com sucesso"
}
```

---

## Requisitos

- Python 3.x
- Flask

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/biancalmds/EntregaAtividade-Grupo1.git
```

2. Instale o Flask:

```bash
pip install flask
```

3. Execute a aplicação:

```bash
python app.py
```

4. A API estará disponível em: `http://127.0.0.1:5000/`

---

## Observações

- Os dados são armazenados apenas em memória e serão perdidos ao reiniciar a aplicação.
- IDs dos usuários são gerados automaticamente de forma sequencial.
