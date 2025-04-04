grenais = 0
vitorias = 0
derrotas = 0
empates = 0

while True:
    INT, GRE = map(int, input().split())
    grenais += 1
    
    if INT > GRE:
        vitorias += 1
    elif INT < GRE:
        derrotas += 1
    else:
        empates += 1
    
    while True:
        a = int(input('Novo grenal (1-sim 2-nao)\n'))
        if a == 1:
            break
        elif a == 2:

            print(f'{grenais} grenais')
            print(f'Inter:{vitorias}')
            print(f'Gremio:{derrotas}')
            print(f'Empates:{empates}')
            
            if vitorias > derrotas:
                print('Inter venceu mais')
            elif vitorias < derrotas:
                print('Gremio venceu mais')
            else:
                print('Nao houve vencedor')
            exit()
