N = int(input())

for num in range(N):
    X = int(input())
    divisores = []

    for num in range(1, X):
        if X % num == 0:
            divisores.append(num)

    if sum(divisores) == X:
        print(f'{X} eh perfeito')

    else:
        print(f'{X} nao eh perfeito')
