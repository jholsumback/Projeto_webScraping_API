SELECT 
    oa.razao_social AS operadora,
    SUM(ano_2024.vl_saldo_final) AS total_despesas
FROM (
    SELECT reg_ans, descricao, vl_saldo_final FROM balanco_financeiro_1t2024
    UNION ALL
    SELECT reg_ans, descricao, vl_saldo_final FROM balanco_financeiro_2t2024
    UNION ALL
    SELECT reg_ans, descricao, vl_saldo_final FROM balanco_financeiro_3t2024
    UNION ALL
    SELECT reg_ans, descricao, vl_saldo_final FROM balanco_financeiro_4t2024
) AS ano_2024
JOIN operadoras_ativas oa ON ano_2024.reg_ans = CAST(oa.registro_ans AS INTEGER)
WHERE ano_2024.descricao ILIKE '%SINISTROS CONHECIDOS%' 
  AND ano_2024.descricao ILIKE '%ASSISTÊNCIA A SAÚDE%' 
  AND ano_2024.descricao ILIKE '%MEDICO%'
GROUP BY oa.razao_social
ORDER BY total_despesas DESC
LIMIT 10;