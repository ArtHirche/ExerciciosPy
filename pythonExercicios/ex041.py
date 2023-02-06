anoNascimento = int(input('Em que ano você nasceu? '))
idade = 2023-anoNascimento
if idade <= 9:
    print('Atleta \033[1mMIRIM\033[m!')
elif idade <= 14:
    print('Atleta \033[1mINFANTIL\033[m!')
elif idade <= 19:
    print('Atleta \033[1mJUNIOR\033[m!')
elif idade == 20:
    print('Atleta \033[1mSÊNIOR\033[m!')
else:
    print('Atleta \033[1mMASTER\033[m!')
