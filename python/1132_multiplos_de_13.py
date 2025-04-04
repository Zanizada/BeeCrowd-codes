X = int(input())
Y = int(input())

numeros = []

if X < Y:
    X, Y = Y, X

for num in range(Y, X+1):

    if num % 13 != 0:
        numeros.append(num)
        soma = sum(numeros)

print(soma)
