ordem = []

while True:
    X, Y = map(int, input().split())

    if X == Y:
        break

    if X > Y:
        ordem.append('Decrescente')

    elif X < Y:
        ordem.append('Crescente')

print('\n'.join(ordem))
