l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
m = l * a
t = m / 2
print(f'Sua parede tem a dimensão de \033[1;31m{l}\033[mx\033[1;33m{a}\033[m e sua área é de \033[1;34m{m}\033[mm².\nPara pintar essa parede, você precisará de \033[1;4;35m{t:.2f}\033[mL de tinta. ')
#Correto!