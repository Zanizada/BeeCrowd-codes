A, B, C = map(float, input().split())
pi = 3.14159
At = (A*C)/2
Ac = pi*C**2
Atr = ((A+B)*C)/2
Aq = B**2
Ar = A*B
print(f'TRIANGULO: {At:.3f}')
print(f'CIRCULO: {Ac:.3f}')
print(f'TRAPEZIO: {Atr:.3f}')
print(f'QUADRADO: {Aq:.3f}')
print(f'RETANGULO: {Ar:.3f}')
