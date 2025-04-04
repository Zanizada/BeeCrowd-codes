numeros = []

for _ in range(100):
    num = int(input())
    numeros.append(num)

maior = max(numeros)
posicao = numeros.index(maior) + 1

print(maior)
print(posicao)
