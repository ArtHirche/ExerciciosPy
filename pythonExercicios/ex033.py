num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
if num1 == num2 == num3:
    print('Os três números são IGUAIS!')
elif num1 >= num2 and num1 >= num3 and num2 <= num3:
    print(f'\033[1;33m{num1}\033[m é o MAIOR número!\n\033[1;36m{num2}\033[m é o MENOR número')
elif num1 >= num2 and num1 >= num3 and num3 <= num2:
    print(f'\033[1;33m{num1}\033[m é o MAIOR número!\n\033[1;31m{num3}\033 é o MENOR número!')
elif num2 >= num1 and num2 >= num3 and num1 <= num3:
    print(f'\033[1;36m{num2}\033[m é o MAIOR número!\n\033[1;33m{num1}\033[m é o MENOR número!')
elif num2 >= num1 and num2 >= num3 and num3 <= num1:
    print(f'\033[1;36m{num2}\033[m é o MAIOR número!\n\033[1;31m{num3}\033[m é o MENOR número!')
elif num3 >= num1 and num3 >= num2 and num1 <= num2:
    print(f'\033[1;31m{num3}\033[m é o MAIOR número!\n\033[1;33m{num1}\033[m é o MENOR número!')
elif num3 >= num1 and num3 >= num2 and num2 <= num1:
    print(f'\033[1;31m{num3}\033[m é o MAIOR número!\n\033[1;36m{num2}\033[m é o MENOR número!')
