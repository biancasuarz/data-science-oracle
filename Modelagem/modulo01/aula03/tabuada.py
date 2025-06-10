# Programa para gerar a tabuada de um número escolhido pelo usuário

numero = int(input("Digite um número inteiro para ver sua tabuada (1 a 10): "))

if 1 <= numero <= 10: 
    print(f"Tabuada do {numero}:")
    for i in range(1, 11): 
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("Por favor, digite um número entre 1 e 10.")
