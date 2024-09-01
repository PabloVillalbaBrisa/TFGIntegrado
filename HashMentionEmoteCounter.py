import pandas as pd
import re
import emoji

def count_hashtags(hashtag_str):
    if pd.isna(hashtag_str) or hashtag_str == '':
        return 0
    return len(hashtag_str.split(';'))

#CONTADOR DE MENCIONES EN LA COLUMNA TEXTO
def count_mentions(text):
    if pd.isna(text):
        return 0
    return len(re.findall(r'@\w+', text))

#CONTADOR DE EMOTICONOS EN LA COLUMNA TEXTO
def count_emojis(text):
    if pd.isna(text):
        return 0
    return sum(1 for char in text if char in emoji.EMOJI_DATA)

#CARGAMOS EL CSV DESTINO
df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_9.csv')

#LLAMAMOS A LAS FUNCIONES, SUS PARÁMETROS SON LAS COLUMNAS A LAS QUE SE APLICAN
#EL RESULTADO SE GUARDA EN LAS NUEVAS COLUMNAS CREADAS
df['num_hashtags'] = df['hashtags'].apply(count_hashtags)
df['num_mentions'] = df['texto'].apply(count_mentions)
df['num_emojis'] = df['texto'].apply(count_emojis)


output_csv_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_10.csv'
df.to_csv(output_csv_path, index=False)

print("Archivo CSV actualizado guardado en:", output_csv_path)