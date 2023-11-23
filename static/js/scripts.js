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
