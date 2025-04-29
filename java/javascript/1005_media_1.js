const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const A = parseFloat(lines[0]);
const B = parseFloat(lines[1]);
const MEDIA = ((3.5 * A) + (7.5 * B))/(3.5 + 7.5);

console.log(`MEDIA = ${MEDIA.toFixed(5)}`);