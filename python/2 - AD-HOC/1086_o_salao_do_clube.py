def conversao_m_para_cm(numero):
    if isinstance(numero, list):
        return [n * 100 for n in numero]
    else:
        return numero * 100

def encontrar_menor_numero_possivel(lista, alvo):
    lista.sort()
    from collections import Counter
    contador = Counter(lista)
    usados = 0
    while alvo > 0 and lista:
        valor = lista.pop()
        if valor == alvo:
            usados += 1
            return usados
        elif valor < alvo:
            complemento = alvo - valor
            if complemento in contador and (complemento != valor or contador[complemento] > 1):
                usados += 2
                return usados
    return float('inf')

while True:
    try:
        linha = input()
        if not linha.strip():
            continue
        largura, comprimento = map(int, linha.strip().split())
        if largura == 0 and comprimento == 0:
            break

        largura_tabuas_cm = int(input())
        tabuas_doadas = int(input())
        comprimento_tabuas = list(map(int, input().split()))
        
        largura_cm = conversao_m_para_cm(largura)
        comprimento_cm = conversao_m_para_cm(comprimento)
        comprimento_tabuas_cm = conversao_m_para_cm(comprimento_tabuas)

        if largura_cm % largura_tabuas_cm != 0:
            print("impossivel")
            continue

        num_fileiras = largura_cm // largura_tabuas_cm
        comprimento_tabuas_cm.sort()
        from collections import Counter
        contador = Counter(comprimento_tabuas_cm)

        usadas = 0
        sucesso = True

        for _ in range(num_fileiras):
            encontrado = False
            for t in reversed(comprimento_tabuas_cm):
                if contador[t] == 0:
                    continue
                if t == comprimento_cm:
                    contador[t] -= 1
                    usadas += 1
                    encontrado = True
                    break
                elif t < comprimento_cm:
                    resto = comprimento_cm - t
                    if resto == t and contador[t] >= 2:
                        contador[t] -= 2
                        usadas += 2
                        encontrado = True
                        break
                    elif resto != t and contador[resto] > 0:
                        contador[t] -= 1
                        contador[resto] -= 1
                        usadas += 2
                        encontrado = True
                        break
            if not encontrado:
                sucesso = False
                break

        print(usadas if sucesso else "impossivel")

    except EOFError:
        break
