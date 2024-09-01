import pandas as pd


df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_2.csv')

palabras = ['Nike', 'Wilson', 'Yonex', 'Adidas', 'Asics', 'Head']

for palabra in palabras:
    df[palabra] = 0

def buscar_palabra(texto, palabra):
    return 1 if palabra.lower() in texto.lower() else 0

for palabra in palabras:
    df[palabra] = df['Marcas Jugador'].apply(lambda texto: buscar_palabra(texto, palabra))

for palabra in palabras:
    suma = df[palabra].sum()
    print(f"La palabra '{palabra}' aparece en {suma} filas diferentes.")

df.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_2.csv', index=False)
