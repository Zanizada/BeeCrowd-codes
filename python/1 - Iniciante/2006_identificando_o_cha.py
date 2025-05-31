cha = int(input())
a, b, c, d, e = map(int, input().split())
competidores = [a, b, c, d, e]
corretos = 0
for competidor in competidores:
    if competidor == cha:
        corretos += 1
print(corretos)