N = int(input())

for num in range(1, N+1):
    X, Y = map(int, input().split())

    soma = 0
    for num in range(min(X, Y) + 1, max(X, Y)):
        if num % 2 != 0:
            soma += num

    print(soma)
