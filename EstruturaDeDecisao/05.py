# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Primeira nota: '))

if nota1  >= 7:
    if nota1 == 10.0:
        print('Aprovado com distinção')
    else:
        print('Aprovado')        
else:
    print('Reprovado')
