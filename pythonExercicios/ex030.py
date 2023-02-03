num = int(input('Digite um número: '))
impar_par = num%2
if impar_par == 0:
    print('O número escolhido é \033[36mPAR\033[m')
else:
    print('O número escolhido é \033[31mIMPAR\033[m')
