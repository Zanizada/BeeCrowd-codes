X = int(input())
Y = int(input())

if X < Y:
    X, Y = Y, X

numeros = []

for num in range(Y+1, X):

    if num % 5 == 2 or num % 5 == 3:

        print(f'{num}')
