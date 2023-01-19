#PRÁTICA:
frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[2][3])

"""
TEORIA:
frase1 = 'Curso em Vídeo Python'
O computador fará:
[C][u][r][s][o][][e][m][][V][í][d][e][o][][P][y][t][h][o][n]
 0  1  2  3  4 5  6  7 8  9 10 11 12 13 14 15 16 17 18 19 20
 Cada índice recebe um número sequencial de 0 até infinito.

Fatiamento de 'Curso em Vídeo Python':
frase[9] == V
frase[9:13] == Víde
frase[9:14] == Vídeo
frase[9:21] == Vídeo Python
frase[9:21:2] == Vdo Pto
frase[:5] == Curso
frase[15:] == Python
frase[9::3] == Ve Ph

Análise de 'Curso em Vídeo Python':
len(frase) == 21 caracteres
frase.count('o') == aparecem 3 'o' na str
frase.count('o', 0, 13) == de 0 até 13 só temos um 'o' na str
frase.find('deo') == 'deo' começou na posição 11
frase.find('Android') == -1, ou seja, não existe na str analisada
'Curso' in frase == True

Transformação de 'Curso em Vídeo Python':
frase.replace('Python', 'Android') == Curso em Vídeo Android
frase.upper() == CURSO EM VÍDEO PYTHON
frase.lower() == curso em vídeo python
frase.capitalize() == Curso em vídeo python
frase.title() == Curso Em Vídeo Python

Divisão de 'Curso em Vídeo Python':
frase.split() == ['Curso', 'em', 'Vídeo', 'Python']
                     0       1      2        3

Junção de 'Curso' 'em' 'Vídeo' 'Python'
'-'.join(frase) == Curso-em-Vídeo-Python
' '.join(frase) == Curso em Vídeo Python

frase2 = '---Aprenda Python--'
Transformação de 'Aprenda Python':
frase.strip == Aprenda Python
frase.rstrip == ---Aprenda Python
frase.lstrip == Aprenda Python--
"""
