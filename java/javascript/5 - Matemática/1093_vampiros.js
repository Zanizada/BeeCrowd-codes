var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function probabilidade(num1, num2, num3, num4, memo) {
    if (num1 <= 0) return 0.0;
    if (num2 <= 0) return 1.0;

    const key = `${num1},${num2}`;
    if (memo.has(key)) return memo.get(key);

    const p1_win_turn = num3 / 6;
    const p2_win_turn = (6 - num3) / 6;

    const p =
        p1_win_turn * probabilidade(num1 + num4, num2 - num4, num3, num4, memo) +
        p2_win_turn * probabilidade(num1 - num4, num2 + num4, num3, num4, memo);

    memo.set(key, p);
    return p;
    }

while (true) {
    const [EV1, EV2, AT, D] = lines.split(" ").map(Number);
    if ((EV1 === 0) && (EV2 === 0) && (AT === 0) && (D === 0)) break;

    const memo = new Map();
    const resultado = probabilidade(EV1, EV2, AT, D, memo) * 100;
    console.log(resultado.toFixed(1));
}