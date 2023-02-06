reta1 = float(input('Qual o tamanho da primeira reta? '))
reta2 = float(input('Qual o tamanho da segunda reta? '))
reta3 = float(input('Qual o tamanho da terceira reta? '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('\033[1;32mÉ possível fazer um triângulo!\033[m')
    if reta1 == reta2 == reta3:
        print('É um triângulo equilátero.')
    elif reta1 == reta2 != reta3 or reta1 == reta3 != reta2:
        print('É um triângulo isósceles.')
    else:
        print('É um triângulo escaleno.')
else:
    print('\033[1;31mNão é possível fazer um triângulo!\033[m')
