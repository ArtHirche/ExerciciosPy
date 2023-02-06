nota1 = float(input('Qual foi a primeira nota do(a) aluno(a)? '))
nota2 = float(input('Qual foi a segunda nota dele(a)? '))
media = (nota1+nota2)/2
if media < 5.0:
    print('\033[1;31mREPROVADO!\033[m')
elif (media == 5.0) or (media < 6.9):
    print('\033[1;33mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')
