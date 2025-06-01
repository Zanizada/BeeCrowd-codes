escolha, numero_um, numero_dois, roubou, acusou = map(int, input().split())

par_ou_impar = {
    1: "par",
    0: "impar"
}

escolha = par_ou_impar[escolha]
soma = numero_um + numero_dois

if roubou == 1 and acusou == 1:
    resultado = "Jogador 2 ganha!"
elif roubou == 1 and acusou == 0:
    resultado = "Jogador 1 ganha!"
else:
    if soma % 2 != 0:
        if escolha == "impar":
            resultado = "Jogador 1 ganha!"
        else:
            resultado = "Jogador 2 ganha!"
    else:
        if escolha == "par":
            resultado = "Jogador 1 ganha!"
        else:
            resultado = "Jogador 2 ganha!"

print(resultado)