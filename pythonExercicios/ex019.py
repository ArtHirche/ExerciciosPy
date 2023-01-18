import random
nome1 = str('Pedro')
nome2 = str('Henrico')
nome3 = str('Arthur')
nome4 = str('Gustavo')
sorteio = random.random(nome1, nome2, nome3, nome4)
print(f'Entre os alunos {nome1}, {nome2}, {nome3} e {nome4}, irá limpar o quadro o {sorteio}.')
