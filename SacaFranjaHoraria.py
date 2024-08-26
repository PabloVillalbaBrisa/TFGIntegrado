import pandas as pd

# Cargar el CSV con el que hemos trabajado
file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_6.csv'  # Actualiza esta ruta con la ruta correcta
data = pd.read_csv(file_path)

# Definir una función para categorizar la hora
def categorize_time(hour):
    if 5 <= hour < 13:
        return 'Mañana'
    elif 13 <= hour < 21:
        return 'Tarde'
    else:
        return 'Noche'

# Convertir la columna 'hora' a tipo datetime.time
data['hora'] = pd.to_datetime(data['hora'], format='%H:%M:%S', errors='coerce').dt.time

# Aplicar la función a la columna 'hora' y crear una nueva columna
data['franja_horaria'] = data['hora'].apply(lambda x: categorize_time(x.hour) if pd.notnull(x) else None)
data.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_7.csv', index=False)


