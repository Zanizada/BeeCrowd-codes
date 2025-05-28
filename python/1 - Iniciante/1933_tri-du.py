primeiraCarta, segundaCarta = map(int, input().split())

if primeiraCarta == segundaCarta:
    terceiraCarta = primeiraCarta
elif primeiraCarta < segundaCarta:
    terceiraCarta = segundaCarta
else:
    terceiraCarta = primeiraCarta

print(terceiraCarta)