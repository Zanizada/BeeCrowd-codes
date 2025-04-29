a, b, c = map(int, input().split())

numeros = [a, b, c]
ordenados = sorted(numeros)

for num in ordenados:
    print(f'{num}')
print()
for num in numeros:
    print(f'{num}')
