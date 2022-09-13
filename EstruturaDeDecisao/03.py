# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

opcao = input('Informe F ou M: ')

if opcao.lower() == 'f':
    print('Feminino')
elif opcao.lower() == 'm':
    print('masculino')
else:
    print('Sexo inválido')