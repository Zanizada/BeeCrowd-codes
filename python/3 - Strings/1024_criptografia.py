def criptografia(texto):
    caracteres = []
    # Passada 1
    for caractere in texto:
        if caractere.isalpha():
            unidade = ord(caractere)
            unidadeCripto = chr(unidade + 3)
            caracteres.append(unidadeCripto)
        else:
            caracteres.append(caractere)
    # Passada 2
    caracteres = caracteres[::-1]
    # Passada 3
    primeiraMetade = caracteres[:len(caracteres)//2]
    segundaMetade = caracteres[len(caracteres)//2:]
    metadeCripto = []
    for caractere in segundaMetade:
        unidade = ord(caractere)
        unidadeCripto = chr(unidade - 1)
        metadeCripto.append(unidadeCripto)
    # Conclusão
    caracteres = primeiraMetade + metadeCripto
    mensagemCriptografada = "".join(caracteres)
    return mensagemCriptografada
    
testes = int(input())
for i in range(testes):
    mensagem = input()
    print(criptografia(mensagem))