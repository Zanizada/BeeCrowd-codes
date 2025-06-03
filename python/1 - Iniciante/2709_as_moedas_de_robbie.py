while True:
    try:
        qntd_moedas = int(input())
        moedas = []
        for i in range(qntd_moedas):
            valor = int(input())
            moedas.append(valor)
        salto = int(input())

        soma = 0
        indice = 0
        while indice < qntd_moedas:
            soma += moedas[indice]
            indice += salto

        primo = True
        for divisor in range(2, soma):
            if soma % divisor == 0:
                primo = False
                break

        if primo == True:
            resultado = "You’re a coastal aircraft, Robbie, a large silver aircraft."
        else:
            resultado = "Bad boy! I’ll hit you."

        print(resultado)

    except EOFError:
        break