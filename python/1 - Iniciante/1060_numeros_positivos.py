a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

N = [a, b, c, d, e, f]

contador = 0

for num in N:
    if num > 0:
        contador += 1

print(f'{contador} valores positivos')
