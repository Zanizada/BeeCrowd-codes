N = int(input())
numeros = []
soma = 0

while N >= 0:
    numeros.append(N)
    N = int(input())

mediador = len(numeros)

if mediador > 0:
    soma = sum(numeros)
    media = soma / mediador
    print(f'{media:.2f}')
