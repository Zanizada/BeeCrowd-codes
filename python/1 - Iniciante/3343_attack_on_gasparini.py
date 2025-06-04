qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input().strip()
pequeno, medio, grande = map(int, input().split())
muralhas = 1

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = [tamanhos[tita] for tita in tamanho_titas]
tamanho_total_titas = sum(titas)

if tamanho_total_titas > tamanho_muralhas:
    for i in range(qntd_titas):
        1 = 0

# 3 titas, 20 metros de muralha
# 1 médio, 1 pequeno, 1 grande
# P = 3, M = 8, G = 10
# 