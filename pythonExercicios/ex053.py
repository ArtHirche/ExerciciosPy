frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print(f'A frase "{frase}" é um palíndromo!')
else:
    print(f'A frase "{frase}" não é um palíndromo!')