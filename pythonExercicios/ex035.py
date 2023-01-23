reta1 = float(input('Qual o tamanho da primeira reta? '))
reta2 = float(input('Qual o tamanho da segunda reta? '))
reta3 = float(input('Qual o tamanho da segunda reta? '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('É possível fazer um triângulo!')
else:
    print('Não é possível fazer um triângulo!')
