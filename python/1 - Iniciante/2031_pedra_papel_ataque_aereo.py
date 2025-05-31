casos_teste = int(input())

for _ in range(casos_teste):
    jogador_um = input()
    jogador_dois = input()

    if jogador_um == jogador_dois:
        if jogador_um == "ataque":
            resultado = "Aniquilacao mutua"
        elif jogador_um == "pedra":
            resultado = "Sem ganhador"
        elif jogador_um == "papel":
            resultado = "Ambos venceram"
    elif jogador_um == "ataque":
        resultado = "Jogador 1 venceu"
    elif jogador_dois == "ataque":
        resultado = "Jogador 2 venceu"
    elif jogador_um == "pedra" and jogador_dois == "papel":
        resultado = "Jogador 1 venceu"
    elif jogador_dois == "pedra" and jogador_um == "papel":
        resultado = "Jogador 2 venceu"

    print(resultado)
