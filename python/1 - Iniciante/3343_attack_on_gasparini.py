qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input().strip()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = [tamanhos[tita] for tita in tamanho_titas]
tamanho_soma_titas = sum(titas)
muralha_atual = tamanho_muralhas
muralhas = 1

if tamanho_soma_titas > tamanho_muralhas:
    for i in range(qntd_titas):
        muralha_atual -= titas[i]
        if i < qntd_titas-1:
            if muralha_atual < titas[i+1]:
                muralhas += 1
                muralha_atual += tamanho_muralhas

print(muralhas)
