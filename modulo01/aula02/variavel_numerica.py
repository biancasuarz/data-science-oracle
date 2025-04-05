#Quantidade de funcionarios e salarios(seguranca, docente e diretoria)2

q_seguranca = 5
s_seguranca = 3000

q_docente = 16
s_docente = 6000

q_diretoria = 1
s_diretoria = 12500

total_funcionario = q_seguranca + q_docente + q_diretoria
print(total_funcionario)

diferenca_salario = s_docente - s_seguranca
print(diferenca_salario)

media = (q_seguranca*s_seguranca + q_diretoria*s_diretoria + q_docente*s_docente) / (total_funcionario)
print(media)