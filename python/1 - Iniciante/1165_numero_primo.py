N = int(input())

for num in range(N):
    X = int(input())
    divisores = 0

    for num in range(1, X+1):
        if X % num == 0:
            divisores += 1

    if divisores == 2:
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')
