import pandas as pd
import os

#LECTURA DEL CSV
df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_12.csv')

#DIRECTORIO PARA ALMACENAR LOS NUEVOS CSVS
output_path = 'C:/Users/pvill/OneDrive/Documentos/CSV_IDIOMAS'

#VERIFICA SI EL DIRECTORIO EXISTE, SI NO, LO CREA
os.makedirs(output_path, exist_ok=True)

#EN LANGUAGES OBTENEMOS LOS IDIOMAS DIFERENTES QUE HAN SIDO DETECTADOS
languages = df['idioma'].unique()

#GENERA UN CSV POR IDIOMA CON LAS FILAS CORRESPONDIENTES A DICHO IDIOMA
for language in languages:
    language_df = df[df['idioma'] == language]
    file_name = f'{language}.csv'
    output_file = os.path.join(output_path, file_name)
    language_df.to_csv(output_file, index=False)

print("Csvs de idiomas generados")
