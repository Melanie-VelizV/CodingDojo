function turnOff(element) {
    if (element.innerText === 'Abrir Sesión') {
    element.innerText = "Cerrar Sesión";
    }else {
        element.innerText = "Abrir Sesión";
    }   
}

function hide(element) {
    element.remove();
}

function mostraAlerta() {
    // podemos incluir más código aquí si queremos
    alert('Ninja fue likeado');
}
