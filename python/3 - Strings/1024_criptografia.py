def criptografia(texto):
    caracteres = []

    # Primeira passada
    
    for str in texto:

        unidade = ord(str)
        unidadeCripto = chr(unidade + 3)
        caracteres.append(unidadeCripto)

    # Segunda passada

    caracteres.reverse()

    # Terceira passada

    metadeInicial = len(caracteres) // 2
    for i in range(metadeInicial, len(caracteres)):
        caracteres[i] = chr(ord(caracteres[i]) - 1)

    # Finalização
    
    mensagem = "".join(caracteres)
    return mensagem

casosTeste = int(input())

for _ in range(casosTeste):
    texto = input()
    mensagemCriptografada = criptografia(texto)
    
    print(mensagemCriptografada)
