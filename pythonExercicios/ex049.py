numero = int(input('Digite um valor: '))
print('-=' * 12)
for c in range(0, 11):
    multiplicacao = numero * c
    print(numero, 'x', c, '=', multiplicacao)
print('-=' * 12)
print('FIM DA TABUADA!')