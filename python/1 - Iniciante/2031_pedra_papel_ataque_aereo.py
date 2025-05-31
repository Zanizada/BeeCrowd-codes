casos_teste = int(input())

jokenpo = {
    "ataque": ["pedra", "papel"],
    "pedra": ["papel"],
}

for i in range(casos_teste):
    jogador_um = input()
    jogador_dois = input()

    if jogador_um in jokenpo[jogador_dois]:
        resultado = "Jogador 2 venceu"
    elif jogador_dois in jokenpo[jogador_um]:
        resultado = "Jogador 1 venceu"
    elif jogador_um == jogador_dois:
        if jogador_um == "papel":
            resultado = "Ambos venceram"
        elif jogador_um == "pedra":
            resultado = "Sem ganhador"
        elif jogador_um == "ataque":
            resultado = "Aniquilacao mutua"
    
    print(resultado)