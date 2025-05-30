numeros = int(input())
numeros = str(numeros)
lista = []
for num in numeros:
    lista.append(num)
lista = lista[::-1]
print("".join(lista))