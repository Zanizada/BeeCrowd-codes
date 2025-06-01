escolha, numero_um, numero_dois, roubou, acusou = map(int, input().split())
soma = numero_um + numero_dois

if roubou == 1 and acusou == 1:
    resultado = "Jogador 2 ganha!"
elif roubou == 1 and acusou == 0:
    resultado = "Jogador 1 ganha!"
else:
    resultado = (
        "Jogador 1 ganha!" if soma % 2 == 0 else "Jogador 2 ganha!"
        ) if escolha == 1 else (
        "Jogador 2 ganha!" if soma % 2 == 0 else "Jogador 1 ganha!"
        )

print(resultado)