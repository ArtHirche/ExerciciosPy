nome = str(input('Digite seu nome inteiro: ')).strip()
verificador = 'Silva' in nome.title()
print(f'Seu nome tem "Silva"? \033[1;4m{verificador}\033[m')
#Correto!