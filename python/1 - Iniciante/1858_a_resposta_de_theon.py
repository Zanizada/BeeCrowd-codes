qntd_pessoas = int(input())
pessoas = list(map(int, input().split()) for _ in range(qntd_pessoas))
contador = 0

for i in range(1, qntd_pessoas+1):
    if i in pessoas:
        contador += 1

print(contador)