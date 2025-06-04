qntd_titas, tamanho_muralhas = map(int, input().split())
ordem_titas = input().strip()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

muralhas = 1
muralha_restante = tamanho_muralhas

for tita in ordem_titas:
    tamanho_tita = tamanhos[tita]

    if muralha_restante >= tamanho_tita:
        muralha_restante -= tamanho_tita
    else:
        muralha_restante = tamanho_muralhas
        muralha_restante -= tamanho_tita
        muralhas += 1

print(muralhas)
