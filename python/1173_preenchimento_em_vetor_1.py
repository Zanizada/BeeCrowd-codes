V = int(input())

vetores = [V]

for i in range(1, 10):
    vetores.append(vetores[i - 1] * 2)

for i in range(10):
    print(f'N{[i]} = {vetores[i]}')
