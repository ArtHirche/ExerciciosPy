#PRÁTICA:
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
for contador in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[contador]}')
print('Comi pra caramba!')
"""
TEORIA:
lanche = hamburguer
lanche = suco
Já tem uma atribuição, logo, o Python elimina a primeira variavel.
E se quiser mais atribuições?
Sim! As variaveis compostas.

Existem 3 tipos:
Tuplas;
Listas;
Dicionários.

Tuplas:
Hamburguer (0)
Suco (1)
Pizza (2)
Pudim (3)
Cada atribuição recebe um índice: 0, 1, 2, 3...

Exemplos:
print(lanche[2])
Retornará: Pizza

print(lanche[0:2])
Retornará: Hamburguer, Suco

print(lanche[1:])
Retornará: Suco, Pizza, Pudim

print(lanche[-1])
Retornará: Pudim

len(lanche)
Retornará: 4

for c in lanche:
    print(c)
Retornará: Hamburguer, Suco, Pizza, Pudim

As tuplas são IMUTÁVEIS!!!
"""