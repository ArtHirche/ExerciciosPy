#PRÁTICA:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}.')
print('PARABÉNS' if m >=6.0 else 'ESTUDE MAIS')

"""
TEORIA:
Exemplo do carro na estrada:
carro.siga() == vai em frente
carro.esquerda() == vire para a esquerda
carro.direita() == vire para a direita
carro.pare() == para o carro
São SEQUENCIAIS!

Condicionais:
carro.siga():
se carro.esquerda()
   carro.siga()
   carro.direita()
   carro.siga()
   carro.direita()
   carro.esquerda()
   carro.siga()
   carro.direita()
   carro.siga()
senão:
   carro.siga()
   carro.esquerda()
   carro.siga()
   carro.esquerda()
   carro.siga()
carro.pare()

Condição:
se carro.esquerda():
   bloco_V_
senão:
    bloco_F_
OU SEJA:
if carro.esquerda():
    bloco_True_
else:
    bloco_False_

Exemplos:
1)
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')
2)
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')
"""