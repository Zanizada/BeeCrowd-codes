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
    # 64 > 20 = True
    for i in range(qntd_titas):
        # i = [0, 1, 2, 3, 4, 5, 6, 7]
        muralha_atual -= titas[i]
        # titas    = [8, 10, 10, 3, 10, 10, 10, 3]
        # posicoes = [0, 1,  2,  3, 4,  5,  6,  7]
        # 20 -  8(i --> 0) = 12;
        # 12 - 10(i --> 1) =  2;
        # 20 - 10(i --> 2) = 10;
        # 10 -  3(i --> 3) =  7;
        # 20 - 10(i --> 4) = 10;
        # 10 - 10(i --> 5) =  0;
        # 20 - 10(i --> 6) = 10;
        # 10 -  3(i --> 7) =  7;
        if i < qntd_titas-1:
            # i = 0 < 7 ==  True;
            # i = 1 < 7 ==  True;
            # i = 2 < 7 ==  True;
            # i = 3 < 7 ==  True;
            # i = 4 < 7 ==  True;
            # i = 5 < 7 ==  True;
            # i = 6 < 7 ==  True;
            # i = 7 < 7 == False;
            if muralha_atual < titas[i+1]:
                # 12 < 10(i + 1 = 1) == False;
                #  2 < 10(i + 1 = 2) ==  True;
                # 10 <  3(i + 1 = 3) == False;
                #  7 < 10(i + 1 = 4) ==  True;
                # 10 < 10(i + 1 = 5) == False;
                #  0 < 10(i + 1 = 6) ==  True;
                # 10 <  3(i + 1 = 7) == False;
                muralha_atual = tamanho_muralhas
                # 2 --> 20 (i = 1);
                # 7 --> 20 (i = 3);
                # 0 --> 20 (i = 5);
                muralhas += 1
                # muralhas = 2;
                # muralhas = 3;
                # muralhas = 4;

print(muralhas)
# muralhas = 4

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