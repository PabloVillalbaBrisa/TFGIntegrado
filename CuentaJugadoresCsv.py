import pandas as pd


def count_unique_values(csv_file, column_name):
    # Lee el archivo CSV en un DataFrame
    df = pd.read_csv(csv_file)

    # Filtra la columna seleccionada, eliminando valores NaN (celdas vacías)
    column_data = df[column_name].dropna()

    # Cuenta el número de valores únicos
    unique_values_count = column_data.nunique()

    return unique_values_count


# Ejemplo de uso:
csv_file = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_13.csv'  # Reemplaza con el nombre de tu archivo CSV
column_name = 'username'  # Reemplaza con el nombre de la columna que deseas analizar

print(f"Número de valores diferentes en la columna '{column_name}': {count_unique_values(csv_file, column_name)}")
