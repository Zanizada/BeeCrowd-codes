def numero_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def proximo_primo(atual):
    candidato = atual + 1
    while True:
        if numero_primo(candidato):
            return candidato
        candidato += 1

def primo_josephus(qntd_pessoas):
    pessoas = list(range(1, qntd_pessoas + 1))
    indice = 0
    salto = 2  # primeiro primo
    while len(pessoas) > 1:
        indice = (indice + salto - 1) % len(pessoas)
        pessoas.pop(indice)
        salto = proximo_primo(salto)
    return pessoas[0]

while True:
    qntd_pessoas = int(input())

    if qntd_pessoas == 0:
        break
    else:
        pass
    
    print(primo_josephus(qntd_pessoas))