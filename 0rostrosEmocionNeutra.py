import pandas as pd

file = 'x.csv'
data = pd.read_csv(file)

#ESTE PROGRAMA ES PARA PREPROCESAMIENTO DE LA TABLA DE DATOS
#ANTES DE CARGAR EN R, SE ASIGNA EMOCIÓN NEUTRAL A AQUELLOS POSTS CON 0 ROSTROS DETECTADOS
def set_emotion_neutral_when_no_faces(df):
    #CON LA FUNCIÓN LOC, SE ACCEDE A LAS FILAS DE LAS COLUMNAS INDICADAS
    #SI CUMPLEN LA CONDICIÓN LÓGICA
    df.loc[df['rostros'] == 0, 'emocion'] = 'neutral'
    return df

data = set_emotion_neutral_when_no_faces(data)
data.to_csv('y.csv', index=False)

