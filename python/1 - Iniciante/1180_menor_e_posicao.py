N = int(input())
X = list(map(int, input().split()))

X = X[:N]

menor = min(X)
posicao = X.index(menor)

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
