import sqlite3
connection=sqlite3.connect("ltc.db")
cursor=connection.cursor()

table_info="""
Create table employee(name varchar(30),
                    role varchar(30),
                    dept varchar(30),
                    salary FLOAT);
"""
cursor.execute(table_info)
cursor.execute('''Insert Into employee values('Venkat','Software Engineer', 'OB' ,15000)''')
cursor.execute('''Insert Into employee values('Ajay','Release Manager', 'OB', 15000)''')
cursor.execute('''Insert Into employee values('Anis','Quality Engineer', 'OB', 14000)''')
cursor.execute('''Insert Into employee values('Bramha','Quality Engineer','OB', 14000)''')
cursor.execute('''Insert Into employee values('Nagendra','SRE','CBO', 14000)''')

print("data inserted successfully")

connection.commit()
connection.close()
