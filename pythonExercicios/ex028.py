from random import randint
num = int(input('Digite o número do seu palpite: '))
máquina = randint(0, 5)
print(f'O número escolhido pela máquina foi: {máquina}')
if num == máquina:
    print('\033[1;32mVOCÊ ADIVINHOU! XD\033[m')
else:
    print('\033[1;31mVOCÊ NÃO ADIVINHOU! :(\033[m')
print('\033[1m---FIM DE JOGO---\033[m')