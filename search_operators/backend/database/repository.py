import psycopg2
from psycopg2.extras import RealDictCursor

def find(query: str):
    # Conexão com o banco
    conn = psycopg2.connect(
        host="localhost",
        database="dados_teste2",
        user="postgres",
        password="12323",
        port=5432
    )
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    sql = """
        SELECT * FROM operadoras_ativas
        WHERE registro_ans ILIKE %s OR cnpj ILIKE %s OR razao_social ILIKE %s OR nome_fantasia ILIKE %s OR modalidade ILIKE %s OR cidade ILIKE %s OR uf ILIKE %s OR endereco_eletronico ILIKE %s OR representante ILIKE %s OR cargo_representante ILIKE %s;
    """

    search_query = f"%{query}%"
    cursor.execute(sql, (search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows
  