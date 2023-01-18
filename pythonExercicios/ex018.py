import math
â = int(input('Digite um ângulo: '))
seno = math.sin(â)
cosseno = math.cos(â)
tangente = seno+cosseno
print(f'Analisando o ângulo de {â}:\nO seno será: {seno:.2f}\nO cosseno será: {cosseno:.2f}\n A tangente será: {tangente:.2f}.')
