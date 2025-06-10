lista = ['Bianca Soares', 9.0,9.5,9.7,True]

for elemento in lista:
    print(elemento)

lista[3] = 10

for elemento in lista:
    print(elemento)

media = (lista[1] + lista[2] + lista[3]) / 3
print(f'A média das notas é: {media}')