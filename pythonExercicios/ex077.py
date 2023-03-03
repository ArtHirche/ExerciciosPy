palavras = ('arthur', 'esta', 'aprendendo', 'linguagem', 'python', 'curso',
            'em', 'video')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
