import operator

casos = int(input())

operadores = {
    "-": operator.sub,
    "+": operator.add,
    "*": operator.mul,
    "/": operator.floordiv
}

for _ in range(casos):
    N1, barra, D1, OP, N2, barra, D2 = input().split()
    