casos = int(input())

for i in range(casos):
    hora, minuto, ocorrencia = map(int, input().split())

    if ocorrencia == 1:
        porta = "A porta abriu!"
    elif ocorrencia == 0:
        porta = "A porta fechou!"