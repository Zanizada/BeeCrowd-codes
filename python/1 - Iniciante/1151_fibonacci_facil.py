N = int(input())

a, b = 0, 1
numeros = [a, b]

for _ in range(N - 2):
    a, b = b, a + b
    numeros.append(b)

resultado = numeros
print(" ".join(map(str, resultado)))
