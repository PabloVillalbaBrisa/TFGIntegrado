import pandas as pd
import numpy as np

csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_3.csv'  # Cambia esto por la ruta de tu archivo

df = pd.read_csv(csv_path)

#FUNCIÓN QUE REEMPLAZA LAS COLUMNAS VACÍAS EN SPONSORS
def replace_empty_or_nan(df, column_name, replacement):
    df[column_name] = df[column_name].replace([np.nan, '', 'nan'], replacement)
    return df

df = replace_empty_or_nan(df, 'sponsors', 'No hay sponsors')
output_csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_4.csv'  # Cambia esto por la ruta donde deseas guardar el nuevo archivo
df.to_csv(output_csv_path, index=False)

