import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

# q = """
# SELECT *
# FROM orderDetails
# JOIN products
# ON orderDetails.productCode = products.productCode
# LIMIT 10;
# """

# USING. If column names are identical between the table, you can simplify with USING(), rather than ON

# q = """
# SELECT *
# FROM orderDetails
# JOIN products
# USING (productCode)
# LIMIT 10;
# """

# ALIAS TABLES. Just like aliasing columns, you can alias tables. This can help simplify when writing code (instead of typing whole name of table) for long queries

# q = """
# SELECT *
# FROM orderDetails AS od
# JOIN products AS p
# ON od.productCode = p.productCode
# LIMIT 10;
# """

# PRINT INDIVIDUAL QUERIES ABOVE
# print(pd.read_sql(q, conn))

# LEFT JOIN. By default, a JOIN is an INNER JOIN. The LEFT JOIN will return all records from the left table and matched records from the right table

# q = """
# SELECT *
# FROM products
# LEFT JOIN orderDetails
# USING (productCode);
# """

# df = pd.read_sql(q, conn)

# Print length of records
# print("Number of records returned: ", len(df))
# print("Number of records where order details are NULL: ", len(df[df.orderNumber.isnull()]))
# Which product has no order?
# print(df[df.orderNumber.isnull()]) 

# FOREIGN KEYS - matches from different tables, you would only need to pull one column from one table

q = """
SELECT c.customerNumber, c.customerName, c.salesRepEmployeeNumber, e.employeeNumber
FROM customers AS c
JOIN employees AS e
ON c.salesRepEmployeeNumber = e.employeeNumber
ORDER BY employeeNumber
"""

df = pd.read_sql(q, conn)
print(df)



conn.close()