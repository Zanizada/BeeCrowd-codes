A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

contador = 0
N = [A, B, C, D, E]
for num in N:
    if num % 2 == 0:
        contador += 1

print(f'{contador} valores pares')
