while True:
    try:
        dias_por_mes = {
            1: 31, 2: 29,
            3: 31, 4: 30,
            5: 31, 6: 30,
            7: 31, 8: 31,
            9: 30, 10: 31,
            11: 30, 12: 31
        }

        mes, dia = map(int, input().split())

        if mes == 12 and dia > 25:
            dias_restantes = "Ja passou!"
        else:
            dias = 0
            for meses in range(1, mes):
                dias += dias_por_mes[meses]
            dias += dia
            
            if dias == 359:
                dias_restantes = "E vespera de natal!"
            elif dias == 360:
                dias_restantes = "E natal!"
            else:
                dias_restantes = f"Faltam {360 - dias} dias para o natal!"

        print(dias_restantes)

    except EOFError:
        break
