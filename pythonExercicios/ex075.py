valores = (int(input('Digite um número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))
print(f'Os valores digitados foram: {valores}.')
print(f'O número 9 (nove) apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'O número 3 (três) apareceu na {valores.index(3)+1}ª posição.')
else:
    print('O número 3 (três) não foi digitado.')
print('Os números pares foram: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
