# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = input('Usuário: ')
senha = input('Senha: ')

if senha != usuario:
    print('Usuário e senha cadastrados')
else:
    while not senha != usuario:
        print('Senha inválida')
        senha = input('Senha: ')
print('Senha cadastrada')


# while senha == usuario: # condição de repetição
#     print('A senha não pode ser igual ao nome do usuário!')
#     senha = input('Senha: ')
# # caso a condição de execução seja falsa (continua)
# # else sem o contexto
# print('Informações foram cadastradas com sucesso!')