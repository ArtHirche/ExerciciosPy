#Prática:
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}.')

"""
TEORIA:
O comando usado é import, para importar uma biblioteca. Importa toda a biblioteca.
Exemplo:
1)  import bebida (importa todas as bebidas da biblioteca bebidas)
2)  from doce import pudim (importa só pudim da biblioteca doces)

Exemplos com biblioteca real:
1)  import math (importa biblioteca matemática inteira)
Na math, temos:
ceil == arredondar para cima;
floor == arredondar para baixo;
trunc == eliminar todos depois da vírgula;
pow == potência;
sqrt == raiz quadrada;
factorial == fatorial.

2)  from math import sqrt (importa só sqrt da biblioteca matemática);
3)  from math import sqrt, ceil (importa sqrt e ceil da biblioteca matemática).
"""
