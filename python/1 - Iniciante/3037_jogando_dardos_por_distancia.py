N = int(input())
arremessosJoao = 0
arremessosMaria = 0

for i in range(N):
    for arremessos in range(6):

        for arremessosJ in range(3):
            X, D = map(int, input().split())
            arremessosJoao += X
        for arremessosM in range(3):
            X, D = map(int, input().split())
            arremessosMaria += X

        if arremessosJoao > arremessosMaria:
            vitoria = 'JOAO'
        elif arremessosJoao < arremessosMaria:
               qvitoria = 'MARIA'
        print(vitoria)
