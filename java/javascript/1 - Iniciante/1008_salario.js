var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let numero_funcionario = parseFloat(lines[0]);
let horas_trabalhadas = parseFloat(lines[1]);
let valor_por_hora = parseFloat(lines[2]);

const salario = horas_trabalhadas * valor_por_hora;

console.log(`NUMBER = ${numero_funcionario}`);
console.log(`SALARY = U$ ${salario.toFixed(2)}`);