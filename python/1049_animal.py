A = input()
B = input()
C = input()

if A == 'vertebrado':
    if B == 'ave':
        if C == 'carnivoro':
            print(f'aguia')
        else:
            print(f'pomba')
    else:
        if C == 'onivoro':
            print(f'homem')
        else:
            print(f'vaca')
else:
    if B == 'inseto':
        if C == 'hematofago':
            print(f'pulga')
        else:
            print(f'lagarta')
    else:
        if C == 'hematofago':
            print(f'sanguessuga')
        else:
            print(f'minhoca')
