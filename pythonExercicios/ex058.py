from random import randint

maquina = randint(0, 10)
jogador = tentativas = 0
print('Olá, sou o seu computador... Não se assuste, só quero jogar um jogo de adivinhação! Estou pensando em um número entre 0 e 10, consegue adivinhar qual é?')
while jogador != maquina:
    jogador = int(input('Digite o número do seu palpite entre 0 e 10: '))
    tentativas += 1
    if jogador != maquina:
        print('\033[1;31mVOCÊ NÃO ADIVINHOU! :(\033[m')
    else:
        print('\033[1;32mVOCÊ ADIVINHOU! XD\033[m')
print(f'O número escolhido pela máquina foi: {maquina}')
print(f'\033[1m---FIM DE JOGO---\033[m\nForam necessárias {tentativas} para acertar.')
