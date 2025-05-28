n = int(input())
ti = list(map(int, input().split()))

menor = ti[0]
indice = 1

for i in range(1, n):
    if ti[i] < menor:
        menor = ti[i]
        indice = i + 1

print(indice)
