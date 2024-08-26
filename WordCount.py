import pandas as pd
import re

def count_words(text):
    if not isinstance(text, str):
        text = ""
    # Contar palabras usando una expresión regular que considere solo palabras
    words = re.findall(r'\b\w+\b', text)
    return len(words)

# Cargar el archivo CSV
file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_11.csv'
df = pd.read_csv(file_path)

# Llenar los valores nulos en la columna 'texto' con una cadena vacía
df['texto'] = df['texto'].fillna("")

# Contar palabras en la columna 'texto' y agregar la columna 'word_count'
df['word_count'] = df['texto'].apply(count_words)

# Guardar el resultado en un nuevo archivo CSV
output_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_12.csv'
df.to_csv(output_path, index=False)

print(f"Archivo procesado y guardado en {output_path}")