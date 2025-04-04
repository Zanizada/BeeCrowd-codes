X = int(input())

if X % 2 == 0:
    N1 = X + 1
    N2 = X + 3
    N3 = X + 5
    N4 = X + 7
    N5 = X + 9
    N6 = X + 11

elif X % 2 > 0:
    N1 = X
    N2 = X + 2
    N3 = X + 4
    N4 = X + 6
    N5 = X + 8
    N6 = X + 10

print(f'{N1}')
print(f'{N2}')
print(f'{N3}')
print(f'{N4}')
print(f'{N5}')
print(f'{N6}')
