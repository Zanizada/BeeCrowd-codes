def josephus(qntd_pessoas, salto):
    sobreviventes = list(range(1, qntd_pessoas + 1))
    sobrevivente = 0

    while len(sobreviventes) > 1:
        sobrevivente = (sobrevivente + salto - 1) % len(sobreviventes)
        del sobreviventes[sobrevivente]

    return sobreviventes[0]

def verif_num_primo(numero):
    if numero > 1:
        if numero % 1 == 0 and numero % numero == 0:
            return True
        else:
            return False
    else:
        return False

