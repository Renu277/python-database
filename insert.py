import tax

taxes = tax.Tax('companies.db')
#taxes.create_table()
#print(taxes.parse_csv('data.csv'))

sql_top_payers="""
SELECT company_name, MAX(CAST(taxable_revenue AS NUMERIC)) as max_taxable_income
    FROM data
    ORDER BY max_taxable_income DESC
    LIMIT 1;
"""

sql_amount_of_companies="""
SELECT COUNT(*) AS total_companies
FROM companies;
"""

print(taxes.sql(sql_amount_of_companies)[0][0])

