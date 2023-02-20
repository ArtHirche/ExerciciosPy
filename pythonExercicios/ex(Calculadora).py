from os import system
from time import sleep

num1 = int(input('Digite o primeiro valor: '))
resto = num1 % 2
opcao = 0
while opcao != 9:
    print('Digite a operação desejada:\n(1) SOMAR\n(2) SUBTRAIR\n(3) DIVIDAR\n(4) MULTIPLICAR\n(5) RAIZ\n(6) POTÊNCIA\n(7) PAR OU IMPAR\n(8) NOVO NÚMERO\n(9) FINALIZAR')
    opcao = int(input('Digite aqui a operação: '))
    system('cls')
    if opcao == 1:
        num2 = int(input('Digite o valor da soma: '))
        print(f'A soma será {num1+num2}')
    elif opcao == 2:
        num2 = int(input('Digite o valor da subtração: '))
        print(f'A subtração será {num1-num2}')
    elif opcao == 3:
        num2 = int(input('Digite o valor da divisão: '))
        print(f'A divisão será {num1/num2:.2f}')
    elif opcao == 4:
        num2 = int(input('Digite o valor da multiplicação: '))
        print(f'A multiplicação será {num1*num2}')
    elif opcao == 5:
            raiz = int(input('Digite o valor da raiz: '))
            print(f'A raiz {raiz} de {num1} será {num1**(1/raiz)}')
    elif opcao == 6:
        num2 = int(input('Digite o valor do expoente: '))
        print(f'A base escolhida foi {num1}, o expoente foi {num2}, a potência será: {num1**num2}')
    elif opcao == 7:
        if resto == 0:
            print(f'O número {num1} é par')
        else:
            print(f'O número {num1} é impar')
    elif opcao == 8:
        print('Tudo bem.')
        num1 = int(input('Digite o novo valor aqui: '))
    elif opcao == 0 or opcao > 9:
        print('Não entendi. Digite a operação de novo.')
print('Ok. Finalizando...')
sleep(1)
print('Programa finalizado. Obrigado pela preferência!')
