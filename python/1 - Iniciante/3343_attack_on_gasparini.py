qntd_titas, tamanho_muralhas = map(int, input().split())
ordem_titas = input().strip()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}
# pequeno = 3, medio = 4, grande = 5
muralhas = 1
muralha = tamanho_muralhas
# muralha = 6
for tita in ordem_titas:
    # tita = [G, P, M, P]
    tamanho_tita = tamanhos[tita]
    # tamanho_tita = [5, 3, 4, 3]
    muralha -= tamanho_tita
    # 1º --> 6 - 5 = 1.
    while tamanho_tita > muralha:
        # 5 > 1 = True:
        muralha = tamanho_muralhas
        # 
        muralhas += 1
    
    muralha -= tamanho_tita

print(muralhas)