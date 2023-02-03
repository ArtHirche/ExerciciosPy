#PRÁTICA:
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m.')

"""
TEORIA:
Padrão ANSI:
Style:
0 == None
1 == Bold (negrito)
4 == Underline (Sublinhado)
7 == Negative

Text:
30 == Branco
31 == Vermelho
32 == Verde
33 == Amarelo
34 == Azul
35 == Roxo
36 == Azul-Claro
37 == Cinza

Back:
40 == Branco
41 == Vermelho
42 == Verde
43 == Amarelo
44 == Azul
45 == Roxo
46 == Azul-Claro
47 == Cinza

Portanto:
\033[style; text; backm

Exemplo:
\033[0;33;44m
Style == padrão
Text == amarelo
Back == azul

Exemplo1:
\033[0;30;41m

Exemplo2:
\033[4;33;44m

Exemplo3:
\033[1;35;43m

Exemplo4:
\033[30;42m

Exemplo5:
\033[m

Exemplo6:
\033[7;30m
"""
