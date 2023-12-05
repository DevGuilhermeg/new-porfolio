document.getElementById('projetos').addEventListener('click', function () {
    var projetosSection = document.getElementById('projetosSection');

    if (projetosSection.style.display === 'none') {
        // Se a seção estiver oculta, exibe e aguarda 100ms para garantir que seja renderizada
        projetosSection.style.display = 'block';
        setTimeout(function() {
            projetosSection.scrollIntoView({ behavior: 'smooth' });
        }, 100);
    } else {
        // Se a seção estiver visível, rola suavemente até ela
        projetosSection.scrollIntoView({ behavior: 'smooth' });
    }
});


document.getElementById('contato').addEventListener('click', function () {
    var projetosSection = document.getElementById('mensagem');

    if (projetosSection.style.display === 'none') {
        // Se a seção estiver oculta, exibe e aguarda 100ms para garantir que seja renderizada
        projetosSection.style.display = 'block';
        setTimeout(function() {
            projetosSection.scrollIntoView({ behavior: 'smooth' });
        }, 100);
    } else {
        // Se a seção estiver visível, rola suavemente até ela
        projetosSection.scrollIntoView({ behavior: 'smooth' });
    }
});

// Abrir opções do projeto

function abrirProjeto(titulo, descricao,) {
    // Atualizar o conteúdo do modal com informações específicas do projeto
    document.getElementById('projetoTitulo').innerHTML = titulo;
    document.getElementById('projetoDescricao').innerHTML = descricao;

  
    // Exibir o modal
    document.getElementById('myModal').style.display = 'block';
  
    // Exibir os botões específicos para cada projeto
    if (titulo === 'API Registro de Usuário') {
      document.getElementById('botaoAbrirProjeto1').style.display = 'block';
      document.getElementById('botaoLoginProjeto1').style.display = 'block';
      document.getElementById('botaoCadastroProjeto1').style.display = 'block';
      
    } else if (titulo === 'Projeto 2') {
      document.getElementById('botaoProjeto1').style.display = 'none';
      document.getElementById('botaoProjeto2').style.display = 'block';
      document.getElementById('botaoProjeto3').style.display = 'none';
    } else if (titulo === 'Projeto 3') {
      document.getElementById('botaoProjeto1').style.display = 'none';
      document.getElementById('botaoProjeto2').style.display = 'none';
      document.getElementById('botaoProjeto3').style.display = 'block';
    }
  };
  
  function fecharModal() {
    // Fechar o modal
    document.getElementById('myModal').style.display = 'none';
  
    // Ocultar os botões ao fechar o modal
    document.getElementById('botaoProjeto1').style.display = 'none';
    document.getElementById('botaoProjeto2').style.display = 'none';
    document.getElementById('botaoProjeto3').style.display = 'none';
  }
  
  function cadastrarProjeto(projeto) {
    // Implemente a lógica para cadastro específico do projeto
    alert(`Cadastrar no projeto: ${projeto}`);
  }
  
  function loginProjeto(projeto) {
    // Implemente a lógica para login específico do projeto
    alert(`Login no projeto: ${projeto}`);
  }
  // Fechar o modal se o usuário clicar fora da área do conteúdo
window.onclick = function(event) {
    var modal = document.getElementById('myModal');
    if (event.target == modal) {
      fecharModal();
    }
  }
  // Adicione um ouvinte de evento para o evento de rolagem
  window.addEventListener("scroll", function() {
    var nav = document.querySelector('.headerr');
    var buttonSignIn = this.document.querySelector('.button-sign-in')
    
    // Verifica se a posição vertical da barra de rolagem é maior que 0
    if (window.scrollY > 150) {
      nav.classList.add('fixed'); // Adiciona a classe 'fixed'
      buttonSignIn.classList.add('none')
    } else {
      nav.classList.remove('fixed'); // Remove a classe 'fixed'
      buttonSignIn.classList.remove('none')
    }
  });

  document.addEventListener('DOMContentLoaded', function () {
    const openModalBtn = document.getElementById('openModalBtn');
    const modal = document.querySelector('.modal');
  
    openModalBtn.addEventListener('click', function () {
      modal.style.display = 'block';
      modal.classList.add('fade-in'); // Adiciona a classe para a animação
  
      // Adiciona uma classe 'modal-open' ao body para evitar que o conteúdo por trás do modal seja clicado
      document.body.classList.add('modal-open');
    });
  
    const closeModalBtn = document.querySelector('.close');
    closeModalBtn.addEventListener('click', function () {
      modal.style.display = 'none';
      modal.classList.remove('fade-in'); // Remove a classe para a animação
  
      // Remove a classe 'modal-open' ao body quando o modal é fechado
      document.body.classList.remove('modal-open');
    });
  });
