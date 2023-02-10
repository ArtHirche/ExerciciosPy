frase = str(input('Digite uma frase: ')).strip
frase = frase.replace(' ', '')
frase_lista_n = []
frase_lista_r = []
for c in range(0, len(frase)):
    frase_lista_n.append(frase[c])
print(f'A frase em ordem normal é: "{frase_lista_n}"')
for c in range(len(frase) - 1, -1, -1):
    frase_lista_r.append(frase[c])
print(f'A frase reversa é: "{frase_lista_r}"')
if frase_lista_n == frase_lista_r:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
