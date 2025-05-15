def josephus(qntd_pessoas, salto):
    sobreviventes = list(range(1, qntd_pessoas + 1))
    indice = 0

    while len(sobreviventes) > 1:
        indice = (indice + salto - 1) % len(sobreviventes)
        del sobreviventes[indice]

    return sobreviventes[0]

def numero_primo(numero):
    if numero > 1:
        for divisor in range(2, numero):
            if numero % divisor != 0:
                return True
            else:
                return False
    else:
        return False
    
numeros = list(input().split())
for num in numeros:
    num = int(num)
    primo = numero_primo(num)
    if primo == True:
        print(num)
    else:
        pass