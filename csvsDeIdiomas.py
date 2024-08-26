import pandas as pd
import os

# Leer el CSV original
df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_12.csv')

# Suponiendo que la columna con los idiomas detectados se llama 'language'
language_column = 'idioma'

# Crear un directorio para los archivos resultantes
output_path = 'C:/Users/pvill/OneDrive/Documentos/CSV_IDIOMAS'
# Verificar que el directorio existe, si no, crearlo
os.makedirs(output_path, exist_ok=True)

# Obtener los diferentes idiomas
languages = df[language_column].unique()

# Generar un CSV por cada idioma
for language in languages:
    language_df = df[df[language_column] == language]
    file_name = f'{language}.csv'
    output_file = os.path.join(output_path, file_name)
    language_df.to_csv(output_file, index=False)

print("Archivos generados con éxito.")
