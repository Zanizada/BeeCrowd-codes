def definirSetor(setor):
    if setor > 0 and setor < 5:
        if setor == 1:
            return 'Rolien'
        elif setor == 2:
            return 'Naej'
        elif setor == 3:
            return 'Elehcim'
        else:
            return 'Odranoel'

N = int(input())
        
for i in range(N):
    K = int(input())

    for i in range(K):
        feedbacks = int(input())
        setor = definirSetor(feedbacks)
        print(setor)
