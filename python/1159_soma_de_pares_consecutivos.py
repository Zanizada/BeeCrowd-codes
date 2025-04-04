while True:
    X = int(input())

    if X == 0:
        break

    soma = 0
    contador = 0

    while contador < 5:
        if X % 2 == 0:
            soma += X
            contador += 1
        X += 1

    print(soma)
