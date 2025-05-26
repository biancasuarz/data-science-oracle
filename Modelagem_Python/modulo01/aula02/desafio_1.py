#Coleta e amostragem de dados
#Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
print(f"Olá {nome_usuario}, você tem {idade_usuario} anos.")

#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.

nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
altura_usuario = float(input("Digite sua altura(ex: 1.53):"))
print(f"Olá {nome_usuario}, você tem {idade_usuario} anos e mede {altura_usuario} metros.")