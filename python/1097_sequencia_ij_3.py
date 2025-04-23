I = 1
J = 7
contador = 0

while I <= 9:
    print(f'I={I} J={J}')
    J -= 1
    contador += 1

    if contador == 3:
        I += 2
        J = 7
        contador = 0

    if I > 9:
        break
