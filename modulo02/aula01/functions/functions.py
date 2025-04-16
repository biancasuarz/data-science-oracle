import matplotlib as plt

notas = {'Primeiro trimestre:': 9.5,'Segundo trimestre':9.8, 'Terceiro trimestre': 10.0}

soma = 0

for nota in notas.values():
    soma = sum(notas.values())
    media = soma / 3
    media = round(media)
print (f'Soma das notas: {soma} | Média final: {media}')

print(type(notas))

