var contador = [0,0,0];

function aumentarLikes(indice){
    contador[indice]++;
    if(indice===0){
        var contadorElemento = document.getElementById('likeUno');
        contadorElemento.innerText = contador[indice] + ' Like(s)';
    }else if(indice===1){
        var contadorElemento = document.getElementById('likeDos');
        contadorElemento.innerText = contador[indice] + ' Like(s)';
    }else if(indice===2){
    var contadorElemento = document.getElementById('likeTres');
    contadorElemento.innerText = contador[indice] + ' Like(s)';
    }
}