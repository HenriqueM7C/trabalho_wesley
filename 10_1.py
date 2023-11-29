from flask import Flask, request, jsonify

app = Flask(__name__)

def eh_triangulo(x, y, z):
    if (x + y > z) and (y + z > x) and (z + x > y):
        return True
    else:
        return False

@app.route('/teste/1', methods=['POST'])
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