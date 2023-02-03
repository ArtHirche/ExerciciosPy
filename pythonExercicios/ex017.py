from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'O valor da hipotenusa será: \033[1;4;32m{hi:.2f}\033[m')
#Correto!