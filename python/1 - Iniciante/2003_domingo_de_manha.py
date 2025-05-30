while True:
    try:
        horas, minutos = map(int, input().split(":"))
        if horas >= 7:
            if 0 < minutos < 60:
                print(f"Atraso maximo: {minutos}")
            else:
                print(f"Atraso maximo: 0")
    except EOFError:
        break