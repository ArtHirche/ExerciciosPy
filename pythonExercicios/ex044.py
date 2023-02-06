preco = float(input('Qual o preço do produto? R$ '))
condicao = int(input("""Como pretende pagar?
Digite 1 para à vista no dinheiro/cheque
Digite 2 para à vista no cartão
Digite 3 para em até 2x no cartão
Digite 4 para em até 3x no cartão
Digite aqui: """))
descontoDez = preco*(10/100)
vistaDinheiroCheque = preco-descontoDez
descontoCinco = preco*(5/100)
vistaCartao = preco-descontoCinco
doisxCartao = preco/2
jurosVinte = preco*(20/100)
tresxCartao = preco+jurosVinte
if condicao == 1:
    print(f'Você pagará R$ {vistaDinheiroCheque:.2f}')
elif condicao == 2:
    print(f'Você pagará R$ {vistaCartao:.2f}')
elif condicao == 3:
    print(f'Você pagará 2 vezes de R$ {doisxCartao:.2f}')
elif condicao == 4:
    print(f'Você pagará R$ {tresxCartao:.2f}')
else:
    print('Opção não encontrada, reinicie o programa.')
