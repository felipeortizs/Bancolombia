#importando las librerias
import pandas as pd
from sqlalchemy import create_engine

# Parámetros de conexión
server = 'LAPTOP-81FOU6LA'
database = 'master'
database_url = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'

# Crea un motor SQLAlchemy
engine = create_engine(database_url)

def create_table(type_file, file_path, table_name, sheet_name):
    
    if type_file == 'csv':
        df = pd.read_csv(file_path)
        print("Cargo el csv al dataframe")
    elif type_file == 'excel':
        df = pd.read_excel(file_path, sheet_name, engine='openpyxl')
        print("Cargo el excel al dataframe")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print("Tabla creada con éxito")

def append_to_table(type_file, file_path, table_name, sheet_name):
    
    if type_file == 'csv':
        df = pd.read_csv(file_path)
        print("Cargo el csv al dataframe")
    elif type_file == 'excel':
        df = pd.read_excel(file_path, sheet_name, engine='openpyxl')
        print("Cargo el excel al dataframe")
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print("Registros añadidos con éxito")

def query_table(table_name):
    
    df = pd.read_sql(f"SELECT TOP 20 * FROM {table_name}", engine)
    print(df)
    
if __name__ == "__main__":
    print("Pasó por el engine")

    # Para crear una nueva tabla (o reemplazarla si ya existe)
    type_file = 'csv' #poner 'csv' o 'excel'
    file_path = "ruta"
    table_name = 'name'
    #sheet_name = 'Hoja1'


    create_table(type_file, file_path, table_name, sheet_name=none) # cuando es csv sheet_name=None / cuando es excel es sheet_name

    #append_to_table(type_file, file_path, table_name, sheet_name)

    #query_table(table_name)