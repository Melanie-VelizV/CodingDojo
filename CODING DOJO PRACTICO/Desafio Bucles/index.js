//--------------------------------------
console.log("Impares del 1 al 20");
for (let i = 1; i <= 20; i++) {
    if (i % 2!== 0) {
        console.log(i);
    }
}
//--------------------------------------
console.log("Disminuir Multiplos de 3");
for (let i = 100; i >= 0; i--) {
    if (i % 3 == 0) {
        console.log(i);
    }
}
//--------------------------------------
console.log("Imprime la secuencia");
for (let i =4;i >=-3.5; i-=1.5)   {
    console.log(i);
}
//--------------------------------------
console.log("Sigma");
let sum = 0;
for (let i = 1; i <= 100; i++) {
    sum+=i;
}
console.log(sum);
//--------------------------------------
console.log("Factorial");
let product = 1;
for (let i = 1; i <= 12; i++) {
    product=product*i;
}
console.log(product);