vetores = []

for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    vetores.append(x)

for i in range(10):
    print(f'X[{i}] = {vetores[i]}')
