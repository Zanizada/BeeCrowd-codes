X = int(input())
Z = int(input())

while Z <= X:
        Z = int(input())

qntd = 1
soma = X

while soma < Z:
    X += 1
    soma += X
    qntd += 1

print(qntd)
