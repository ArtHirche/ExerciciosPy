velocidade = float(input('Qual era a velocidade do carro? '))
multa = (velocidade-80)*7
if velocidade > 80.0:
    print('Você estava acima da velocidade permitida e será multado.')
    print(f'Sua multa será de: R$ {multa:.2f}.')
else:
    print('Você estava dentro da velocidade máxima permitida!')
