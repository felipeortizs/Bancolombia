import pyodbc
import pandas as pd


# Parámetros de conexión
server = 'LAPTOP-81FOU6LA'
database = 'master'
username = 'Felipe Ortiz'
password = 'Pipe2020*'
cnxn_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes'


# Conexión a la base de datos
cnxn = pyodbc.connect(cnxn_string)
cursor = cnxn.cursor()


# Si es CSV
file_path = 'C:/Users/Felipe Ortiz/Documents/Universidad EAFIT/Semestre 2023-2/Power BI/Millones_de_Registros.csv'
df = pd.read_csv(file_path)

# Crear tabla desde DataFrame
table_name = 'millones_de_registros'
df.to_sql(table_name, cnxn_string, if_exists='replace', index=False)




# # Crear una tabla
# cursor.execute('''
# CREATE TABLE Test (
#     ID INT PRIMARY KEY,
#     Name NVARCHAR(50)
# )
# ''')
# cnxn.commit()

# # Añadir datos q
# cursor.execute("INSERT INTO Test (ID, Name) VALUES (0, 'Nombre0'), (1, 'Nombre1')")
# cnxn.commit()

# # Consultar datos
# cursor.execute("SELECT * FROM Test")
# rows = cursor.fetchall()
# for row in rows:
#  print(row)

cursor.close()
cnxn.close()
