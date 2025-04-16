import matplotlib
import matplotlib.pyplot as plt

# Dados para o gráfico
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Criando o gráfico
plt.plot(x, y, label="Linha 1")
plt.title("Exemplo de Gráfico")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()

# Mostrar o gráfico
plt.show()
