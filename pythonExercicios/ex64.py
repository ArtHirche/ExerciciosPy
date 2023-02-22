numero = contador = soma = 0
numero = int(input('Digite um número (999 para encerrar): '))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input('Digite um número (999 para encerrar): '))
print(f'Foram digitados {contador} números. A soma entre eles foi {soma}.')