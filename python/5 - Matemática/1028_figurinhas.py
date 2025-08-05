from math import gcd

casos_teste = int(input())

for i in range(casos_teste):
    figurinhas_ricardo, figurinhas_vicente = map(int, input().split())
    print(gcd(figurinhas_ricardo, figurinhas_vicente))
