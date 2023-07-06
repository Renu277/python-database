import sqlite3
import csv

class Tax:
    db = None
    cur = None
    db_file = None

    def __init__(self, db_file=":memory:"):
        self.db_file=db_file
        self.db = sqlite3.connect(db_file)
        self.cur = self.db.cursor()

    def __del__(self):
        self.db.close()

    def commit(self):
        self.db.commit()

    def create_table(self, table_name='companies'):
        create_sql = f"""
        CREATE TABLE "{table_name}" (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        business_id TEXT,
        company_name TEXT,
        taxable_revenue REAL,
        tax_paid REAL
        );
        """

        self.cur.execute(create_sql)
        self.commit()

    def parse_csv(self, csv_file, table_name='companies', encoding='utf-8', open_mode='r', delimiter=';', skip_first_line=True):
        
        insert_sql=f"""
        INSERT INTO {table_name} (business_id, company_name, taxable_revenue, tax_paid) 
        VALUES (?,?,?,?)
        """
        
        with open(csv_file, open_mode, encoding=encoding) as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            line = 1

            for row in reader:
                if line==1 and skip_first_line:
                    print('Skipping first line')
                else:
                    self.cur.execute(insert_sql, (row[1], row[2], row[4], row[5]))
                    print(row[2] + ' Was added to DB')
                
                line+=1

        self.commit()
        return line
    

    def sql(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()