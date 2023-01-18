#Prática:
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
r = n1%n2
print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}', end=' ')
print(f'divisão inteira {di} e potência {e}')

"""
TEORIA:
Operadores Aritméticos:
+ Adição; (5 + 2 == 7)
- Subtração; (5 - 2 == 3)
* Multiplicação; (5 * 2 == 10)
/ Divisão; (5 / 2 == 2.5)
** Potência; (5 ** 2 == 25)
// Divisão inteira; (5 // 2 == 2)
% Resto da Divisão. (5 % 2 == 1)

Ordem de Precedência:
1)  Parênteses ();
2)  **;
3)  *, /, //, %;
4)  +, -.
Exemplos:
1)  5 + 3 * 2 == 11
2)  3 * 5 + 4 ** 2 == 31
3)  3 * (5 + 4) ** 2 == 243

OBS:
== Significa: igual a
= Significa: recebe
"""
