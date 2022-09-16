# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Informe o nome: ')

while not (len(nome) > 3):
    print('Nome inválido, informe o nome com mais de 3 caracteres')
    nome = input('Nome: ')
print('Nome validado')


idade = int(input('Idade: '))

while idade < 0 or idade > 150:
    print('Idade inválida, informe a idade entre 0 e 150')
    idade = int(input('Idade: '))
print('Idade validada')


salario = float(input('Salário: '))

while not salario > 0:
    print('Salário inválido, o salário deve ser maior que zero.')
    salario = float(input('Salário: '))
print('Salário validado')  


sexo = input('Sexo: ')

while sexo != "f" and sexo != "m":
    print('Sexo inválido, informe F ou M.')
    sexo = input('Sexo: ')
print('Sexo validado')


estado_civil = input('Informe o estado civil: ')

while estado_civil not in 'scvd':
    print('Estado civil inválido, informe s, c, v ou d.')
    estado_civil = input('Estado civil: ')
print('Estado civil validado.')    