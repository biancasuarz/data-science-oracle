#manipulando strings

texto = "Amo Jesus"
print(texto)

print(texto.upper())
print(texto.lower())

invertido = ''.join(reversed(texto))
print(invertido)

n1 = 123456789
inverso = int(str(n1)[::-1])
print(inverso)

texto2 = "Byanca"
texto2 = texto2.strip().replace('y', 'i')
print(texto2)