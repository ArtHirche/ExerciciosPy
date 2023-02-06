num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
if num1 > num2:
    print(f'O número {num1} é maior que {num2}.')
elif num2 > num1:
    print(f'O número {num2} é maior que {num1}.')
else:
    print('Não existe valor maior, os dois são iguais.')
