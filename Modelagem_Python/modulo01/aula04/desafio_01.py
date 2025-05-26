gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
soma = sum(gastos)
media = soma / len(gastos)
print(soma)
print(f"Média de gastos: {media:.2f}")

compras_acima_3000 = [gasto for gasto in gastos if gasto > 3000]
quantidade_acima_3000 = len(compras_acima_3000)
percentual_acima_3000 = (quantidade_acima_3000 / len(gastos)) * 100

print(f"Compras acima de 3000: {quantidade_acima_3000}")
print(f"Porcentagem de compras acima de 3000: {percentual_acima_3000:.2f}%")