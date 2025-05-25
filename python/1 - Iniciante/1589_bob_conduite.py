import math

pi = math.pi
casos_teste = int(input())
for _ in range(casos_teste):
    R1, R2 = map(int, input().split())
    area1 = pi*(R1**2)
    area2 = pi*(R2**2)
    area = area1+area2
    