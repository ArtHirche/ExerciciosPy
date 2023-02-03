num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10
print(f'A milhar do seu número será: \033[31m{m}\033[m\nA centena será: \033[34m{c}\033[m\nA dezena será: \033[32m{d}\033[m\nA unidade será: \033[33m{u}\033[m')
#Correto!