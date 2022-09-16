# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Informe uma nota entra 0 e 10: '))

if nota >= 0 and nota <= 10:
    print('Valor válido')    
else: 
    while not(nota >= 0 and nota <= 10):
        print('valor inválido')
        nota = int(input('Informe uma nota entra 0 e 10: '))
print('válido')        