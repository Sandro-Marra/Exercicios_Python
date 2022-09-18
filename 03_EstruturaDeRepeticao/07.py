# Faça um programa que leia 5 números e informe o maior número.

# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))
# n3 = int(input('Terceiro número: '))
# n4 = int(input('Quarto número: '))
# n5 = int(input('Quinto número: '))

contador = 0
maior = 0
while contador <= 4:
    n = int(input("Digite um numero: "))
    if(n > maior):
        maior = n
    contador += 1
print("o maior numero digitado foi:",maior)

                