from flask import Flask, render_template, request, redirect
import requests
from tkinter import messagebox

app = Flask(__name__)


url_pessoas = 'https://api-usuarios-tvdy.onrender.com/pessoas'
# URL da API para login
url_login = 'https://api-usuarios-tvdy.onrender.com/login'
url_cadastrar = 'https://api-usuarios-tvdy.onrender.com/pessoas'


@app.route('/')
def index():
    # Obtenha o email do parâmetro na URL
    email = request.args.get('email')
    dados_usuario = None
    nome = "Recrutador"
    
    # Se o email estiver presente, faça a solicitação à API para obter dados do usuário, se necessário
    if email:
        urlEmail = f'https://api-usuarios-tvdy.onrender.com/pessoas/email/{email}'
        resposta = requests.get(urlEmail)

        if resposta.status_code == 200:
            # Aqui você pode usar os dados do usuário obtidos da API
            dados_usuario = resposta.json()
            nome = (dados_usuario['pessoa']['nome'])

            # ...
    
    # Restante do código da rota /index
    
    saldaçao = f"Olá, {nome}! Guilherme aqui"
    print(saldaçao)
    
    return render_template('index.html', nome=saldaçao)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fazer-login', methods=['POST'])
def fazer_login():
    # Obter os valores do formulário
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Dados de login em formato JSON
    dados_login = {'email': email, 'senha': senha}

    # Fazendo a requisição POST para o endpoint de login com os dados em JSON
    resposta = requests.post(url_login, json=dados_login, verify=True)  # O parâmetro 'verify=True' verifica o certificado SSL

    # Verificando o status da resposta
    if resposta.status_code == 200:
        # Redirecionar para a página principal ou outra página após o login bem-sucedido
        return redirect(f'/?email={email}')
    else:
        return f"Falha no login. Código de status: {resposta.status_code}"
    

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    try:
        # Obter os valores do formulário
        nome = request.form.get('nome')
        email = request.form.get('email')
        idade = request.form.get('idade')
        senha = request.form.get('senha')

        # Verificar se o e-mail já existe
        url_verificar_email = f'https://api-usuarios-tvdy.onrender.com/pessoas/email/{email}'
        resposta_verificacao = requests.get(url_verificar_email)

        if resposta_verificacao.status_code == 200:
            # Se o e-mail já existe, informe ao usuário
            return "E-mail já cadastrado. Escolha outro e-mail."

        # Dados de cadastro em formato JSON
        dados_cadastro = {'nome': nome, 'email': email, 'idade': idade, 'senha': senha}

        # Fazendo a requisição POST para o endpoint de cadastro com os dados em JSON
        resposta = requests.post(url_pessoas, json=dados_cadastro, verify=True)

        # Verificando o status da resposta
        if resposta.status_code == 200:
            # Redirecionar para a página principal ou outra página após o cadastro bem-sucedido
            return redirect(f'/?email={email}')
        else:
            return f"Falha no cadastro. Código de status: {resposta.status_code}. Resposta: {resposta.text}"

    except Exception as e:
        # Adicione um log para registrar a exceção
        app.logger.error(f"Erro durante o cadastro: {str(e)}")
        return f"Falha no cadastro. Erro interno do servidor: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
