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

#Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

# Entrada dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Escolha da operação
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

# Realiza a operação
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero.")
        exit()
else:
    print("Operação inválida.")
    exit()

# Exibe o resultado
print(f"\nResultado da operação: {resultado}")

#positivo ou negativo
if resultado > 0:
    print("O resultado é positivo.")
elif resultado < 0:
    print("O resultado é negativo.")
else:
    print("O resultado é zero (neutro).")

#inteiro ou decimal
if resultado == int(resultado):
    print("O resultado é um número inteiro.")
    #par ou ímpar (só para inteiros)
    if int(resultado) % 2 == 0:
        print("O resultado é par.")
    else:
        print("O resultado é ímpar.")
else:
    print("O resultado é um número decimal.")
