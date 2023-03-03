listagemPrecos = ('Dell G15-i1200', 4800, 'Monitor', 1340.9, 'Caderno', 15.9,
                  'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
for pos in range(0, len(listagemPrecos)):
    if pos % 2 == 0:
        print(f'{listagemPrecos[pos]:.<30}', end='')
    else:
        print(f' R$ {listagemPrecos[pos]:>7.2f}')
