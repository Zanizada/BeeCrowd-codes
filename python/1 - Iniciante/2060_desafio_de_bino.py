def multiplos(numero, multiplos=list):
    contador = 0
    resultados = []
    for multiplo in multiplos:
        resultado = f"{contador} Multiplos(s) de {multiplo}"
        if numero % multiplo == 0:
            contador += 1
        resultados.append(resultado)
        return resultado

tamanho_lista = int(input())
numeros = list(map(int, input().split()))

for numero in numeros:
    if numero % 2 == 0: