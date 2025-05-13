import random

def num_de_wellington(lista):
    if 13 in lista:
        if lista[-1] == 13:
            pass
        else:
            lista.remove(13)
            lista.append(13)

def josephus(lista, salto):
    num_de_wellington(lista)
    indice = 0
    while len(lista) > 1:
        indice = (indice + salto - 1) % len(lista)
        if lista[indice] == 13:
            lista.append(lista.pop(indice))
        else:
            lista.pop(indice)
    return lista[0]

while True:
    regioes = []
    num_regioes = int(input())
    
    if num_regioes == 0:
        break
    
    num_salto = random.randint(1, num_regioes)

    for num in range(num_regioes):
        regioes.append(num)
    
    resultado = josephus(regioes, num_salto)
    print(resultado)