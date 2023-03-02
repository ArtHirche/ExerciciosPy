import random

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sorteio = random.choices(tupla, k=5)
print(f'Os valores sorteados foram: {sorteio}')