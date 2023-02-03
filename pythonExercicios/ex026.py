frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece \033[1;31m{frase.count("A")}\033[m\nA primeira letra A aparece na posição \033[1;34m{frase.find("A")+1}\033[m\nA última letra A aparece na posição \033[1;36m{frase.rfind("A")+1}\033[m')
#Correto!