X, Y = map(int, input().split())

num = 1
for _ in range(Y // X):
    linha = []
    for _ in range(X):
        linha.append(str(num))
        num += 1
    print(" ".join(linha))
