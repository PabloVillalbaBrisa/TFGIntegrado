import pandas as pd
import re

def count_words(text):
    if not isinstance(text, str):
        text = ""
    words = re.findall(r'\b\w+\b', text)
    return len(words)

file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_11.csv'
df = pd.read_csv(file_path)

df['texto'] = df['texto'].fillna("")


df['word_count'] = df['texto'].apply(count_words)

output_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_12.csv'
df.to_csv(output_path, index=False)

print(f"Archivo procesado y guardado en {output_path}")