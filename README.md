# README: Portfolio - Aplicação Flask com Formulário de Contato e Autenticação

Este é um exemplo de um portfólio web construído com Flask, que inclui um formulário de contato e funcionalidade de autenticação básica.

## Configuração do Ambiente

Certifique-se de ter as dependências instaladas antes de executar a aplicação. Use o seguinte comando para instalar as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Configuração do Flask-Mail

A aplicação utiliza o Flask-Mail para enviar e-mails. Certifique-se de configurar corretamente as variáveis no arquivo `app.py` sob a seção "Configurações do Flask-Mail" com as informações do seu servidor de e-mail.

## Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando:

```bash
python app.py
```

A aplicação será executada localmente em `http://127.0.0.1:5000/`.

## Funcionalidades

### Página Inicial

- A página inicial cumprimenta o usuário com base no email fornecido na URL.
- Se nenhum email for fornecido, um cumprimento padrão é exibido.

### Formulário de Contato

- A rota `/processa_formulario` processa o formulário de contato enviado por POST.
- O formulário inclui campos para nome, email e mensagem.
- Após o envio bem-sucedido, a página inicial é recarregada.

### Autenticação

- A rota `/login` exibe uma página de login simples.
- A rota `/fazer-login` processa a tentativa de login via POST.
- Os dados de login são enviados para um endpoint remoto usando a biblioteca `requests`.
- Se o login for bem-sucedido, o usuário é redirecionado para a página inicial com o email fornecido.
- Se o login falhar, uma mensagem de erro é exibida.

### Cadastro de Usuário

- A rota `/cadastro` exibe uma página de cadastro.
- A rota `/cadastrar` processa o formulário de cadastro enviado por POST.
- Os dados de cadastro são enviados para um endpoint remoto usando a biblioteca `requests`.
- Se o cadastro for bem-sucedido, o usuário é redirecionado para a página inicial com o email fornecido.
- Se o cadastro falhar, uma mensagem de erro é exibida.

## Erros Comuns

- **500 Internal Server Error:** Erro interno do servidor durante o cadastro. Verifique o log para obter detalhes.
- **E-mail já cadastrado. Escolha outro e-mail:** O e-mail fornecido já está registrado na base de dados. Escolha um e-mail diferente.
- **Falha no login. Código de status: ...:** A tentativa de login falhou. Verifique as credenciais e a conexão com o servidor remoto.
- **Falha no cadastro. Código de status: ... Resposta: ...:** O cadastro falhou. Verifique o código de status e a resposta do servidor remoto para obter detalhes.

Lembre-se de ajustar as configurações conforme necessário para o seu ambiente de desenvolvimento e requisitos específicos do projeto. Este é um exemplo básico que pode ser expandido de acordo com as necessidades da sua aplicação de portfólio.
