import pandas as pd

# Caminho do CSV original
csv_original = "C:/Users/jhols/OneDrive/Área de Trabalho/planilhas/4T2024.csv"
csv_corrigido = "C:/Users/jhols/OneDrive/Área de Trabalho/planilhas/4T2024_corrigido.csv"

# Lê o CSV
df = pd.read_csv(csv_original, sep=';', encoding='utf-8')

# Converte vírgulas para pontos nas colunas de valor
df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].str.replace(',', '.').astype(float)
df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].str.replace(',', '.').astype(float)

# Salva CSV corrigido (com ponto)
df.to_csv(csv_corrigido, sep=';', index=False, encoding='utf-8')

print("Conversão concluída com sucesso!")
