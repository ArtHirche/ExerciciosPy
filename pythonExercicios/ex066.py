from os import system

contador = soma = 0
numero = int(input('Digite um valor (999 para parar): '))
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um valor (999 para parar): '))
    system('cls')
    if numero == 999:
        break
print(f'Você digitou {contador} números\nA soma entre eles será {soma}')