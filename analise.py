import numpy as np

# Criar vendas fictícias 12 meses
meses = np.array(["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"])
vendas = np.array([1500, 2000, 1750, 4000, 3570, 2400, 1700, 1800, 5450, 1000, 2100, 2300])

# Estatísticas básicas
media_vendas = np.mean(vendas)
maior_venda = np.max(vendas)
menor_venda = np.min(vendas)

# Identificando o melhor mês
indice_melhor_mes = np.argmax(vendas)
melhor_mes = meses[indice_melhor_mes]

# Crescimento percentual do ano
crescimento = ((vendas[-1] - vendas[0]) / vendas[0]) * 100

print("===== Análise Vendas Anual =====")
print(f"Média de vendas: {media_vendas:.2f}")
print(f"Maior venda: {maior_venda}")
print(f"Menor venda: {menor_venda}")
print(f"Melhor mês: {melhor_mes}")
print(f"Crescimento anual: {crescimento:.2f}%")