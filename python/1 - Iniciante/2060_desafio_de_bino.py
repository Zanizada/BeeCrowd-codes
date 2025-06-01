def verificar_multiplos(numeros=list, multiplos=list):
    
    i = 0
    resultados = []
    while i <= len(multiplos):
        contador = 0
        for numero in numeros:
            if numero % multiplos[i] == 0:
                contador += 1
                resultado = f"{contador} Multiplos(s) de {multiplos[i]}"
            else:
                resultado = f"{contador} Multiplos(s) de {multiplos[i]}"
        i += 1
        resultados.append(resultado)
    return resultados

tamanho_lista = int(input())
numeros = list(map(int, input().split()))
multiplos = [2, 3, 4, 5]

print(verificar_multiplos(numeros, multiplos))