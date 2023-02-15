num1 = int(input('Digite um número para saber o fatorial: '))
f1 = 1
c1 = num1
while c1 > 1:
    f1 *= c1
    c1 -= 1
print(f'O resultado de {num1}! é {f1}')