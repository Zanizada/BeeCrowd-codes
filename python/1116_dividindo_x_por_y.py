N = int(input())

for num in range(1, N+1):
    X, Y = map(int, input().split())

    if Y == 0:
        print(f'divisao impossivel')
    else:
        divisao = X / Y
        print(f'{divisao}')
