//Función que crea un objeto pizza
function pizzaOven(tipoCoreteza,tipoSalsa,queso,salsas) {
    var pizza = {};
        pizza.tipoCoreteza = tipoCoreteza;
        pizza.tipoSalsa = tipoSalsa;
        pizza.queso = queso;
        pizza.salsas = salsas;
        return pizza;
}

var p1 = pizzaOven("estilo Chicago", "tradicional", ["mozzarella"], ["pepperoni", "salchicha"]);
console.log(p1);

var p2 = pizzaOven("lanzada a mano" , "marinara" , ["mozzarella", "feta"], ["champiñones", "aceitunas", "cebollas"]);
console.log(p2);

var p3 = pizzaOven("pan plano", "barbacoa casera", ["mozzarella"], ["pepperoni", "pollo", "champiñones"]);
console.log(p3);

var p4 = pizzaOven("pan plano", "barbacoa casera", ["mozzarella"], ["pepperoni", "carne vacuno", "choclo"]);
console.log(p4);
