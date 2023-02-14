sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Invalidado! Digite seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} validado com sucesso!')
