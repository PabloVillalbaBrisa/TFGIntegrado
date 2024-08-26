import pandas as pd
import numpy as np

# Ruta del archivo CSV
csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_3.csv'  # Cambia esto por la ruta de tu archivo

# Leer el archivo CSV
df = pd.read_csv(csv_path)

# Función para reemplazar celdas vacías o NaN
def replace_empty_or_nan(df, column_name, replacement):
    df[column_name] = df[column_name].replace([np.nan, '', 'nan'], replacement)
    return df

# Reemplazar las celdas vacías o NaN en la columna 'columna' por la cadena 'X'
df = replace_empty_or_nan(df, 'sponsors', 'No hay sponsors')
# Guardar el DataFrame actualizado en un nuevo archivo CSV
output_csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_4.csv'  # Cambia esto por la ruta donde deseas guardar el nuevo archivo
df.to_csv(output_csv_path, index=False)

