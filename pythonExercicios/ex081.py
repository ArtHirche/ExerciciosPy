num = []
while True:
    num.append(int(input('Digite um número inteiro: ')))
    restart = str(input('Deseja prosseguir? (S/N) '))
    if restart in 'Nn':
        break
print(f'Você digitou {len(num)} valores.')
num.sort(reverse=True)
print(f'Os valores em ordem \033[1mdecrescente\033[m são: {num}')
if 5 in num:
    print('O número 5 está na lista!')
else:
    print('Não encontrei o número 5 na lista!')