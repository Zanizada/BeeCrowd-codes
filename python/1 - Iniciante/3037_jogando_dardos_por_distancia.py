N = int(input())
arremessosJoao = 0
arremessosMaria = 0

for i in range(N):
    arremessosJoao = 0
    arremessosMaria = 0

    for arremessosJ in range(3):
        X, D = map(int, input().split())
        arremessosJoao += X * D
        
    for arremessosM in range(3):
        X, D = map(int, input().split())
        arremessosMaria += X * D

    if arremessosJoao > arremessosMaria:
        vitoria = 'JOAO'
        
    elif arremessosJoao < arremessosMaria:
        vitoria = 'MARIA'

    print(vitoria)
