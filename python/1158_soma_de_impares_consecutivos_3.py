N = int(input())

for num in range(N):
    X, Y = map(int, input().split())

    soma = 0
    contador = 0
    
    while contador < Y:
        if X % 2 != 0:
            soma += X
            contador += 1
        X += 1

    print(soma)
