qntd_titas, tamanho_muralhas = map(int, input().split())
tamanho_titas = input().strip()
pequeno, medio, grande = map(int, input().split())

tamanhos = {
    "P": pequeno,
    "M": medio,
    "G": grande
}

titas = [tamanhos[tita] for tita in tamanho_titas]
tamanho_total_titas = sum(titas)
muralha_atual = tamanho_muralhas

muralhas = 1
# 1ª Muralha.
if tamanho_total_titas > tamanho_muralhas:
    # 12 > 6 = True.
    for i in range(qntd_titas):
        # titas = [5, 3, 4, 3]
        # i     = [0, 1, 2, 3]
        muralha_atual -= titas[i]
        # 6 - 5(i = 0) = 1;
        # 7 - 3(i = 1) = 4;
        # 4 - 4(i = 2) = 0;
        # 6 - 3(i = 3) = 3;
        if i < qntd_titas-1:
            # i = 0 < 3 ==  True;
            # i = 1 < 3 ==  True;
            # i = 2 < 3 ==  True;
            # i = 3 < 3 == False;
            if muralha_atual < titas[i+1]:
                # 1 < 3(i + 1 = 1) ==  True;
                # 4 < 4(i + 1 = 2) == False;
                # 0 < 3(i + 1 = 3) ==  True;
                muralha_atual += tamanho_muralhas
                # 1 + 6 = 7. (i = 0);
                # 0 + 6 = 6. (i = 2);
                muralhas += 1
                # muralhas = 2;
                # muralhas = 3;

print(muralhas)
# muralhas = 4