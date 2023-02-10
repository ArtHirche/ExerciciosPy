soma = 0
for c in range(0, 6):
    valor = int(input(('Digite um valor: ')))
    par = valor % 2
    if par == 0:
        soma += valor
print(f'A soma dos pares é: {soma}.')
