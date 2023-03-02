classificacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
                 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
                 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
                 'Red Bull Bragantino', 'Coritiba', 'Cuiabá', 'Ceará',
                 'Atlético-GO', 'Avaí', 'Juventude')
print('-=' * 35)
print(f'Classificação geral do Brasileirão 2022: {classificacao}')
print('-=' * 35)
print(f'Os 5 primeiros são: {classificacao[0:5]}')
print('-=' * 35)
print(f'Os 4 últimos são {classificacao[16:20]}')
print('-=' * 35)
print(f'Em ordem alfabética: {sorted(classificacao)}')