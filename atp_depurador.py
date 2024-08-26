import pandas as pd

df = pd.read_csv("C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/atp_information_with_age.csv")

#ESTE PROGRAMA ES DE PREPROCESAMIENTO DE DATOS ANTES DE R
#EN EL SCRAPEO, LOS PREMIOS MONETARIOS DE UNIDADES EN MILES SE GUARDARON CON COMAS
#ESTO PROVOCA PROBLEMAS EN EL PROCESAMIENTO POSTERIOR

def extraer_numero_antes_coma(valor):
    if pd.isna(valor):
        return valor
    valor_str = str(valor)
    return valor_str.split(',')[0]

df['Premio monetario'] = df['Premio monetario'].apply(extraer_numero_antes_coma)

df.to_csv("C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/atp_information_R.csv", index=False)
