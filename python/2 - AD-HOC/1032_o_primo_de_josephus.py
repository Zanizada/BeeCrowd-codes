def josephus(qntd_pessoas, salto):
    sobreviventes = list(range(1, qntd_pessoas + 1))
    indice = 0

    while len(sobreviventes) > 1:
        indice = (indice + salto - 1) % len(sobreviventes)
        del sobreviventes[indice]

    return sobreviventes[0]

def numero_primo(numero):
    