hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

if hora_inicial < hora_final or (hora_inicial == hora_final and minuto_inicial < minuto_final):
    horas = hora_final - hora_inicial
    minutos = minuto_final - minuto_inicial

elif hora_inicial == hora_final and minuto_inicial == minuto_final:
    horas = 24
    minutos = 0

else:
    horas = (24 - hora_inicial) + hora_final
    minutos = minuto_final - minuto_inicial

if minutos < 0:
    minutos += 60
    horas -= 1

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
