import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata_limpio.csv')

# Contar el número de filas antes de eliminar duplicados
num_filas_antes = len(df)

# Eliminar filas duplicadas
df_sin_duplicados = df.drop_duplicates()

# Contar el número de filas después de eliminar duplicados
num_filas_despues = len(df_sin_duplicados)

# Guardar el DataFrame sin duplicados en un nuevo archivo CSV
df_sin_duplicados.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata_clean.csv', index=False)

# Informar si se han eliminado filas duplicadas
if num_filas_antes > num_filas_despues:
    print(f"Se han eliminado {num_filas_antes - num_filas_despues} filas duplicadas.")
else:
    print("No se han encontrado filas duplicadas.")




