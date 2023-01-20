frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count("A")}\nA primeira letra A aparece na posição {frase.find("A")+1}\nA última letra A aparece na posição {frase.rfind("A")+1}')
#Correto!