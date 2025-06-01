def verificar_multiplos(numeros=list, multiplos=list):
    
    resultados = []
    for multiplo in multiplos:
        contador = 0
        for numero in numeros:
            if numero % multiplo == 0:
                contador += 1
                resultado = f"{contador} Multiplos(s) de {multiplo}"
        resultados.append(resultado)
    return resultados

tamanho_lista = int(input())
numeros = list(map(int, input().split()))
multiplos = [2, 3, 4, 5]

print(verificar_multiplos(numeros, multiplos))