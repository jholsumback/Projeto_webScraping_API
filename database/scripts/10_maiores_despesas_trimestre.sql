SELECT 
    oa.razao_social AS operadora,
    SUM(bf.vl_saldo_final) AS total_despesas
FROM balanco_financeiro_4t2023 bf
JOIN operadoras_ativas oa ON bf.reg_ans = CAST(oa.registro_ans AS INTEGER)
WHERE bf.descricao ILIKE '%SINISTROS CONHECIDOS%' 
  AND bf.descricao ILIKE '%ASSISTÊNCIA A SAÚDE%' 
  AND bf.descricao ILIKE '%MEDICO%'
GROUP BY oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;