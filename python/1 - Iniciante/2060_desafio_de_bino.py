def verificar_multiplos(numeros=list, multiplos=list):
    contador = 0
    resultados = []
    for multiplo in multiplos:
        for numero in numeros:
            if numero % multiplo == 0:
                resultado = f"{contador} Multiplos(s) de {multiplo}"
                contador += 1
        resultados.append(resultado)
    return resultados

tamanho_lista = int(input())
numeros = list(map(int, input().split()))
multiplos = [2, 3, 4, 5]

print(verificar_multiplos(numeros, multiplos))