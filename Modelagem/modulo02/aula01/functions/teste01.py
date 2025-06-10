import matplotlib.pyplot as plt

estudantes = ['Ana', 'Bianca', 'Carlos']
notas = [8, 9, 7]

plt.bar(x=estudantes, height=notas)
plt.xlabel('Estudantes')
plt.ylabel('Notas')
plt.title('Notas dos Estudantes')
plt.show()
