const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const pi = 3.14159;
const raio =  parseFloat(lines[0]);
const area = pi * Math.pow(raio, 2);

console.log(`A=${area.toFixed(4)}`);