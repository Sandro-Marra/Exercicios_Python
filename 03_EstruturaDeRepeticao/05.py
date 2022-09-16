# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_a = int(input('Informe a população do pais A: '))
tx_a = float(input('Informa a tava de crescimento do pais A: '))
pais_b = int(input('Informe a população do pais B:'))
tx_b = float(input('Informa a tava de crescimento do pais A: '))

ano = 0 #simular a passagem de anos
while not (pais_a >= pais_b):
#while pais_a < pais_b:
    pais_a = round(pais_a * tx_a + pais_a)
    pais_b = round(pais_b * tx_b + pais_b)
    ano = ano + 1

print(f'''
A população do País A de {pais_a} habitantes
ultrapassou o País B de {pais_b} habitantes
após {ano} anos.
''')
# repetir = input('Deseja repetir a operação, S ou N? ').lower()
# if repetir == "s": 

