X = float(input())
valores = [X]
vetor = 0
N = 0

while vetor < 100:
    X /= 2
    valores.append(X)
    vetor += 1

for i in range(100):
    print(f'N[{i}] = {valores[i]:.4f}')
