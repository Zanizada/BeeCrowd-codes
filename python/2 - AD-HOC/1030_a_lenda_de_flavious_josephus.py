casos_teste = int(input())

for i in range(casos_teste):
    qntd_pessoas, salto = map(int, input().split())
    sobreviventes = list(range(1, qntd_pessoas + 1))
    sobrevivente = 0

    while len(sobreviventes) > 1:
        sobrevivente = (sobrevivente + salto - 1) % len(sobreviventes)
        del sobreviventes[sobrevivente]

    print(f'Case {i+1}: {sobreviventes[0]}')