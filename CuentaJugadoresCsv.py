import pandas as pd


def count_unique_values(csv_file, column_name):

    df = pd.read_csv(csv_file)
    #ELIMINA VALORES NA
    column_data = df[column_name].dropna()

    #CONTADOR DE VALORES DIFERENTES
    unique_values_count = column_data.nunique()

    return unique_values_count

csv_file = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_13.csv'
column_name = 'username'

print(f"Número de valores diferentes en la columna '{column_name}': {count_unique_values(csv_file, column_name)}")
