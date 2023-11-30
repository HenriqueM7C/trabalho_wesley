from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'alunos.db'

# Função para conectar ao banco de dados SQLite
def connect_db():
    return sqlite3.connect(DATABASE)

# Criação da tabela 'alunos' se ela não existir
def create_table():
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT NOT NULL,
                nome TEXT NOT NULL,
                matricula TEXT NOT NULL,
                endereco TEXT NOT NULL,
                email TEXT NOT NULL,
                celular TEXT NOT NULL,
                nota REAL NOT NULL
            );
        ''')
        connection.commit()

# Rota para criar um novo aluno
@app.route('/alunos', methods=['POST'])
def criar_aluno():
    create_table()
    
    dados_aluno = request.json
    cpf = dados_aluno['cpf']
    nome = dados_aluno['nome']
    matricula = dados_aluno['matricula']
    endereco = dados_aluno['endereco']
    email = dados_aluno['email']
    celular = dados_aluno['celular']
    nota = dados_aluno['nota']

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO alunos (cpf, nome, matricula, endereco, email, celular, nota)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (cpf, nome, matricula, endereco, email, celular, nota))
        connection.commit()

    return jsonify({'message': 'Aluno criado com sucesso!'}), 201

# Rota para obter todos os alunos
@app.route('/alunos', methods=['GET'])
def obter_alunos():
    create_table()

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM alunos;')
        alunos = cursor.fetchall()

    alunos_json = []
    for aluno in alunos:
        aluno_dict = {
            'id': aluno[0],
            'cpf': aluno[1],
            'nome': aluno[2],
            'matricula': aluno[3],
            'endereco': aluno[4],
            'email': aluno[5],
            'celular': aluno[6],
            'nota': aluno[7]
        }
        alunos_json.append(aluno_dict)

    return jsonify(alunos_json)

# Rota para obter um aluno por CPF
@app.route('/alunos/<cpf>', methods=['GET'])
def obter_aluno(cpf):
    create_table()

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM alunos WHERE cpf = ?;', (cpf,))
        aluno = cursor.fetchone()

    if aluno:
        aluno_dict = {
            'id': aluno[0],
            'cpf': aluno[1],
            'nome': aluno[2],
            'matricula': aluno[3],
            'endereco': aluno[4],
            'email': aluno[5],
            'celular': aluno[6],
            'nota': aluno[7]
        }
        return jsonify(aluno_dict)
    else:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# Rota para atualizar os dados de um aluno por CPF
@app.route('/alunos/<cpf>', methods=['PUT'])
def atualizar_aluno(cpf):
    create_table()

    dados_atualizados = request.json

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE alunos
            SET cpf=?, nome=?, matricula=?, endereco=?, email=?, celular=?, nota=?
            WHERE cpf=?;
        ''', (dados_atualizados['cpf'], dados_atualizados['nome'],
              dados_atualizados['matricula'], dados_atualizados['endereco'],
              dados_atualizados['email'], dados_atualizados['celular'],
              dados_atualizados['nota'], cpf))
        connection.commit()

    return jsonify({'message': 'Dados do aluno atualizados com sucesso!'})

# Rota para deletar um aluno por CPF
@app.route('/alunos/<cpf>', methods=['DELETE'])
def deletar_aluno(cpf):
    create_table()

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM alunos WHERE cpf=?;', (cpf,))
        connection.commit()

    return jsonify({'message': 'Aluno deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)