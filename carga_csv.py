import pandas as pd
from sqlalchemy import create_engine

# Parámetros de conexión
server = 'LAPTOP-81FOU6LA'
database = 'master'
database_url = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'

# Crea un motor SQLAlchemy
engine = create_engine(database_url)

print("paso por el engine")

# Si es CSV
file_path = 'ruta'
df = pd.read_csv(file_path)

# Si es excel
file_path = 'C:/Users/Felipe Ortiz/Downloads/Columna a Partir de Ejemplos Practicar.xlsx'
df = pd.read_excel(file_path, sheet_name='Hoja1', engine='openpyxl')



print("cargo el csv al dataframe")

# Crear tabla desde DataFrame
table_name = 'Apartir_de_ejemplos'
print("va a iniciar la carga a la BD")
df.to_sql(table_name, engine, if_exists='replace', index=False)
print("tabla creada con exito")
