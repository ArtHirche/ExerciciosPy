aluno = input('Qual é o nome do(a) aluno(a)? ')
nota1 = float(input('Qual foi a primeira nota dele(a)? '))
nota2 = float(input('Qual foi a segunda nota dele(a)? '))
média = (nota1 + nota2) / 2
print(f'A média do(a) aluno(a) \033[1;4m{aluno}\033[m, foi \033[4;34m{média:.1f}\033[m')
#Correto!