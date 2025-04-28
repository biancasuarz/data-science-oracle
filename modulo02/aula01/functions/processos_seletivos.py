import numpy as np
import matplotlib.pyplot as plt

categorias = ['Gupy', 'Sites de Vagas', 'Total']
candidaturas = [84, 174, 258]
respostas_negativas = [60, 111, 171]
sem_resposta = [0, 0, 87]

empresas = ['Banco Pine', 'B3', 'Agendado']
pine_etapas = [1, 0, 0]
b3_etapas = [1, 1, 0]
agendado_etapas = [0, 0, 2]

meses = ['Jan', 'Fev', 'Mar', 'Abr']
candidaturas_mensais = [65, 65, 65, 65]
entrevistas_mensais = [1, 1, 1, 1]

fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# candidaturas e respostas
axs[0].barh(categorias, candidaturas, color='blue', label='Candidaturas Totais')
axs[0].barh(categorias, respostas_negativas, color='orange', label='Respostas Negativas')
axs[0].barh(categorias, sem_resposta, color='red', label='Sem Resposta')
axs[0].set_ylabel("Candidaturas x Respostas")
axs[0].legend()

# processos seletivos
x = np.arange(len(empresas))
bar_width = 0.5

axs[1].bar(x, pine_etapas, color='green', label='Banco Pine')
axs[1].bar(x, b3_etapas, color='green', label='B3')
axs[1].bar(x, agendado_etapas, bottom=np.array(pine_etapas) + np.array(b3_etapas), color='orange', label='Agendado')
axs[1].set_xticks(x)
axs[1].set_xticklabels(empresas)
axs[1].set_ylabel("Entrevistas")
axs[1].legend()

# candidatura x entrevista
axs[2].fill_between(meses, candidaturas_mensais, color='blue', alpha=0.4, label='Candidaturas por Mês')
axs[2].plot(meses, candidaturas_mensais, marker='o', color='blue')
axs[2].plot(meses, entrevistas_mensais, marker='o', color='orange', label='Entrevistas por Mês')
for i, txt in enumerate(entrevistas_mensais):
    axs[2].text(meses[i], entrevistas_mensais[i] + 1, str(txt), color="orange", fontsize=9)
axs[2].set_xlabel("Meses")
axs[2].set_ylabel("Candidaturas x Entrevistas")
axs[2].legend()

plt.tight_layout()
plt.show()
