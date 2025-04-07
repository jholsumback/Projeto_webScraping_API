import psycopg2

# Conexão com o banco
conn = psycopg2.connect(
    host="localhost",
    database="dados_teste2",
    user="postgres",
    password="12323",
    port=5432
)

csv_path = "C:/Users/jhols\OneDrive/Área de Trabalho/planilhas/4T2024_corrigido.csv"
table_name = 'balanco_financeiro_4t2024'

cur = conn.cursor()

with open(csv_path, 'r', encoding='utf-8') as f:
    next(f)  # Pula o cabeçalho
    cur.copy_expert(
        f"""
        COPY {table_name} (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
        FROM STDIN WITH CSV DELIMITER ';' NULL '' ENCODING 'UTF8'
        """,
        f
    )

conn.commit()
cur.close()
conn.close()

print("Importação concluída com sucesso!")
