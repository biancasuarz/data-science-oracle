
import matplotlib.pyplot as plt

# Dados para os gráficos
# Gráfico de barras horizontais
categorias = ["Gupy", "Sites de Vagas", "Total"]
candidaturas = [84, 174, 258]
respostas_negativas = [60, 111, 171]
sem_resposta = [24, 63, 87]

# Gráfico de colunas agrupadas (processos seletivos)
empresas = ["Banco Pine", "B3", "Entrevistas Agendadas"]
etapas = [1, 2, 2]  # Número de etapas alcançadas

# Gráfico de linha (esforço ao longo do tempo)
meses = ["Mês 1", "Mês 2", "Mês 3", "Mês 4"]
candidaturas_mensais = [65, 65, 65, 65]
entrevistas_mensais = [1, 1, 1, 1]

# Criando os gráficos
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Gráfico de barras horizontais
axs[0].barh(categorias, candidaturas, color='blue', label='Candidaturas')
axs[0].barh(categorias, respostas_negativas, color='orange', label='Respostas Negativas', alpha=0.7)
axs[0].barh(categorias, sem_resposta, color='red', label='Sem Resposta', alpha=0.7)
axs[0].set_title("Candidaturas e Respostas por Categoria")
axs[0].set_xlabel("Quantidade")
axs[0].legend()

# Gráfico de colunas agrupadas
axs[1].bar(empresas, etapas, color='green', label='Etapas Alcançadas')
axs[1].set_title("Avanço nos Processos Seletivos")
axs[1].set_ylabel("Número de Etapas")
axs[1].set_ylim(0, 3)
axs[1].legend()

# Gráfico de linha
axs[2].plot(meses, candidaturas_mensais, marker='o', color='blue', label='Candidaturas por Mês')
axs[2].plot(meses, entrevistas_mensais, marker='o', color='orange', label='Entrevistas por Mês')
axs[2].set_title("Esforço ao Longo do Tempo")
axs[2].set_xlabel("Meses")
axs[2].set_ylabel("Quantidade")
axs[2].legend()

plt.tight_layout()
plt.show()
