from random import randint


def determinaVitoria(jogador1, maquina):
    if jogador1 == maquina:
        print('EMPATOU!')
    elif jogador1 == 2 and maquina == 1:
        print('Você ganhou!')
    elif jogador1 == 3 and maquina == 2:
        print('Você ganhou!')
    elif jogador1 == 1 and maquina == 3:
        print('Você ganhou!')
    else:
        print('A máquina ganhou!')


def iniciaJogo():
    restart = ""

    jokempo = {1: 'PEDRA', 2: 'PAPEL', 3: 'TESOURA'}
    while restart == "":
        jogador = input(
            "Digite 1 para PEDRA\nDigite 2 para PAPEL\nDigite 3 para TESOURA\nDigite aqui: "
        )

        if jogador.isnumeric() and int(jogador) <= 3:

            maquina = randint(1, 3)

            print(f'A máquina escolheu {jokempo[maquina]}')
            determinaVitoria(int(jogador), maquina)
        else:
            print(
                'Desculpe, não entendi! Reinicie o programa. NÃO ESQUEÇA:\nDigite 1 para PEDRA\n2 para PAPEL\n3 para TESOURA'
            )
        restart = input('Pressione Enter para continuar.')


iniciaJogo()
