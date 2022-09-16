# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ')

if letra.lower() in 'aeiou':
    print('Vogal.')
elif not letra.isalpha():
    print('Valor inválido')
else:
    print('Consoante.')