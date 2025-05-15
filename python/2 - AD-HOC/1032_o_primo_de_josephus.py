def josephus(qntd_pessoas, salto):
    sobreviventes = list(range(1, qntd_pessoas + 1))
    sobrevivente = 0

    while len(sobreviventes) > 1:
        sobrevivente = (sobrevivente + salto - 1) % len(sobreviventes)
        del sobreviventes[sobrevivente]

    return sobreviventes[0]