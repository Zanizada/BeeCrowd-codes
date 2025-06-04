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
muralha_atual = tamanho_muralhas

if tamanho_total_titas > tamanho_muralhas:
    for i in range(1, qntd_titas+1):
        

# 8 titas, 20 metros de muralha
# 1 médio, 2 grandes, 1 pequeno, 3 grandes, 1 pequeno
# P = 3, M = 8, G = 10

# 1ª Muralha:
    # 20 - 8 = 12; 1 M
    # 12 - 10 = 2; 1 G
    # 2 < 10, CAIU.

# 2ª Muralha:
    # 20 - 10 = 10; 1 G
    # 10 - 3  = 7;  1 P
    # 7 < 10, CAIU.
# 3ª Muralha:
    # 20 - 10 = 10; 1 G
    # 10 - 10 = 0;  1 G
    # 0 < 10, CAIU.
# 4ª Muralha:
    # 20 - 10 = 10; 1 G
    # 10 - 3  = 7;  1 P

# total de muralhas: 4