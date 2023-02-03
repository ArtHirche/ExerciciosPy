nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print(f'Prazer em conhecê-lo \033[1;4m{nome}\033[m!\nSeu primeiro nome: \033[1;34m{nome_separado[0]}\033[m\nSeu último nome: \033[1;36m{nome_separado[len(nome_separado)-1]}\033[m')
