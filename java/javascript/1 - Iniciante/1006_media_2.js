var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

let A = parseFloat(lines[0]);
let B = parseFloat(lines[1]);
let C = parseFloat(lines[2]);

const PA = 2.0;
const PB = 3.0;
const PC = 5.0;

let MEDIA = ((A * PA) + (B * PB) + (C * PC)) / (PA + PB + PC);

console.log(`MEDIA = ${MEDIA.toFixed(1)}`);