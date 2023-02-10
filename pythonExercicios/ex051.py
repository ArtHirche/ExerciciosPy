valor = int(input('Digite o valor: '))
razao = int(input('Digite a razão: '))
l = [valor]
v = 0
for c in range(1, 10):
    v = valor + razao * c
    l.append(v)
print(f'Os 10 primeiros valores da progreção são {l}')
