casos_teste = int(input())
sobreviventes = []
sobrevivente = None

for i in range(casos_teste):
    qntd_pessoas, salto = map(int, input().split())
    
    for pessoas in range(qntd_pessoas):
        sobreviventes.append(pessoas)
        sobrevivente =+ pessoas

    tamanho_lista = len(sobreviventes)

    while tamanho_lista > 1:
        sobrevivente -= sobreviventes[salto]

    #prints dos casos
    print(f'Case {i}: {sobrevivente}')