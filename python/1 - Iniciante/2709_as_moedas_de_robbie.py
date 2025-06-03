import math

while True:
    try:
        qntd_moedas = int(input())
        moedas = []
        for i in range(qntd_moedas):
            valor = int(input())
            moedas.append(valor)
        salto = int(input())

        soma = 0
        indice = qntd_moedas - 1
        while indice >= 0:
            soma += moedas[indice]
            indice -= salto

        primo = True
        if soma < 2:
            primo = False
        else:
            for divisor in range(2, int(math.sqrt(soma)) + 1):
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