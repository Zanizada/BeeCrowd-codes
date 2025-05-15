def josephus(qntd_pessoas, salto):
    sobreviventes = list(range(1, qntd_pessoas + 1))
    sobrevivente = 0

    while len(sobreviventes) > 1:
        sobrevivente = (sobrevivente + salto - 1) % len(sobreviventes)
        del sobreviventes[sobrevivente]

    return sobreviventes[0]

def verif_num_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

while True:
    qntd_pessoas = int(input())
    if qntd_pessoas == 0:
        break

    salto = 1
    while True:
        if verif_num_primo(salto):
            resultado = josephus(qntd_pessoas, salto)
            if resultado == 1:
                print(salto)
                break
        salto += 1
