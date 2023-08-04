import pandas as pd 
import sqlite3

# Load the dataset (assuming it's in a CSV file)
data = pd.read_csv('sales_data.csv')

# Connect to an SQLite database (you can replace this with your preferred database)
conn = sqlite3.connect('data_review.db')

# Load the data into a database table
data.to_sql('sales_table', conn, if_exists='replace', index=False)

# Perform data review and QA using SQL
# Identify missing values
missing_data_query = '''
SELECT COUNT(*) AS total_rows,
       SUM(CASE WHEN product_id IS NULL THEN 1 ELSE 0 END) AS missing_product_id,
       SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END) AS missing_customer_id,
       SUM(CASE WHEN transaction_date IS NULL THEN 1 ELSE 0 END) AS missing_transaction_date
FROM sales_table;
'''

missing_data_result = pd.read_sql(missing_data_query, conn)

print("Missing Data Summary:")
print(missing_data_result)

# Close the database connection
conn.close()