def josephus(lista, salto):
    while len(lista) > 1:
        ultimo_valor = (ultimo_valor + salto - 1) % len(lista)
        del lista[ultimo_valor]