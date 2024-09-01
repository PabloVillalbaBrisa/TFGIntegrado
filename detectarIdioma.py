import pandas as pd
from langdetect import detect, LangDetectException
import langcodes

df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_10.csv')

#FUNCIÓN QUE DETECTA EL IDIOMA
def detectar_idioma(texto):
    #COMPRUEBA QUE EL TEXTO ES STRING
    #SI EL TEXTO NO ES STRING O NO SE DETECTA UN IDIOMA SE DEVUELVE DESCONOCIDO
    #ESTO PUEDE PASAR SI EL TEXTO ESTÁ EN VARIAS IDIOMAS, EN IDIOMAS POCO COMUNES,
    #ES MUY CORTO O CONTIENE CARACTERES ESPECIALES ABUNDANTES, POR EJEMPLO.
    if isinstance(texto, str):
        try:
            codigo_idioma = detect(texto)
            nombre_idioma = langcodes.Language.get(codigo_idioma).display_name()
            return nombre_idioma
        except LangDetectException:
            return 'desconocido'
    else:
        return 'desconocido'

#NUEVA COLUMNA DE IDIOMA
df['idioma'] = df['texto'].apply(detectar_idioma)

#CSV DESTINO DEL NUEVO DATAFRAME
df.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_11.csv', index=False)

print("Archivo procesado y guardado con éxito.")
