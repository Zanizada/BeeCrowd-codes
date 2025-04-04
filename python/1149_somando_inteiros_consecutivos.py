valores = list(map(int, input().split()))
A, N = valores[0], valores[1]

ind = 2
while N <= 0:
    if ind < len(valores):
        N = valores[ind]
        ind += 1

numeros = []

for i in range(N):
    numeros.append(A+i)

somas = sum(numeros)

print(somas)
