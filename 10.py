# Importar a classe Flask e o objeto request:
from flask import Flask, request

# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/teste/1
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {
# "linguagem" : "Python",
# "framework" : "Flask"
# }
@app.route('/teste/1', methods=['POST'])
def teste_json():
    objeto_json = request.get_json()

    # Verificar se o objeto no formato JSON não é nulo.
    if objeto_json is not None:
        if 'linguagem' in objeto_json:
            linguagem = objeto_json['linguagem']
        if 'framework' in objeto_json:
            framework = objeto_json['framework']

        return '''
        Linguagem informada: {}
        Framework informado: {}
        '''.format(linguagem, framework)

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)