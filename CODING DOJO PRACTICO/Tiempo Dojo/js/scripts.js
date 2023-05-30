function mostraAlerta() {
    // podemos incluir más código aquí si queremos
    alert('Cargando reporte del tiempo');
}

function ocultar(){
    var cookies = document.getElementById('cookies');
    cookies.remove();
}

function modificar(element) {
    let temp = document.querySelectorAll(".max, .min");  
    for (let i=0; i<temp.length; i++) {
        let currentTemp = parseFloat(temp[i].textContent);
        if (element.value === "fahrenheit") {
            let valorFahrenheit = (currentTemp * 9/5) + 32;
            temp[i].textContent = parseInt(valorFahrenheit) + "°";
        } else if (element.value === "celsius") {
            let valorCelsius = (currentTemp - 32) * 5/9;
            temp[i].textContent = parseInt(valorCelsius) + "°";
        }
    }
}