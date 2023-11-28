from flask import Flask, request

app = Flask(__name__)

@app.route('/teste/1', methods=['GET' , 'POST'])
def analise_numeros():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        # Obter os três números do formulário
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        num3 = float(request.form.get('num3'))

        # Calcular o menor número
        menor_numero = min(num1, num2, num3)

        # Calcular o maior número
        maior_numero = max(num1, num2, num3)

        # Calcular a média dos números
        media = (num1 + num2 + num3) / 3

        # Retornar os resultados como HTML
        return '''
        <h1>Maior número: {}</h1>
        <h1>Menor número: {}</h1>
        <h1>Média: {}</h1>
        '''.format(maior_numero, menor_numero, media)

    return '''
    <form method="POST" action="/teste/1">
        <div><label>Número 1: <input type="text" name="num1"></label></div>
        <div><label>Número 2: <input type="text" name="num2"></label></div>
        <div><label>Número 3: <input type="text" name="num3"></label></div>
        <input type="submit" value="Enviar">
    </form>
    '''

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)