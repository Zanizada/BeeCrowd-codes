casos_teste = int(input())
sobreviventes = []
sobrevivente = 0

for i in range(casos_teste):
    qntd_pessoas, salto = map(int, input().split())
    
    for pessoas in range(qntd_pessoas):
        sobreviventes.append(pessoas)
        sobrevivente += pessoas

    
    while len(sobreviventes) > 1:
        sobrevivente = (sobrevivente + salto - 1) % len(sobreviventes)
        del sobreviventes(sobrevivente)
    #prints dos casos
    print(f'Case {i}: {sobreviventes[0]}')