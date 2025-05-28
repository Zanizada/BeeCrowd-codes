def verificar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

A, B, C, D = sorted(map(int, input().split()), reverse=True)

if (verificar_triangulo(A, B, C) or
    verificar_triangulo(A, C, D) or
    verificar_triangulo(B, C, D) or
    verificar_triangulo(A, B, D)):
    print("S")
else:
    print("N")