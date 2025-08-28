from flask import Flask, jsonify, request
app = Flask(__name__)

usuarios = []
usuarios_contador = 0

@app.route('/users', methods=['POST'])
def postUsers():
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
        return jsonify({"usuarios": usuarios, "total_usuarios": len(usuarios)}), 200
    
@app.route('/users/<int:id_user>', methods=['GET'])
def getUser(id_user):
    usuario = next((user for user in usuarios if user["id"] == id_user), None)
    if usuario:
        return jsonify({"mensagem": "Usuário encontrado com sucesso!", "dados_usuario": usuario}), 200
    return jsonify({"mensagem": "Usuário não encontrado"}), 404
    
@app.route('/users/<int:id_user>', methods=['PUT'])
def updateUser(id_user):
    usuario = next((user for user in usuarios if user["id"] == id_user), None)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404
    dados = request.get_json()
    usuario['nome'] = dados.get('nome', usuario['nome'])
    usuario['email'] = dados.get('email', usuario['email'])
    return jsonify({"mensagem": "Dados do usuário atualizados com sucesso!"})

@app.route('/users/<int:id_user>', methods=['DELETE'])
def deleteUser(id_user):
    global usuarios
    usuario = next((user for user in usuarios if user["id"] == id_user), None)
    if not usuario:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404
    usuarios = [user for user in usuarios if user["id"] != id_user]
    return jsonify({"mensagem": "Usuário excluído com sucesso"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)