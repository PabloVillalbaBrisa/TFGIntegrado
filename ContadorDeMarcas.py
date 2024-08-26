import pandas as pd
from collections import Counter
import re

csv = 'atp_only_insta.csv'
col_name = 'Marcas Jugador'
df = pd.read_csv(csv)

#ELIMINAMOS LAS FILAS DE LAS QUE SE DESCONOZCAN LAS MARCAS
df_filtrado = df[~df[col_name].str.contains('Se desconoce con que marcas trabaja el jugador', na=False)]

def split_words(text):
    if pd.isna(text):
        return []
    words = re.split(r'[,\s]+', text.strip())
    return words

#ELIMINAMOS COMAS Y ESPACIOS PARA DEVOLVER UNA LISTA DE PALABRAS
all_words = []
df_filtrado[col_name].apply(lambda x: all_words.extend(split_words(x)))

#CONTADOR DE PALABRAS
word_counter = Counter(all_words)

#COUNTER ES UN DICCIONARIO, LAS PALABRAS SON LAS CLAVES, Y LAS FRECUENCIAS LOS VALORES
word_count_df = pd.DataFrame(word_counter.items(), columns=['Palabra', 'Frecuencia'])

#QUEREMOS QUE EL ORDEN SEGÚN FRECUENCIA SEA DE MAYOR A MENOR
word_count_df = word_count_df.sort_values(by='Frecuencia', ascending=False)

print(word_count_df)

output = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/frecuencia_marcas.csv'
word_count_df.to_csv(output, index=False)