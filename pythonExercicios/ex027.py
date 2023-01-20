nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print(f'Prazer em conhecê-lo {nome}!\nSeu primeiro nome: {nome_separado[0]}\nSeu último nome: {nome_separado[len(nome_separado)-1]}')
