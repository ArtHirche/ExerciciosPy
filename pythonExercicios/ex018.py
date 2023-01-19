from math import radians, sin, cos, tan
â = float(input('Digite um ângulo: '))
seno = sin(radians(â))
cosseno = cos(radians(â))
tangente = tan(radians(â))
print(f'Analisando o ângulo de {â}:\nO seno será: {seno:.2f}\nO cosseno será: {cosseno:.2f}\n A tangente será: {tangente:.2f}.')
#Correto!