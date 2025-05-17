import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_csv('temperaturas.csv')

# Exibe as 5 primeiras linhas
print("Dados de temperatura:")
print(df.head())

# Converte a coluna 'Dia' para formato de data (opcional, se quiser usar datas reais)
# df['Dia'] = pd.to_datetime(df['Dia'], format='%d/%m')

# Plotando o gráfico de linhas
plt.figure(figsize=(10, 5))
plt.plot(df['Dia'], df['Temperatura'], marker='o', linestyle='-', color='purple')
plt.title('Variação de Temperatura ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_temperatura.png')
plt.show()
