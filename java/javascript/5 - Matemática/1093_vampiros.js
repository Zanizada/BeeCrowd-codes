var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

function probabilidade(num1, num2) {
    if (num1 <= 0) {
        return 0.0;
    }
    if (num2 <= 0) {
        return 1.0;
    }
    if (num1, num2) {
        
    }
}

while (true) {
    let EV1 = parseInt(lines[0]);
    let EV2 = parseInt(lines[1]);
    const AT = parseInt(lines[2]);
    const D = parseInt(lines[3]);

    if ((EV1 == 0) & (EV2 == 0) & (AT == 0) & (D == 0)) {
        break
    }


}

/*
dado de 6 lados
6 = 100%
1 = x
6x = 100
x = 100 / 6
x = 16,66
*/