from random import choice
nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = choice(lista)
print(f'Entre os alunos {nome1}, {nome2}, {nome3} e {nome4}, irá limpar o quadro o {sorteado}.')
