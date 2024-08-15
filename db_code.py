import sqlite3
import pandas as pd

# create new data base (STAFF.db) and connect to it
conn = sqlite3.connect('STAFF.db')


# table name in STAFF.db
table_name = 'INSTRUCTOR'

# attribute details = column headers
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# create file path and READ csv
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)




# use to_sql() to upload data frame to table (INSTRUCTOR)
# in STAFF.db
df.to_sql(table_name, conn, if_exists = 'replace', index=False)
print('Table is ready')


# Viewing all data in table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing only one column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing total number of rows (entries)
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Adding data to table
data_dict = {'ID': [100], 'FNAME': ['John'], 'LNAME': ['Doe'], 'CITY': ['Paris'], 'CCODE': ['FR']}

data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index = False)
print('Data appended successfully')


# Run count to see how many rows are in table now
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()
connect = sqlite3.connect('STAFF.db')

# Departments Table
#initialize tb name
tb_name = 'Departments'
#initialize tb headers
attr_list = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']
#create file path to data being moved to Departments data base
f_path = '/home/project/Departments.csv'
#create data frame by reading file path and adding headers
df1 = pd.read_csv(f_path, names = attr_list)
#data frame to sql table
df1.to_sql(tb_name, connect, if_exists = 'replace', index = False)
print(f'{tb_name} table is ready!!!')
# Append data to table
new_data_dict = {'DEPT_ID': [9], 'DEP_NAME': ['Quality Assurance'], 'MANAGER_ID': [30010], 'LOC_ID': ['L0010']}
new_data = pd.DataFrame(new_data_dict)
# Query to view all data
query = f"SELECT * FROM {tb_name}"
query_result = pd.read_sql(query, connect)
print(query)
print(query_result)
# Query only department names
query = f"SELECT DEP_NAME FROM {tb_name}"
query_result = pd.read_sql(query, connect)
print(query)
print(query_result)
# Query the count of the table (total entries)
query = f"SELECT COUNT(*) FROM {tb_name}"
query_result = pd.read_sql(query, connect)
print(query)
print(query_result)







