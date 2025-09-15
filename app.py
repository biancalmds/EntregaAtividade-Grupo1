from flasgger import Swagger
from flask import Flask, jsonify, request, redirect
app = Flask(__name__)
swagger = Swagger(app, template={
    "info": {
        "title": "API Simples com Flask",
        "description": "Uma API simples para gerenciar usuários, criada com Flask e documentada com Swagger.",
        "version": "1.0.0",
    }})

usuarios = []
usuarios_contador = 0

@app.route("/")
def index():
    return redirect("/apidocs/")

@app.route('/users', methods=['POST'])
def postUsers():
    """
    Cria novo usuário.
    ---
    tags:
      - Usuários
    description: Cria um novo usuário com nome e email.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: user
        description: Objeto JSON com os dados do usuário
        required: true
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
              example: Bianca Almeida
            email:
              type: string
              example: biancalmeida@gmail.com
    responses:
      201:
        description: Usuário criado com sucesso!
        schema:
          type: object
          properties:
            dados_usuario:
              type: object
              properties:
                email:
                  type: string
                  example: biancalmeida@gmail.com
                id:
                  type: integer
                  example: 0
                nome:
                  type: string
                  example: Bianca Almeida
            mensagem: 
              type: string
              example: "Usuario criado com sucesso!"
    """
    global usuarios_contador
    dados = request.get_json()
    novo_usuario = {
        "id": usuarios_contador,
        "nome": dados.get("nome"),
        "email": dados.get("email")
    }
    usuarios.append(novo_usuario)
    usuarios_contador += 1
    return jsonify({"mensagem": "Usuario criado com sucesso!", "dados_usuario": novo_usuario}), 201

@app.route('/users', methods=['GET'])
def getUsers():
    """
    Retorna uma lista de todos os usuário.
    ---
    tags:
      - Usuários
    description: Lista todos os usuários existentes e seus respectivos dados.
    consumes:
      - application/json
    produces:
      - application/json
    responses:
      200:
        description: Lista de usuários retornada com sucesso!
        schema:
          type: object
          properties:
            total_usuarios:
              type: integer
              example: 1
            usuarios:
              type: array
              items:
                type: object
                properties:
                  email:
                    type: string
                    example: felipefernandes@gmail.com
                  id:
                    type: integer
                    example: 0
                  nome: 
                    type: string
                    example: Felipe Fernandes
    """
    return jsonify({"usuarios": usuarios, "total_usuarios": len(usuarios)}), 200
    
@app.route('/users/<int:id_user>', methods=['GET'])
def getUser(id_user):
    """
    Retorna um usuário especificado pelo id.
    ---
    tags:
      - Usuários
    description: Obtém todos os dados de um usuário específico a partir do seu id.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: path
        name: id_user
        type: integer 
        description: id do usuário que será buscado.
        required: true
    responses:
      200:
        description: Usuário encontrado com sucesso!
        schema:
          type: object
          properties:
            dados_usuario:
              type: object
              properties:
                email:
                  type: string
                  example: biancalmeida@gmail.com
                id:
                  type: integer
                  example: 0
                nome:
                  type: string
                  example: Bianca Almeida
            mensagem: 
              type: string
              example: "Usuário encontrado com sucesso!"
      404:
        description: Requisição inválida, usuário não existe.
        schema:
          type: object
          properties:
            mensagem: 
              type: string
              example: "Usuário não encontrado"
    """
    usuario = next((user for user in usuarios if user["id"] == id_user), None)
    if usuario:
        return jsonify({"mensagem": "Usuário encontrado com sucesso!", "dados_usuario": usuario}), 200
    return jsonify({"mensagem": "Usuário não encontrado"}), 404
    
@app.route('/users/<int:id_user>', methods=['PUT'])
def updateUser(id_user):
    """
    Atualiza os dados de um usuário especificado pelo id.
    ---
    tags:
      - Usuários
    description: Altera os dados de um usuário específico a partir do seu id.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: path
        name: id_user
        type: integer 
        description: id do usuário que será buscado.
        required: true
      - in: body
        name: user
        description: Objeto JSON com os dados do usuário a serem atualizados.
        required: true
        schema:
          type: object
          required:
            - nome
            - email
          properties:
            nome:
              type: string
              example: Bianca Almeida
            email:
              type: string
              example: biancalmeida@gmail.com
    responses:
      200:
        description: Dados do usuário atualizados com sucesso!
        schema:
          type: object
          properties:
            mensagem:
              type: string
              example: "Dados do usuário atualizados com sucesso"
      404:
        description: Requisição inválida, usuário não existe para modificar os seus dados.
        schema:
          type: object
          properties:
            mensagem: 
              type: string
              example: "Usuário não encontrado para modificar os seus dados"
    """
    usuario = next((user for user in usuarios if user["id"] == id_user), None)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado para modificar os seus dados"}), 404
    dados = request.get_json()
    usuario['nome'] = dados.get('nome', usuario['nome'])
    usuario['email'] = dados.get('email', usuario['email'])
    return jsonify({"mensagem": "Dados do usuário atualizados com sucesso!"}), 200

@app.route('/users/<int:id_user>', methods=['DELETE'])
def deleteUser(id_user):
    """
    Deleta um usuário especificado pelo id.
    ---
    tags:
      - Usuários
    description: Exclui todos os dados de um usuário específico a partir do seu id.
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: path
        name: id_user
        type: integer 
        description: id do usuário que será excluído.
        required: true
    responses:
      200:
        description: Usuário encontrado e excluído com sucesso!
        schema:
          type: object
          properties:
            mensagem: 
              type: string
              example: "Usuário excluído com sucesso!"
      404:
        description: Requisição inválida, usuário não existe.
        schema:
          type: object
          properties:
            mensagem: 
              type: string
              example: "Usuário não encontrado para deletar os seus dados"
    """
    global usuarios
    usuario = next((user for user in usuarios if user["id"] == id_user), None)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado para deletar os seus dados"}), 404
    usuarios = [user for user in usuarios if user["id"] != id_user]
    return jsonify({"mensagem": "Usuário excluído com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)