from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
#atribuindo o nome do arquivo do banco de dados à variável DATABASE
DATABASE = 'produtos.db'

# Função para conectar ao banco de dados SQLite
def connect_db():
    return sqlite3.connect(DATABASE)

# Criação da tabela 'produtos' se ela não existir
def create_table():
    #gerencia conexão com banco de dados
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                descricao TEXT NOT NULL,
                fornecedor TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER NOT NULL
            );
        ''')
        connection.commit()

# Rota para criar um novo produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    create_table()
    
    dados_produto = request.json
    nome = dados_produto['nome']
    descricao = dados_produto['descricao']
    fornecedor = dados_produto['fornecedor']
    preco = dados_produto['preco']
    quantidade = dados_produto['quantidade']

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO produtos (nome, descricao, fornecedor, preco, quantidade)
            VALUES (?, ?, ?, ?, ?);
        ''', (nome, descricao, fornecedor, preco, quantidade))
        connection.commit()

    return jsonify({'message': 'Produto criado com sucesso!'}), 201

# Rota para obter todos os produtos
@app.route('/produtos', methods=['GET'])
def obter_produtos():
    create_table()

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM produtos;')
        produtos = cursor.fetchall()

    produtos_json = []
    for produto in produtos:
        produto_dict = {
            'id': produto[0],
            'nome': produto[1],
            'descricao': produto[2],
            'fornecedor': produto[3],
            'preco': produto[4],
            'quantidade': produto[5]
        }
        produtos_json.append(produto_dict)

    return jsonify(produtos_json)

# Rota para obter um produto por ID
@app.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    create_table()

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM produtos WHERE id = ?;', (id,))
        produto = cursor.fetchone()

    if produto:
        produto_dict = {
            'id': produto[0],
            'nome': produto[1],
            'descricao': produto[2],
            'fornecedor': produto[3],
            'preco': produto[4],
            'quantidade': produto[5]
        }
        return jsonify(produto_dict)
    else:
        return jsonify({'message': 'Produto não encontrado'}), 404

# Rota para atualizar os dados de um produto por ID
@app.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    create_table()

    dados_atualizados = request.json

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE produtos
            SET nome=?, descricao=?, fornecedor=?, preco=?, quantidade=?
            WHERE id=?;
        ''', (dados_atualizados['nome'], dados_atualizados['descricao'],
              dados_atualizados['fornecedor'], dados_atualizados['preco'],
              dados_atualizados['quantidade'], id))
        connection.commit()

    return jsonify({'message': 'Dados do produto atualizados com sucesso!'})

# Rota para deletar um produto por ID
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    create_table()

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM produtos WHERE id=?;', (id,))
        connection.commit()

    return jsonify({'message': 'Produto deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)

    #"nome": "Produto1",
  #"descricao": "Descrição do Produto1",
  #"fornecedor": "Fornecedor1",
  #"preco": 29.99,
  #"quantidade": 100