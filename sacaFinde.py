import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_8.csv')

# Asegúrate de que la columna 'fecha' sea de tipo datetime con el formato adecuado
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')

# Crear la columna 'weekend' que será 1 si es fin de semana, 0 si no lo es
df['weekend'] = df['fecha'].dt.weekday.apply(lambda x: 1 if x >= 5 else 0)

# Guardar el DataFrame resultante en un nuevo archivo CSV
df.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_9.csv', index=False)

print(df)
