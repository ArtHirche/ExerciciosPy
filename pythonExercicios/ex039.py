anoNascimento = int(input('Em que ano você nasceu? '))
idade = 2023-anoNascimento
if idade < 18:
    print(f'Você ainda vai se alistar.\nFalta(m) {18-idade} ano(s) para você se alistar.')
elif idade == 18:
    print('Você já pode se alistar!')
else:
    print(f'Passou o tempo de se alistar!\nVocê passou {idade-18} ano(s) do prazo.')
