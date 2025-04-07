#Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual = float(input("Digite o percentual de crescimento da produção (%): "))

if percentual > 0:
    print(f"Houve crescimento de {percentual}%.")
elif percentual < 0:
    print(f"Houve decrescimento de {percentual}%.")
else:
    print("Não houve crescimento nem decrescimento.")

#Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = input("Digite uma letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra do alfabeto.")
elif letra in 'aeiou':
    print("É uma vogal.")
else:
    print("É uma consoante.")
