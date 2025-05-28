casos_teste = int(input())

for _ in range(casos_teste):
    ano = int(input())
    anos_passados = 2015 - ano
    if anos_passados <= 0:
        anos_passados = f"A.C. {anos_passados-1}"