def resolver():
    while True:
        # Entrada: dimensões do salão
        largura, comprimento = map(int, input().split())
        if largura == 0 and comprimento == 0:
            break

        # Lê os demais dados
        largura_tabuas_cm = int(input())
        k = int(input())
        comprimentos_metros = list(map(int, input().split()))

        # Conversão para cm
        largura_cm = largura * 100
        comprimento_cm = comprimento * 100
        comprimentos_cm = [c * 100 for c in comprimentos_metros]

        # Quantas "fileiras" precisamos?
        if largura_cm % largura_tabuas_cm != 0:
            print("impossivel")
            continue
        linhas_necessarias = largura_cm // largura_tabuas_cm

        # Separa tábuas que cobrem sozinhas o comprimento
        sozinhas = []
        pequenas = []
        for t in comprimentos_cm:
            if t >= comprimento_cm:
                sozinhas.append(t)
            else:
                pequenas.append(t)

        # Conta quantas fileiras já dá pra cobrir com tábuas sozinhas
        fileiras_cobertas = min(len(sozinhas), linhas_necessarias)
        total_tabuas_usadas = fileiras_cobertas
        linhas_restantes = linhas_necessarias - fileiras_cobertas

        # Tentar formar pares de tábuas pequenas que somem >= comprimento_cm
        pequenas.sort()
        i = 0
        j = len(pequenas) - 1
        while i < j and linhas_restantes > 0:
            if pequenas[i] + pequenas[j] >= comprimento_cm:
                # Esse par cobre uma fileira
                total_tabuas_usadas += 2
                linhas_restantes -= 1
                i += 1
                j -= 1
            else:
                # Muito pequena, tentar com uma maior
                i += 1

        # Se ainda faltam fileiras, é impossível
        if linhas_restantes > 0:
            print("impossivel")
        else:
            print(total_tabuas_usadas)
