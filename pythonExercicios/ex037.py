número = int(input('Digite o número à ser analisado: '))
conversão = int(input("""Em qual análise você deseja fazer para o número:\n
Digite 1 para \033[1mBinário\033[m\n
Digite 2 para \033[1mOctal\033[m\n
Digite 3 para \033[1mHexadecimal\033[m\n
Digite aqui: """))
if conversão == 1:
    print(f'O número digitado em binário é: {(bin(número))}')
elif conversão == 2:
    print(f'O número digitado em octal é: {(oct(número))}')
elif conversão == 3:
    print(f'O número digitado em hexadecimal é: {(hex(número))}')
else:
    print('Opção inexistente, reinicie o programa.')
