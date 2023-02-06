from random import choice
jogador = int(input("""Digite 1 para PEDRA
Digite 2 para PAPEL
Digite 3 para TESOURA
Digite aqui: """))
jokempo = ['PEDRA', 'PAPEL', 'TESOURA']
maquina = choice(jokempo)
cores = '\033[1;31mmáquina', '\033[1;32mVocê', '\033[1;33mEMPATOU'
print(f'A máquina escolheu {maquina}')
if jogador == 1 and maquina == 'PEDRA':
    print('EMPATE!')
elif jogador == 1 and maquina == 'PAPEL':
    print('A máquina ganhou!')
elif jogador == 1 and maquina == 'TESOURA':
    print('Você ganhou!')
elif jogador == 2 and maquina == 'PEDRA':
    print('Você ganhou!')
elif jogador == 2 and maquina == 'PAPEL':
    print('EMPATOU!')
elif jogador == 2 and maquina == 'TESOURA':
    print('A máquina ganhou!')
elif jogador == 3 and maquina == 'PEDRA':
    print('A máquina ganhou!')
elif jogador == 3 and maquina == 'PAPEL':
    print('Você ganhou!')
elif jogador == 3 and maquina == 'TESOURA':
    print('EMPATOU!')
else:
    print('Desculpe, não entendi! Reinicie o programa. NÃO ESQUEÇA:\nDigite 1 para PEDRA\n 2 para PAPEL\n 3 para TESOURA')
