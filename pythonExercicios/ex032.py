ano = int(input('Digite um ano: '))
bi1 = ano%4
bi2 = ano%100
bi3 = ano%400
if bi1 == 0 and bi2 != 0:
    print(f'{ano} é um ano bissexto.')
elif bi1 == 0 and bi2 == 0 and bi3 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
