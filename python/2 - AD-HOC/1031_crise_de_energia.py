import random

def numeros_sequenciais(condicao):
    num = 1
    while condicao:
        num += 1
    return num

def josephus(salto, tamanho_lista=None, lista=None):
    if lista is None and tamanho_lista is None:
        raise ValueError("Você precisa fornecer 'lista' ou 'tamanho_lista'.")
    else:
        if lista is None:
            lista = list(range(1, tamanho_lista + 1))
        elif tamanho_lista is None:
            tamanho_lista = len(lista)
        
    numeros_josephus = 0
    while len(lista) > 1:
        numeros_josephus = (numeros_josephus + salto - 1) % len(lista)
        del lista[numeros_josephus]
    return {lista[0]}

while True:
    qntd_regioes = int(input())
    regioes = []
    salto = numeros_sequenciais(())