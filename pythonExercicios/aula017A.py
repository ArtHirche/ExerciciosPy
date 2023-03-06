#PRÁTICA:
num = list()
for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
if '5' in num:
    num.remove(5)
else:
    print('Não achei o número 5.')
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')
print(f'Essa lista tem {len(num)} valores.')
"""
TEORIA:
Listas:
Tuplas ()
Listas []

lanche = ['hambúrguer', 'suco', 'pizza', pudim]
lanche[3] = 'picolé'
Nesse caso, a lista substituirá o pudim e colocará picolé. Diferente das tuplas, listas podem sofrer alterações.

- lanche.append('cookie')
Você pode adicionar coisas no final da lista.

- lanche.insert(0, hotdog)
Você pode adicionar coisas na lista em qualquer posição.

- del lanche[3]
- lanche.pop()
- lanche.remove('pizza')
Você pode eliminar qualquer coisa da lista.

- if 'pizza' in lanche:
      lanche.remove('pizza')
Você pode eliminar qualquer coisa da lista depois de verificar se há essa coisa na lista com o if.

- valores = list(range(4, 11))
Você pode criar uma variável como lista com o list e range.

valores = [8, 2, 5, 4, 9, 3, 0]
- valores.sort()
- valores.sort(reverse = True)
Você pode organizar uma lista usando o sort.

- len(valores)
Você pode ler quantos elementos têm em uma lista.

- a = [2, 3, 4, 7]
b = a[:]
Você pode criar uma cópia da lista.
"""