#Importa as classes necessárias do módulo Flask para criar uma aplicação web e lidar com solicitações HTTP.
from flask import Flask, request, jsonify

#Cria uma instância da aplicação Flask.
app = Flask(__name__)

#recebe três parâmetros (lados de um triângulo) e retorna True se os lados fornecidos podem formar um triângulo e False caso contrário
def eh_triangulo(x, y, z):
    if (x + y > z) and (y + z > x) and (z + x > y):
        return True
    else:
        return False

#Define uma rota chamada /teste/1 que aceita apenas solicitações HTTP POST.
@app.route('/teste/1', methods=['POST'])
#Função associada à rota. Recebe dados JSON contendo os lados do triângulo 
#e retorna se esses lados podem formar um triângulo ou não.
#A função tenta obter os dados JSON da solicitação usando request.get_json().
def verificar_triangulo():
    try:
        dados_json = request.get_json()

        if 'x' in dados_json and 'y' in dados_json and 'z' in dados_json:
            x = float(dados_json['x'])
            y = float(dados_json['y'])
            z = float(dados_json['z'])

            resultado = eh_triangulo(x, y, z)

            return jsonify({'triangulo': resultado})
        else:
            raise ValueError("Os valores X, Y e Z devem ser fornecidos no formato JSON.")

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)