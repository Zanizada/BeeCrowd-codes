N = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

centavos = int(round(N * 100))

print('NOTAS:')
for nota in notas:
    valor_nota = int(nota * 100)
    qntd_notas = centavos // valor_nota
    print(f'{qntd_notas} nota(s) de R$ {nota:.2f}')
    centavos %= valor_nota

print('MOEDAS:')
for moeda in moedas:
    valor_moeda = int(moeda * 100)
    qntd_moedas = centavos // valor_moeda
    print(f'{qntd_moedas} moeda(s) de R$ {moeda:.2f}')
    centavos %= valor_moeda
