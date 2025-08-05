var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let nome_vendedor = parseFloat(lines[0]);
let salario_fixo = parseFloat(lines[1]);
let vendas = parseFloat(lines[2]);

const comissao = vendas * 0.15;
const salario_total = salario_fixo + comissao;

console.log(`TOTAL = R$ ${salario_total.toFixed(2)}`);