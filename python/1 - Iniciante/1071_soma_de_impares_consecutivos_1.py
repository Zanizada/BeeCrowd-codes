X = int(input())
Y = int(input())

if X > Y:
    X, Y = Y, X
    
soma_impares = 0
for num in range(X + 1, Y):
    if num % 2 != 0:
        soma_impares += num

print(f'{soma_impares}')
