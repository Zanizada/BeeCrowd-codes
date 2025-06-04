qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = []
for tita in tamanho_titas:
    tita = tamanhos[tita]
    titas.append(tita)

