info = input('Digite algo: ')
print('O tipo \033[30mprimitivo\033[m desse valor é: ', type(info))
print('É um \033[31malfanumérico\033[m? ', info.isalnum())
print('Só tem \033[32mespaços?\033[m ', info.isspace())
print('É um \033[33mnúmero\033[m? ', info.isnumeric())
print('É \033[34malfabético\033[m? ', info.isalpha())
print('Está em \033[35mmaiúsculas\033[m? ', info.isupper())
print('Está em \033[36mminúsculas\033[m? ', info.islower())
print('Está \033[7;37mcapitalizado\033[m? ', info.istitle())
#Correto!