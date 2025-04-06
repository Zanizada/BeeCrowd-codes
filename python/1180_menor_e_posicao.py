N = int(input())

for _ in range(N):
    X = [map(int, input().split())]
    menor = min(X)
    posicao = X.index(menor) + 1

print(f'Menor Valor: {menor}')
print(f'Posicao: {posicao}')
