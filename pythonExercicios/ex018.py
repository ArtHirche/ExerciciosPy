from math import radians, sin, cos, tan
â = float(input('Digite um ângulo: '))
seno = sin(radians(â))
cosseno = cos(radians(â))
tangente = tan(radians(â))
print(f'Analisando o ângulo de \033[1;4m{â}:\033[m\nO seno será: \033[1;31m{seno:.2f}\033[m\nO cosseno será: \033[1;34m{cosseno:.2f}\033[m\n A tangente será: \033[1;33m{tangente:.2f}\033[m.')
#Correto!