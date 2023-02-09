#PRÁTICA:
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valores foi {s}')

"""
TEORIA:
passo == boneco anda
pegar == boneco pega item
pula == boneco pula

Se precisar andar muitas vezes, porém, fica muito repetitivo
Usamos a estrutura de repetição:
laçocnointervalo(1,10)
    passo
pegar
Em Py:
for c in range(1,10):
    passo
pega

Exemplos:
1)
for c in range(0,3):
    passo
    pula
passo
pega

2)
for c in range(0,3):
    if temMoeda:
        pega
    passo
    pula
passo
pega

"""
