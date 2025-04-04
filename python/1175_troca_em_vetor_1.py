valores = []

for i in range(20):
    valores.append(int(input()))

for i, valor in enumerate(valores[::-1]):
    print(f'N[{i}] = {valor}')
