#Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual = float(input("Digite o percentual de crescimento da produção (%): "))

if percentual > 0:
    print(f"Houve crescimento de {percentual}%.")
elif percentual < 0:
    print(f"Houve decrescimento de {percentual}%.")
else:
    print("Não houve crescimento nem decrescimento.")
