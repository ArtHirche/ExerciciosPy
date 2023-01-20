num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1%10
d = num // 10%10
c = num // 100%10
m = num // 1000%10
print(f'A milhar do seu número será: {m}\nA centena será: {c}\nA dezena será: {d}\nA unidade será: {u}')
#Correto!