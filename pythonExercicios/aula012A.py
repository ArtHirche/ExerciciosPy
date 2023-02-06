#PRÁTICA
nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Arthur':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')

"""
TEORIA:
Nem sempre será só Se ou Senão (if ou else).
Nesse caso, usamos o Senão Se (elif).

Exemplo:
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.direita()
else:
    carro.siga()
carro.pare()
OBS: Você pode usar dentro do if quantos elif quiser.
"""