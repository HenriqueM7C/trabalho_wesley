#Importa as classes necessárias do módulo Flask para criar uma aplicação web e lidar com solicitações HTTP.
from flask import Flask, request, jsonify
# Criar o objeto Flask app:
app = Flask(__name__)

# Tabela de preços
#criando um dicionário chamado tabela_precos
tabela_precos = {
    1: {"produto": "Sapato", "preco": 99.99},
    2: {"produto": "Bolsa", "preco": 103.89},
    3: {"produto": "Camisa", "preco": 49.98},
    4: {"produto": "Calça", "preco": 89.72},
    5: {"produto": "Blusa", "preco": 97.35},
}

@app.route('/teste/1', methods=['POST'])
#def é uma palavra-chave em Python que é usada para definir uma função.
def consultar_preco():
    try:
        dados_json = request.get_json()

        if 'codigo' in dados_json:
            codigo_produto = int(dados_json['codigo'])

            if codigo_produto in tabela_precos:
                produto = tabela_precos[codigo_produto]['produto']
                preco = tabela_precos[codigo_produto]['preco']

                return jsonify({'produto': produto, 'preco': preco})
            else:
                raise ValueError("Código de produto inválido.")

        else:
            raise ValueError("O código do produto deve ser fornecido no formato JSON.")

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)