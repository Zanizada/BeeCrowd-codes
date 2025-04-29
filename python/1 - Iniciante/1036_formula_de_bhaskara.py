import math

A, B, C = map(float, input().split())

Δ = (B**2)-(4*A*C)

if Δ < 0:
    print(f'Impossivel calcular')
elif A <= 0:
    print(f'Impossivel calcular')
else:
    R1 = (-B +math.sqrt(Δ)) / (2*A)
    R2 = (-B -math.sqrt(Δ)) / (2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')
