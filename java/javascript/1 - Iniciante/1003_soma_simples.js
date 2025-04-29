const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const A = parseInt(lines[0]);
const B = parseInt(lines[1]);
const SOMA = A + B;

console.log(`SOMA = ${SOMA}`);