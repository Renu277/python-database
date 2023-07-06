import sqlite3
import csv

connection = sqlite3.connect("mydata.db")
cursor = connection.cursor()

cursor.execute("create table companies(id INTEGER PRIMARY KEY AUTOINCREMENT, business_id TEXT,business_name TEXT, taxable_revenue REAL, tax_paid REAL)")

def parse_csv( csv_file, table_name='companies', encoding='utf-8', open_mode='r', delimiter=';', skip_first_line=True):
        
        insert_sql=f"""
        INSERT INTO {table_name} (business_id, business_name, taxable_revenue, tax_paid) 
        VALUES (?,?,?,?)
        """
for row in cursor.execute("select * from companies"):
      print(row)

    

connection.close()