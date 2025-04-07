nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
nota_3 = float(input('Digite sua terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3
print(f'Sua nota final é {media}')

if media >= 7 :
    print('Aprovado(a)!')
elif media > 5 and media < 7 :
    print('Recuperação!')
else:
    print('Reprovado(a)!')

