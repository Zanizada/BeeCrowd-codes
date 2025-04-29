A, B, C = map(float, input().split())

triangulo = all([A + B > C, A + C > B, B + C > A])

if triangulo == True:
    P = A+B+C
    print(f'Perimetro = {P:.1f}')
else:
    Ar = ((A+B)*C)/2
    print(f'Area = {Ar:.1f}')
