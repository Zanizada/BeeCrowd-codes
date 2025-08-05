var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function criptografia(texto) {
    let caracteres = [];

    // Passada 1
    for (let caractere of texto) {
        if (/[a-zA-Z]/.test(caractere)) {
            let unidade = caractere.charCodeAt(0);
            let unidade_cripto = String.fromCharCode(unidade + 3);
            caracteres.push(unidade_cripto);
        } else {
            caracteres.push(caractere);
        }
    }

    // Passada 2
    caracteres = caracteres.reverse();

    // Passada 3
    let meio = Math.floor(caracteres.length / 2);
    let primeira_metade = caracteres.slice(0, meio);
    let segunda_metade = caracteres.slice(meio);
    let metade_cripto = [];

    for (let caractere of segunda_metade) {
        let unidade = caractere.charCodeAt(0);
        let unidade_cripto = String.fromCharCode(unidade - 1);
        metade_cripto.push(unidade_cripto);
    }

    // Conclusão
    let caracteres_finais = primeira_metade.concat(metade_cripto);
    let mensagem_criptografada = caracteres_finais.join("");
    return mensagem_criptografada;
}

let testes = parseInt(lines[0]);
for (let i = 0; i < testes; i++) {
    let mensagem = lines[i + 1];
    console.log(criptografia(mensagem));
}