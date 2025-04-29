a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

N = [a, b, c, d, e]
par = 0
impar = 0
positivo = 0
negativo = 0

for num in N:
    if num % 2 == 0:
        par += 1
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1
    elif num % 2 > 0:
        impar += 1
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
