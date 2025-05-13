import random

def numeros_sequenciais(condicao):
    num = 1
    while condicao:
        num += 1
    return num

def josephus(tamanho_lista, salto, lista):
    if lista != None:
        lista = list(range(1, tamanho_lista + 1))
    else:
        numeros_josephus = 0
        while len(lista) > 1:
            numeros_josephus = (numeros_josephus + salto - 1) % len(lista)
            del lista[numeros_josephus]
        
    return {lista[0]}

while True:
    qntd_regioes = int(input())
    regioes = []
    