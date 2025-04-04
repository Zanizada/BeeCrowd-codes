T = int(input())

valores = []

for i in range(1000):
    valores.append(i % T)

for i in range(1000):
    print(f'N[{i}] = {valores[i]}')
