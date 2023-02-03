from random import choice
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = choice(lista)
print(f'Entre os alunos \033[1;4;30m{nome1}\033[m, \033[1;4;32m{nome2}\033[m, \033[1;4;35m{nome3}\033[m e \033[1;4;36m{nome4}\033[m, irá limpar o quadro o \033[1;4;34m{sorteado}\033[m.')
