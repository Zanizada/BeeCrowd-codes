def josephus(salto, numero_alvo=None, tamanho_lista=None, lista=None):
    if lista is None and tamanho_lista is None:
        raise ValueError("Você precisa fornecer 'lista' ou 'tamanho_lista'.")
    else:
        if lista is None:
            lista = list(range(1, tamanho_lista + 1))
        elif tamanho_lista is None:
            tamanho_lista = len(lista)
        
    lista.remove(1)
    numeros_josephus = 0
    
    while len(lista) > 1:
        numeros_josephus = (numeros_josephus + salto - 1) % len(lista)
        del lista[numeros_josephus]
    
    if numero_alvo is None:
        return lista[0]
    else:
        return lista[0] == numero_alvo

def menor_salto_para_alvo(tamanho_lista, numero_alvo):
    salto = 1
    while True:
        if josephus(salto, numero_alvo, tamanho_lista) == True:
            return salto
        salto += 1

while True:
    qntd_regioes = int(input())

    if qntd_regioes == 0:
        break

    regiao_alvo = 13
    
    salto = menor_salto_para_alvo(qntd_regioes, regiao_alvo)
    print(salto)