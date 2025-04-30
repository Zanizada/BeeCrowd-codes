def criptografia(texto):
    for caractere in texto:
        # Primeira passada
        unidade = ord(caractere)
        unidadeCripto = chr(unidade + 3)
        caracteres = []
        caracteres.append(unidadeCripto)
        # Segunda passada
        caracteres.reverse()
        # Terceira passada
        metadeInicial = len(caracteres) // 2
        segundaMetade = caracteres[metadeInicial:]
        for caractere in segundaMetade:
            unidade = ord(caractere)
            unidadeCripto = chr(unidade - 1)
            segundaMetade2 = []
            segundaMetade2.append(unidadeCripto)
        # Junção
        memns = "".join(metadeInicial, segundaMetade2)
        return caracteres

casosTeste = int(input())

for i in range(casosTeste):
    texto = input()
    criptografia(texto)
    print(caracteres)
