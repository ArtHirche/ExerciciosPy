from random import randint
num = int(input('Digite o número do seu palpite: '))
pc = randint(0, 5)
print(f'O número escolhido pela máquina foi {pc}')
if num == pc:
    print('VOCÊ ADIVINHOU! XD')
else:
    print('VOCÊ NÃO ADIVINHOU! :(')
print('---FIM DE JOGO---')