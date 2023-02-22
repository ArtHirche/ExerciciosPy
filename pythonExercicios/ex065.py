resposta = 'S'
soma = quantidade = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar? (S/N) ')).upper().strip()[0]
media = soma / quantidade
print(f'Você digitou {quantidade} números e a média deles foi {media}\nO maior valor foi {maior} e o menor foi {menor}')