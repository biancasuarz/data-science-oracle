#Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

numero_1 = int(input('Digite um numero inteiro: '))
numero_2 = int(input('Digite outro numero inteiro: '))

if numero_1 > numero_2:
    menor = numero_2
    maior = numero_1
else:
    menor = numero_1
    maior = numero_2

print(f"Os números entre {menor} e {maior} são:")

for numero in range(menor + 1, maior): 
    print(numero)