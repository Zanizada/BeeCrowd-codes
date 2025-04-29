def definirSetor(setor):
    if setor > 0 and setor < 5:
        if setor == 1:
            setor = 'Rolien'
        elif setor == 2:
            setor = 'Naej'
        elif setor == 3:
            setor = 'Elehcim'
        else:
            setor = 'Odranoel'

    return setor

N = int(input())
        
for i in range(N):
    K = int(input())

    for i in range(K):
        feedbacks = int(input())
        definirSetor(feedbacks)
        print(f'{setor}')
