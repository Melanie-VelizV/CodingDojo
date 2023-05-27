var contador = 0;

function aumentarLikes(){
    contador++;
    var contadorElemento = document.getElementById('like');
    contadorElemento.innerText = contador + ' Like(s)';
}