# Faça 1um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
1
produto1 = float(input('Preço do produto 1: '))
produto2 = float(input('Preço do produto 2: '))
produto3 = float(input('Preço do produto 3: '))

if produto1 < produto2 and produto1 < produto3:
    print('Você deve comprar o produto 1.')
elif produto2 < produto1 and produto2 < produto3:
    print('Você deve comprar o produto 2.')    
else:
    print('Você deve comprar o produto 3.')
    

# menor_valor = min(n1, n2, n3)

# print('Compre o produto', end=' ')
# if n1 == menor_valor:
#     print('Produto 1')
# elif n2 == menor_valor:
#     print('Produto 2')
# else:
#     print('Produto 3')