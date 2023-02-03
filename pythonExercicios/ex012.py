preço = float(input('Qual o preço do produto? $ '))
desconto = preço*(5/100)
total = preço-desconto
print(f'O seu desconto será de $ \033[1;31m{desconto:.2f}\033[m! Totalizando $ \033[1;4;32m{total:.2f}\033[m!')
#Correto!