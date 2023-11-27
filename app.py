from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import requests

app = Flask(__name__)

# Configurações do Flask-Mail (substitua com suas próprias configurações)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'netmultiverso@gmail.com'
app.config['MAIL_PASSWORD'] = 'jbus eqwl ohfu htud'


mail = Mail(app)

url_pessoas = 'https://api-usuarios-tvdy.onrender.com/pessoas'
url_login = 'https://api-usuarios-tvdy.onrender.com/login'

@app.route('/')
def index():
    email = request.args.get('email')
    dados_usuario = None
    nome = "Recrutador"
    
    if email:
        urlEmail = f'https://api-usuarios-tvdy.onrender.com/pessoas/email/{email}'
        resposta = requests.get(urlEmail)

        if resposta.status_code == 200:
            dados_usuario = resposta.json()
            nome = dados_usuario['pessoa']['nome']

    saudacao = f"Olá, {nome}! Guilherme aqui"
    print(saudacao)
    
    return render_template('index.html', nome=saudacao)

@app.route('/processa_formulario', methods=['POST'])
def processa_formulario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        # Configurar e enviar e-mail
        msg = Message('"ATENÇÃO NOVO RECRUTADOR"',
                      sender='seu_email@example.com',
                      recipients=['netmultiverso@gmail.com'])  # Substitua pelo seu endereço de e-mail
        msg.body = f"Nome: {nome}\nE-mail: {email}\nMensagem:\n{mensagem}"

        mail.send(msg)

        # Redirecionar para uma página de sucesso
        return render_template('index.html')

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
