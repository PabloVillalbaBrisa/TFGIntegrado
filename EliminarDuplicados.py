import pandas as pd

df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata_limpio.csv')

num_filas_antes = len(df)

df_sin_duplicados = df.drop_duplicates()

num_filas_despues = len(df_sin_duplicados)

df_sin_duplicados.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/metadata_clean.csv', index=False)

if num_filas_antes > num_filas_despues:
    print(f"Se han eliminado {num_filas_antes - num_filas_despues} filas duplicadas.")
else:
    print("No ha habido filas duplicadas.")




