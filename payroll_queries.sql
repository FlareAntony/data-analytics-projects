SELECT
    name,
    CAST(salary_usd AS REAL) AS clean_salary_usd,
    UPPER(REPLACE(country, ' ', '')) AS standardized_country
FROM payroll_logs
WHERE salary_usd != 'ERROR_NO_DATA'
  AND hours_logged IS NOT NULL
  AND CAST(salary_usd AS REAL) <= 50000;
