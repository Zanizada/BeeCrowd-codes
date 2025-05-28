casos_teste = int(input())

for _ in range(casos_teste):
    ano = int(input())
    anos_passados = 2015 - ano
    if anos_passados <= 0:
        anos_passados = f"{abs(anos_passados-1)} A.C."
    else:
        anos_passados = f"{abs(anos_passados)} D.C."
    
    print(anos_passados)