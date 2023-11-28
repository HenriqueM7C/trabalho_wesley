from flask import Flask, request

app = Flask(__name__)

# Importar a classe Flask e o objeto request:
from flask import Flask, request, render_template

# Criar o objeto Flask app:
app = Flask(__name__)

# http://127.0.0.1:5000/teste/1
# Aceita requisições com os métodos GET e POST.
# GET: gera um formulário em HTML para o usuário
# enviar dados para o servidor.
# POST: lê os dados enviados pelo usuário através
# do formulário HTML.
@app.route('/teste/1', methods=['GET', 'POST'])
def teste_dados_formulario_html():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        linguagem = request.form.get('linguagem')
        framework = request.form.get('framework')
        # Ou:
        # linguagem = request.form['linguagem']
        # framework = request.form['framework']
        return render_template('resposta.html', linguagem_usr=linguagem,
                               framework_usr=framework)
    # Caso contrário, trata a requisição com método GET:
    return render_template('index.html')

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)