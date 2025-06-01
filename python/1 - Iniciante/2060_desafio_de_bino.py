def multiplos(numero, multiplo_um=None, multiplo_dois=None, multiplo_tres=None, multiplo_quatro=None):

tamanho_lista = int(input())
numeros = list(map(int, input().split()))
multiplo_de_dois = 0
multiplo_de_tres = 0
multiplo_de_quatro = 0
multiplo_de_cinco = 0

for numero in numeros:
    if numero % 2 == 0:
