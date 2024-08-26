import pandas as pd
from langdetect import detect, LangDetectException
import langcodes

# Cargar el archivo CSV
df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_10.csv')

# Función para detectar el idioma
# Función para detectar el idioma y convertir el código al nombre completo
def detectar_idioma(texto):
    if isinstance(texto, str):  # Verificar si el texto es una cadena
        try:
            codigo_idioma = detect(texto)
            nombre_idioma = langcodes.Language.get(codigo_idioma).display_name()
            return nombre_idioma
        except LangDetectException:
            return 'desconocido'
    else:
        return 'desconocido'  # Devolver 'no_texto' si no es una cadena

# Crear una nueva columna 'idioma' aplicando la función a la columna de texto
df['idioma'] = df['texto'].apply(detectar_idioma)

# Guardar el DataFrame con la nueva columna en un nuevo archivo CSV
df.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_11.csv', index=False)

print("Archivo procesado y guardado con éxito.")
