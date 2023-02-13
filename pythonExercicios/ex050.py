soma = 0
contador = 0
for c in range(1, 7):
    valor = int(input((f'Digite o {c}º valor: ')))
    if valor % 2 == 0:
        soma += valor
        contador += 1
print(f'A soma dos pares informados ({contador}) é: {soma}.')
