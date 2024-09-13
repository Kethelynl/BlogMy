btn_menu = document.getElementById("btn-menu")


window.addEventListener('load', function() {
    
    const login = document.getElementById("btn-entrar")
    const cadastro = document.getElementById("btn-cadastrar")

    // Verifica se já existe uma escolha armazenada no LocalStorage
    const escolha = localStorage.getItem('escolha');

    if (escolha === 'cadastro') {
        // Se o usuário escolheu 'cadastro', posiciona a bolinha no ícone de cadastro
        login.classList.remove('active');
        cadastro.classList.add('active', 'exit-left');
    } else {
        // Por padrão, a bolinha fica no ícone de login
        login.classList.add('active', 'exit-rigth');
        cadastro.classList.remove('active');
    }

    // Adiciona eventos de clique para armazenar a escolha do usuário
    login.addEventListener('click', function() {
        localStorage.setItem('escolha', 'login');
        login.classList.add('click');
        cadastro.classList.remove('click');
        // Redireciona para a página de login
        window.location.href = 'users/login';
    });

    cadastro.addEventListener('click', function() {
        localStorage.setItem('escolha', 'cadastro');
        cadastro.classList.add('active');
        login.classList.remove('active');
        // Redireciona para a página de cadastro
        window.location.href = 'users/cadastro';
    });
});


click = 1
// verificação do menu
function AbrirMenu(){
    menu = document.getElementById("nav-list_celular")

    if(click == 1){
        // se o usuario clicar uma vez o menu abre
        menu.classList.add("active")
        click = 2
    }else if(click == 2){
        // se o usuario clicar de novo ele fecha
        menu.classList.remove("active")
        click = 1
    }
}



btn_menu.addEventListener('click', AbrirMenu)