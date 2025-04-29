A, B, C = map(float, input().split())

triangulo = sorted([A, B, C], reverse=True)
A, B, C = triangulo

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
