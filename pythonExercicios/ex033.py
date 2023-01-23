num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 == num2 == num3:
    print('Os três números são IGUAIS!')
elif num1 >= num2 and num1 >= num3 and num2 <= num3:
    print(f'{num1} é o MAIOR número!\n{num2} é o MENOR número')
elif num1 >= num2 and num1 >= num3 and num3 <= num2:
    print(f'{num1} é o MAIOR número!\n{num3} é o MENOR número!')
elif num2 >= num1 and num2 >= num3 and num1 <= num3:
    print(f'{num2} é o MAIOR número!\n{num1} é o MENOR número!')
elif num2 >= num1 and num2 >= num3 and num3 <= num1:
    print(f'{num2} é o MAIOR número!\n{num3} é o MENOR número!')
elif num3 >= num1 and num3 >= num2 and num1 <= num2:
    print(f'{num3} é o MAIOR número!\n{num1} é o MENOR número!')
elif num3 >= num1 and num3 >= num2 and num2 <= num1:
    print(f'{num3} é o MAIOR número!\n{num2} é o MENOR número!')
