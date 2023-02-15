from time import sleep

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('=-=='*7)
opcao = 0
while opcao != 5:
    print(
        '[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] FINALIZAR PROGRAMA'
    )
    opcao = int(input('Qual sua opção?\nDIGITE AQUI: '))
    print('=-=='*7)
    if opcao == 1:
        soma = num1+num2
        print(f'A soma entre {num1} e {num2} é {soma}.')
        print('=-=='*7)
    elif opcao == 2:
        multiplica = num1*num2
        print(f'A multiplicação entre {num1} e {num2} é {multiplica}')
        print('=-=='*7)
    elif opcao == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que o número {num2}')
        if num2 > num1:
            print(f'O número {num2} é maior que o número {num1}')
        print('=-=='*7)
        if num1 == num2:
            print(f'Os números {num1} e {num2} são iguais.')
    elif opcao == 4:
        print('Informe os novos números: ')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        print('=-=='*7)
    elif opcao == 0 or opcao > 5:
        print('Opção invalida. Tente novamente.')
        print('=-=='*7)
print('Finalizando...')
sleep(5)
print('Fim do programa!')
