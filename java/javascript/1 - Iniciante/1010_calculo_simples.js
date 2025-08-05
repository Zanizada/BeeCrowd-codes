var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let [codigo_peca_1, num_pecas_1, valor_pecas_1] = lines[0].split(" ");
codigo_peca_1 = parseInt(codigo_peca_1);
num_pecas_1 = parseInt(num_pecas_1);
valor_pecas_1 = parseFloat(valor_pecas_1);

let [codigo_peca_2, num_pecas_2, valor_pecas_2] = lines[0].split(" ");
codigo_peca_2 = parseInt(codigo_peca_2);
num_pecas_2 = parseInt(num_pecas_2);
valor_pecas_2 = parseFloat(valor_pecas_2)

const total_peca_1 = num_pecas_1 * valor_pecas_1;
const total_peca_2 = num_pecas_2 * valor_pecas_2;
const total = total_peca_1 + total_peca_2;

console.log(`VALOR A PAGAR: R$ ${total.toFixed(2)}`);