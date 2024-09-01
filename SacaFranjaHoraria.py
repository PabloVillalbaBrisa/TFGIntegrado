import pandas as pd

file_path = 'C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_6.csv'  # Actualiza esta ruta con la ruta correcta
data = pd.read_csv(file_path)

#FUNCIÓN QUE CATEGORIZA EN FRANJA HORARIA SEGÚN LAS HORAS
def categorize_time(hour):
    if 5 <= hour < 13:
        return 'Mañana'
    elif 13 <= hour < 21:
        return 'Tarde'
    else:
        return 'Noche'

#COLUMNA HORA A DATETIME
data['hora'] = pd.to_datetime(data['hora'], format='%H:%M:%S', errors='coerce').dt.time

#SE APLICA LA FUNCIÓN Y SE CREA UNA NUEVA COLUMNA FRANJA_HORARIA
data['franja_horaria'] = data['hora'].apply(lambda x: categorize_time(x.hour) if pd.notnull(x) else None)
data.to_csv('C:/Users/pvill/OneDrive/Documentos/TFG INTEGRADO/paolo_metadata_7.csv', index=False)


