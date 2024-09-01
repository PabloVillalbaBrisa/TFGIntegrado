import pandas as pd

df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_8.csv')

#COLUMNA FECHA AL TIPO DATETIME
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

#WEEKEND SERÁ 1 SI CAE FIN DE SEMANA, 0 SI NO. WEEKDAY DA EL DÍA DE LA SEMANA LOS OBJETOS DATETIME
df['weekend'] = df['fecha'].dt.weekday.apply(lambda x: 1 if x >= 5 else 0)

df.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_9.csv', index=False)


