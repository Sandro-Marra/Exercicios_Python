# Faça um programa que leia 5 números e informe o maior número.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
n4 = int(input('Quarto número: '))
n5 = int(input('Quinto número: '))

if (n1 > n2 or n1 > n3 or n1 > n4 or n1 > n5):
    print ('O maior número é:', n1)    

if (n2 > n1 or n2 > n3 or n2 > n4 or n2 > n5): 
        print ('O maior número é:', n2)    

if (n3 > n1 or n3 > n2 or n3 > n4 or n3 > n5): 
        print ('O maior número é:', n3) 

if (n4 > n1 or n4 > n2 or n4 > n3 or n4 > n5): 
        print ('O maior número é:', n4)

if (n5 > n1 or n5 > n2 or n5 > n3 or n5 > n4): 
        print ('O maior número é:', n5)                  