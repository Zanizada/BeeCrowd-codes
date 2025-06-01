escolha, numero_um, numero_dois, roubou, acusou = map(int, input().split())

par_ou_impar = {
    1: "par",
    0: "impar"
}

escolha = par_ou_impar[escolha]

if roubou == 1 and acusou == 1:
    resultado = "Jogador 2 ganha!"