var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function gcd(numero_1, numero_2) {
    while (numero_2 !== 0) {
        let temp = numero_2;
        numero_2 = numero_1 % numero_2;
        numero_1 = temp;
    }
    return numero_1;
}

let casos_teste = parseInt(lines[0]);

for (let i = 0; i < casos_teste; i++) {
    let [figurinhas_ricardo, figurinhas_vicente] = lines[i + 1].split(" ");
    figurinhas_ricardo = parseInt(figurinhas_ricardo);
    figurinhas_vicente = parseInt(figurinhas_vicente);
    console.log(gcd(figurinhas_ricardo, figurinhas_vicente));
}