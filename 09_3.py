from flask import Flask, request

app = Flask(__name__)

@app.route('/teste/1', methods=['GET' , 'POST'])
def calcular_imc():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        # Obter os valores de peso e altura do formulário
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))

        # Calcular o IMC
        imc = peso / (altura ** 2)

        # Determinar o grau de obesidade
        grau_obesidade = obter_grau_obesidade(imc)

        # Retornar os resultados formatados em HTML
        resultado = '''
        <h1>IMC: {:.2f}</h1>
        <h1>Grau de Obesidade: {}</h1>
        '''.format(imc, grau_obesidade)

        return resultado

    return '''
    <form method="POST" action="/teste/1">
        <div><label>Peso (kg): <input type="text" name="peso"></label></div>
        <div><label>Altura (m): <input type="text" name="altura"></label></div>
        <input type="submit" value="Calcular IMC">
    </form>
    '''

def obter_grau_obesidade(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug=True, port=5000)