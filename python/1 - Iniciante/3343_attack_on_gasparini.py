qntd_titas, tamanho_muralhas = map(int, input().split())
ordem_titas = input().strip()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

muralhas = 1
muralha = tamanho_muralhas

for tita in ordem_titas:
    tamanho_tita = tamanhos[tita]

    while tamanho_tita > muralha:
        muralha = tamanho_muralhas
        muralhas += 1
    
    muralha -= tamanho_tita

print(muralhas)
